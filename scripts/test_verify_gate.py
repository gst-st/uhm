#!/usr/bin/env python3
"""Regression checks for fail-closed orchestration of corpus verifiers."""
import contextlib
import io
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

import verify_gate


class GateTests(unittest.TestCase):
    def run_gate(self, outcomes):
        calls = []

        def tool(command, **kwargs):
            name = Path(command[1]).name
            calls.append(name)
            code, stdout, stderr = outcomes.get(name, (0, 'файлов: 1\n', ''))
            return subprocess.CompletedProcess(command, code, stdout, stderr)

        output = io.StringIO()
        with patch.object(verify_gate.subprocess, 'run', side_effect=tool), \
                patch.object(Path, 'exists', return_value=True), \
                contextlib.redirect_stdout(output):
            code = verify_gate.main()
        self.assertEqual(set(calls), set(verify_gate.TOOLS) |
                         {p.name for p in verify_gate.SITE_TOOLS})
        return code, output.getvalue()

    def test_formal_checker_failure_closes_gate_and_reports_diagnostic(self):
        code, output = self.run_gate({'verify_readout_descent.py':
                                     (1, '', 'Lean replay failed')})
        self.assertEqual(code, 1)
        self.assertIn('Lean replay failed', output)

    def test_success_without_declared_scope_is_rejected(self):
        code, output = self.run_gate({'verify_readout_descent.py':
                                     (0, 'success\n', '')})
        self.assertEqual(code, 1)
        self.assertIn('ОХВАТ НЕ НАЗВАН: verify_readout_descent.py', output)

    def test_site_checker_without_scope_is_also_rejected(self):
        code, _ = self.run_gate({'render_lint.py': (0, '', '')})
        self.assertEqual(code, 1)

    def test_mixed_file_and_proof_counts_are_valid(self):
        code, output = self.run_gate({'verify_readout_descent.py':
                                     (0, 'проверок: 21\n', '')})
        self.assertEqual(code, 0)
        self.assertIn('verify_readout_descent.py — проверок 21', output)

    def test_existing_explicit_non_corpus_witness_exemption_is_preserved(self):
        code, _ = self.run_gate({'natal_startup_verify.py': (0, '', '')})
        self.assertEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
