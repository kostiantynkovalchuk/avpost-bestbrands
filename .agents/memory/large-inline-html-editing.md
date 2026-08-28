---
name: Large inline HTML editing
description: Safe editing approach for oversized single-file issue pages with embedded base64 images.
---

The issue HTML may exceed the patch tool's 16 MiB file-size limit because all images are embedded as data URIs. When that happens, use a guarded exact-string transformation that checks unique anchors before writing and validates the result afterward.

**Why:** A normal patch cannot open the oversized file, while broad replacements can accidentally match CSS selectors or alter existing image payloads.

**How to apply:** Search body markup from `<body>` rather than the first matching `alt`, validate replacement counts, compare every pre-existing image `src` against the committed version, and run `git diff --check` before committing.