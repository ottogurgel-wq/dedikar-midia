import sys; from automatizar import S; from anim import render_anim
sel=[int(a) for a in sys.argv[1:]] or None
print(render_anim('Automatizar',S,'out/2026-11-10-automatizar-anim',only=sel))
