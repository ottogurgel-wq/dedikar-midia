import sys, json, pathlib
sys.path.insert(0,'/home/claude/som')
import semana2_telas as s
from anim import render_anim
from sfx2 import KITS, plano_slide, mix
C=pathlib.Path('/home/claude/car')
SOM={'Receita':('tech',2,None),'Desconto':('ritmo',0,'contador'),'Sexta':('leve',1,None),'Portfolio':('cinema',2,None)}
for n,only in [('Portfolio',[2,3,4,5]),('Desconto',[5]),('Receita',[5]),('Sexta',[5])]:
    pasta,S=s.D[n]; anim=C/'out/anim'/pasta
    render_anim(n,S,anim,only=only)
    kit,var,extra=SOM[n]; K=KITS[kit]; tot=len(S)
    out=pathlib.Path('/home/claude/som/final')/pasta
    for i in only:
        ev=json.loads((C/f'_{n}_anim_{i}.ev.json').read_text())
        mix(str(anim/f'{n}_slide_{i}.mp4'),str(out/f'{n}_slide_{i}.mp4'),plano_slide(ev,i,tot,K,var,extra),dur=9.0)
    print('ok',n,flush=True)
