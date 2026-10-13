"""Smoke checks for template validation and placeholder release blocking."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import package_plugins

ROOT = Path(__file__).resolve().parents[2]
PACKAGER = ROOT / "scripts" / "package_plugins.py"


class TemplatePackagingTests(unittest.TestCase):
    def test_mit_license_allows_plugin_owner_copyright(self) -> None:
        license_text = package_plugins.MIT_LICENSE_TEXT.replace(
            "Copyright (c) 2026 Pupujiang", "Copyright (c) 2026 wtwang1998"
        )
        package_plugins._require_mit_license_text(
            license_text.encode("utf-8"), subject="plugin LICENSE"
        )

    def test_template_placeholders_are_rejected_for_release(self) -> None:
        manifest = json.loads((ROOT / "plugin" / "manifest.json").read_text())
        manifest["id"] = "org.example.plugin-template"
        with tempfile.TemporaryDirectory() as temporary_dir:
            manifest_path = Path(temporary_dir) / "manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "replace the template plugin id"):
                package_plugins._load_manifest(manifest_path, allow_template=False)
        with self.assertRaisesRegex(ValueError, "template placeholder"):
            package_plugins._reject_template_placeholders(
                {"personas.json": b"Replace with a persona"}
            )

    def test_repository_source_passes_check(self) -> None:
        check = subprocess.run(
            [sys.executable, str(PACKAGER), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(check.returncode, 0, check.stderr)


if __name__ == "__main__":
    unittest.main()
