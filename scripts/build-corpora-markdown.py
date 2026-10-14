#!/usr/bin/env python3
"""Build all five theory corpora, separate Autogeny, and one complete MD bundle.

Uses each repository's scripts/build-markdown.py; Python 3, Bun and Pandoc
must be available. Repository paths can be overridden for independent checkouts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def revision(repo):
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def default_synarc():
    repo = (ROOT / "internal/synarc-omega").resolve()
    if (repo / "scripts/build-markdown.py").is_file() or not repo.is_dir():
        return repo
    # A new exporter may be committed in the active worktree while main awaits
    # its independent integration checks. Never guess between multiple editions.
    result = subprocess.run(["git", "-C", str(repo), "worktree", "list", "--porcelain"],
                            text=True, capture_output=True, check=True)
    candidates = [Path(line.removeprefix("worktree ")) for line in result.stdout.splitlines()
                  if line.startswith("worktree ")]
    candidates = [path for path in candidates if (path / "scripts/build-markdown.py").is_file()]
    if len(candidates) == 1:
        print(f"SYNARC exporter is in worktree: {candidates[0]}", flush=True)
        return candidates[0]
    return repo  # The normal preflight reports the missing exporter and override.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output/markdown/corpora")
    parser.add_argument("--uhm-root", type=Path, default=ROOT)
    parser.add_argument("--diakrisis-root", type=Path, default=ROOT / "internal/diakrisis")
    parser.add_argument("--foundations-root", type=Path,
                        default=ROOT / "internal/diakrisis/internal/math-foundations")
    parser.add_argument("--msfs-root", type=Path, default=ROOT / "internal/math-msfs")
    parser.add_argument("--synarc-root", type=Path)
    args = parser.parse_args()
    repos = {"math-foundations": args.foundations_root.resolve(),
             "uhm": args.uhm_root.resolve(), "diakrisis": args.diakrisis_root.resolve(),
             "msfs": args.msfs_root.resolve(),
             "synarc": (args.synarc_root or default_synarc()).resolve()}
    for name, repo in repos.items():
        if not (repo / "scripts/build-markdown.py").is_file():
            parser.error(f"Missing {name} exporter: {repo / 'scripts/build-markdown.py'}; "
                         "supply the corresponding --*-root argument")
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    # Publish only after every corpus succeeded. A failed build leaves the
    # previous delivery intact; only our isolated temporary directory is removed.
    with tempfile.TemporaryDirectory(prefix=".corpora-build-", dir=output.parent) as temp:
        stage = Path(temp)
        records, published = [], {}
        for name, repo in repos.items():
            edition = stage / name
            before = revision(repo)
            subprocess.run([sys.executable, str(repo / "scripts/build-markdown.py"),
                            "--output-dir", str(edition)], check=True)
            if revision(repo) != before:
                raise RuntimeError(f"{name} checkout changed during export; rerun")
            files = []
            for source in sorted(edition.iterdir()):
                if source.suffix not in {".md", ".json"}:
                    continue
                target = source.name if source.suffix == ".md" else f"{name}-{source.name}"
                if target in published:
                    raise RuntimeError("Duplicate artifact name: " + target)
                data = source.read_bytes()
                published[target] = data
                files.append({"file": target, "bytes": len(data), "sha256": sha(data)})
            records.append({"corpus": name, "repository": str(repo), "head": before,
                            "exporter_sha256": sha((repo / "scripts/build-markdown.py").read_bytes()),
                            "artifacts": files})

        request = repos["synarc"] / "reference/research/2026-10-14-external-research-request-ru.md"
        if request.is_file():
            published["research-request-ru.md"] = request.read_bytes()
        primary = [("Mathematical Foundations (including Autogeny)", "math-foundations.md"),
                   ("UHM / УГМ", "uhm-ru.md"), ("Diakrisis", "diakrisis-ru.md"),
                   ("MSFS", "msfs-ru.md"), ("SYNARC", "synarc-ru.md")]
        chunks = [b"# Complete theory corpora\n\n",
                  b"Five complete corpora follow, without summarization. Autogeny is already "
                  b"included in Mathematical Foundations. Russian editions are selected where "
                  b"available. Separate English and exact LaTeX-source editions accompany this "
                  b"file. Each constituent below is preserved byte-for-byte; source hashes, "
                  b"coverage and conversion details are recorded in the accompanying manifests. "
                  b"Original links and image references remain source references; TikZ diagrams "
                  b"are retained as LaTeX code. This compilation contains the theory documents, "
                  b"not the implementation or experiment datasets.\n\n"]
        for index, (title, filename) in enumerate(primary, 1):
            data = published[filename]
            start = f"<!-- BEGIN COMPLETE CORPUS {index}: {filename} -->\n".encode()
            stop = f"\n<!-- END COMPLETE CORPUS {index} -->".encode()
            if start in data or stop in data:
                raise RuntimeError("Corpus delimiter collision: " + filename)
            chunks.extend([f"\n\n---\n\n# Corpus {index}: {title}\n\n".encode(),
                           start, data, stop, b"\n"])
        combined = b"".join(chunks)
        for index, (_, filename) in enumerate(primary, 1):
            start = f"<!-- BEGIN COMPLETE CORPUS {index}: {filename} -->\n".encode()
            stop = f"\n<!-- END COMPLETE CORPUS {index} -->".encode()
            recovered = combined.split(start, 1)[1].split(stop, 1)[0]
            if recovered != published[filename]:
                raise RuntimeError("Combined corpus verification failed: " + filename)
        published["all-corpora.md"] = combined
        lines = ["# Полные корпуса в Markdown\n\n",
                 "`all-corpora.md` объединяет пять полных корпусов: math-foundations, УГМ, "
                 "Diakrisis, MSFS и SYNARC. Аутогения уже входит в math-foundations; "
                 "`autogeny.md` предоставлен отдельно для удобства. Это полные тексты, без "
                 "сокращения. Для больших корпусов удобнее отправлять отдельные файлы.\n\n",
                 "| Файл | Размер, МБ (10⁶ байт) |\n|---|---:|\n"]
        for filename, data in sorted(published.items()):
            if filename.endswith(".md"):
                lines.append(f"| [{filename}]({filename}) | {len(data) / 1_000_000:.2f} |\n")
        lines.append("\nФайлы `*-source.md` содержат точные исходники LaTeX/BibTeX. "
                     "В читаемых версиях формулы сохранены в LaTeX, неподдержанные окружения "
                     "и TikZ — в блоках кода. Бинарные изображения не встраиваются; "
                     "для отрисованных схем используйте исходные PDF/сайт.\n\n"
                     "Каждый корпус проверен собственным сборщиком; манифесты содержат "
                     "хеши исходников и проверки полноты. Общий манифест фиксирует "
                     "ревизии репозиториев и хеши отправляемых файлов. "
                     "`research-request-ru.md`, если он присутствует, содержит самодостаточную "
                     "постановку вопросов для внешних исследователей.\n")
        published["README.md"] = "".join(lines).encode()
        report = {"schema_version": 1, "corpora": records,
                  "research_request_source": str(request) if request.is_file() else None,
                  "combined_order": [filename for _, filename in primary],
                  "combined_roundtrip": True,
                  "artifacts": [{"file": name, "bytes": len(data), "sha256": sha(data)}
                                for name, data in sorted(published.items())]}
        published["corpora-manifest.json"] = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode()
        for name, data in published.items():
            temporary = stage / name
            temporary.write_bytes(data)
            os.replace(temporary, output / name)
        print(f"\nReady: {output / 'README.md'}")
        print(f"Combined: {output / 'all-corpora.md'} ({len(combined):,} bytes)")


if __name__ == "__main__":
    main()
