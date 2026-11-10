#!/usr/bin/env bun
/** Build from clean inputs. Package only what the TeX run actually used. */
import { spawnSync } from "node:child_process";
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, renameSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const source = path.resolve(import.meta.dir, "../paper");
const args = process.argv.slice(2);
const usage = "bun scripts/build-paper.ts [--arxiv | --zenodo] [--out-dir DIRECTORY]";
if (args.includes("--help") || args.includes("-h")) { console.log(usage); process.exit(0); }
let mode = "pdf", destination = source;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--out-dir" && args[i+1] && !args[i+1].startsWith("--")) destination = path.resolve(args[++i]);
  else if (mode === "pdf" && ["--arxiv", "--zenodo"].includes(args[i])) mode = args[i].slice(2);
  else throw new Error(usage);
}

// The work tree has no old PDF, bibliography, auxiliary or cached success to reuse.
const work = mkdtempSync(path.join(tmpdir(), "uhm-manuscript-"));
const read = (f: string) => readFileSync(path.join(work, f), "utf8");
const staged = new Set<string>();
function stage(dir: string) {
  for (const e of readdirSync(path.join(source, dir), {withFileTypes:true})) {
    const n = path.join(dir, e.name);
    if (e.name.startsWith(".") || e.name === "zenodo") continue;
    if (e.isDirectory()) { stage(n); continue; }
    // A figure PDF may be an input; a previous manuscript PDF never is.
    if (!e.isFile() || !(/\.(tex|txt|bib|bst|sty|cls|png|jpe?g|eps)$/i.test(n) || /^figures\/.+\.pdf$/.test(n))) continue;
    mkdirSync(path.dirname(path.join(work,n)), {recursive:true});
    copyFileSync(path.join(source,n), path.join(work,n));
    staged.add(n);
  }
}
function run(command: string, args: string[]) {
  const proc = spawnSync(command,args,{cwd:work,encoding:"utf8",maxBuffer:32*1024*1024});
  if (proc.error) throw proc.error;
  if (proc.status !== 0) throw new Error([command+" failed",proc.stdout.slice(-4500),proc.stderr.slice(-1200)].join("\n"));
}
function deliver(name: string, target: string) {
  mkdirSync(path.dirname(target), {recursive:true});
  const temporary = mkdtempSync(path.join(path.dirname(target), ".paper-"));
  try {
    const item = path.join(temporary,"ready");
    copyFileSync(path.join(work,name),item);
    renameSync(item,target);
  } finally { rmSync(temporary,{recursive:true,force:true}); }
  console.log(target);
}
function plain(file: string) {
  const text = read(file).trim().replace(/\s+/g," ");
  if (!text || /[\\%$&#_{}<>^~]/.test(text)) throw new Error(file+" must contain plain publication text");
  return text;
}
try {
  stage("");
  const title=plain("title.txt"), description=plain("abstract.txt");
  run("latexmk",["-pdf","-recorder","-interaction=nonstopmode","-halt-on-error","-file-line-error","main.tex"]);
  const log=read("main.log");
  if (/There were undefined (?:references|citations)|(?:Citation|Reference) .+ undefined|There were multiply-defined labels/.test(log))
    throw new Error("Unresolved citations, references or duplicate labels");
  if (!existsSync(path.join(work,"main.pdf"))) throw new Error("Missing article PDF");
  if (mode === "pdf") deliver("main.pdf",path.join(destination,"uhm-paper.pdf"));
  else {
    const files=new Set<string>();
    for (const line of read("main.fls").split(/\r?\n/)) {
      if (!line.startsWith("INPUT ")) continue;
      const name=path.relative(work,path.resolve(work,line.slice(6)));
      if (staged.has(name)) files.add(name);
    }
    // BibTeX is a separate process, so .bib/.bst inputs are not in the TeX recorder.
    if (existsSync(path.join(work,"main.bbl"))) {
      files.add("main.bbl");
      for (const [ ,kind,values] of read("main.aux").matchAll(/\\bib(data|style)\{([^}]+)\}/g)) {
        for(const value of values.split(",")) {
          const name=value.trim()+(kind==="data"?".bib":".bst");
          if (staged.has(name)) files.add(name);
          else if (kind==="data") throw new Error("Missing local bibliography: "+name);
        }
      }
    }
    for (const n of ["main.tex","title.txt","abstract.txt"])
      if (!files.has(n)) throw new Error("Publication text was not read by TeX: "+n);
    run("tar",[...(process.platform==="darwin"?["--no-mac-metadata"]:[]),"-czf","sources.tar.gz","--",...Array.from(files).sort()]);
    if (mode==="arxiv") deliver("sources.tar.gz",path.join(destination,"uhm-arxiv.tar.gz"));
    else {
      const folder=path.join(destination,"zenodo");
      const metadata={metadata:{title,description,upload_type:"publication",publication_type:"preprint",
        creators:[{name:"Sereda, Max",affiliation:"Independent researcher"}],language:"eng",license:"CC-BY-NC-SA-4.0",access_right:"open",
        related_identifiers:[{relation:"isDocumentedBy",identifier:"https://holon.sh",scheme:"url"}]}};
      writeFileSync(path.join(work,"metadata.json"),JSON.stringify(metadata,null,2)+"\n");
      writeFileSync(path.join(work,"deposit.md"),"# "+title+"\n\n"+description+"\n\nExtract the source archive and run `latexmk -pdf -halt-on-error main.tex` with TeX Live.\n");
      for (const [src,dst] of [["main.pdf","uhm-paper.pdf"],["sources.tar.gz","uhm-paper-source.tar.gz"],
        ["metadata.json","zenodo-metadata.json"],["deposit.md","README.md"]]) deliver(src,path.join(folder,dst));
    }
  }
} finally { rmSync(work,{recursive:true,force:true}); }
