# Pupu Danmu plugin template

Use this repository template to create one declarative Pupu Danmu plugin repository. The root `LICENSE` covers this template's scaffolding only; it does not choose the license for your plugin. Before publishing, replace every placeholder in `plugin/`, choose a supported plugin license in `plugin/manifest.json`, and provide matching license text in `plugin/LICENSE`.

## Build a plugin Release

1. Replace `org.example.plugin-template`, `0.0.0`, name, description, author, and the placeholder resources in `plugin/`.
2. Choose `MIT` as the plugin license and put the matching MIT text in `plugin/LICENSE`. More plugin license policies can be added after review.
3. Run `python3 scripts/package_plugins.py --check`.
4. Tag the commit as `<plugin-slug>-v<manifest-version>`, for example `community-demo-v0.0.1`, then push the tag. The Release workflow builds the ZIP and SHA-256 file from source and attaches both to the GitHub Release. Never commit generated ZIP files.
5. Submit the Release URL, exact ZIP size, SHA-256, manifest metadata, source repository, and license to the plugin Registry.

Packages contain static JSON/text data only. They cannot include Python, JavaScript, executables, arbitrary files, or instructions that bypass host safety and pacing rules. The host owns generation, account identity, safety checks, and sending.

The Registry stores reviewed Catalog metadata, not package files. See its [contribution guide](https://github.com/pupujiang-org/pupu-danmu-plugin-registry/blob/main/CONTRIBUTING.md) for review requirements.
