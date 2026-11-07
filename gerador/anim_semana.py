import sys
from semana import D
from anim import render_anim
from sfx_mix import mix_tudo
for n in (sys.argv[1:] or list(D)):
    pasta,S=D[n]
    render_anim(n,S,f'out/anim/{pasta}')
    mix_tudo(n,f'out/anim/{pasta}',f'out/final/{pasta}',len(S))
    print('ok',n,flush=True)
