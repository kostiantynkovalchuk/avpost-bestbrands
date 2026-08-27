#!/usr/bin/env python3
"""Inline images/<name> into index.html as base64 (same single-file convention as Issue №1).
Usage: python3 inline_images.py            # writes index.inlined.html
       python3 inline_images.py --in-place # overwrites index.html
Before inlining, resize: max 1600px long edge, JPEG q82 (needs Pillow). Portraits/pets stay ≥900px."""
import re, base64, os, sys, io
try:
    from PIL import Image
except ImportError:
    Image = None
SRC = 'index.html'
html = open(SRC, encoding='utf-8').read()
missing = []
def repl(m):
    rel = m.group(1)
    base = os.path.splitext(os.path.basename(rel))[0]
    cands = [f for f in os.listdir('images') if os.path.splitext(f)[0] == base] if os.path.isdir('images') else []
    if not cands:
        missing.append(rel); return m.group(0)
    path = os.path.join('images', cands[0])
    data = open(path, 'rb').read()
    mime = 'image/png' if path.lower().endswith('.png') else 'image/jpeg'
    if Image:
        im = Image.open(io.BytesIO(data))
        if im.mode in ('RGBA', 'P') and mime == 'image/png':
            pass
        else:
            im = im.convert('RGB'); mime = 'image/jpeg'
        w, h = im.size; mx = 1600
        if max(w, h) > mx:
            im.thumbnail((mx, mx))
        buf = io.BytesIO()
        im.save(buf, 'PNG' if mime == 'image/png' else 'JPEG', **({} if mime == 'image/png' else {'quality': 82, 'optimize': True}))
        data = buf.getvalue()
    return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(data).decode())
out = re.sub(r'src="(images/[^"]+)"', repl, html)
dst = SRC if '--in-place' in sys.argv else 'index.inlined.html'
open(dst, 'w', encoding='utf-8').write(out)
print('written', dst, len(out)//1024, 'KB')
if missing: print('MISSING (left as-is):', *missing, sep='\n  ')
