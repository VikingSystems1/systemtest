---
name: ImageMagick background removal
description: How to remove white backgrounds from logo images in this Replit environment
---

PIL/Pillow is not available without Nix setup. ImageMagick (`magick`) is pre-installed.

**Command:**
```bash
magick input.png -fuzz 15% -transparent white output.png
```

**Why:** `-fuzz 15%` catches near-white pixels at logo edges, not just pure #ffffff.

**How to apply:** Any time a user uploads a PNG logo with a white background that needs transparency. Adjust fuzz % if edges look jagged (up) or bleed into logo colors (down).
