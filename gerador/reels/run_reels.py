import sys; from reels_cfg import CFG; from reel_edit import editar
for n in sys.argv[1:] or list(CFG): editar(n,CFG[n])
