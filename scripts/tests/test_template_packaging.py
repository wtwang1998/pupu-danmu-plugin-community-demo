"""Smoke checks for template validation and placeholder release blocking."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGER = ROOT / "scripts" / "package_plugins.py"


class TemplatePackagingTests(unittest.TestCase):
    def test_template_checks_but_cannot_build_release_assets(self) -> None:
        check = subprocess.run(
            [sys.executable, str(PACKAGER), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(check.returncode, 0, check.stderr)

        with tempfile.TemporaryDirectory() as output_dir:
            build = subprocess.run(
                [sys.executable, str(PACKAGER), "--output", output_dir],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(build.returncode, 0)
            self.assertIn("replace the template plugin id", build.stderr)
            self.assertEqual(list(Path(output_dir).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
