import sys, json, pathlib
sys.path.insert(0,'/home/claude/som')
import semana3 as s
from anim import render_anim
from sfx2 import KITS, plano_slide, mix
C=pathlib.Path('/home/claude/car')
SOM={'BlackFriday':('cinema',0,None),'SiteVende':('leve',2,None),'Novembro':('tech',1,'contador'),
     'OG_VenderValor':('ritmo',1,None),'OG_Frase28':('classico',0,None),'OG_Domingo29':('leve',1,None)}
for n in (sys.argv[1:] or list(s.D)):
    pasta,S=s.D[n]; anim=C/'out/anim'/pasta
    render_anim(n,S,anim)
    kit,var,extra=SOM[n]; K=KITS[kit]; tot=len(S)
    out=pathlib.Path('/home/claude/som/final')/pasta; out.mkdir(parents=True,exist_ok=True)
    for i in range(1,tot+1):
        ev=json.loads((C/f'_{n}_anim_{i}.ev.json').read_text())
        mix(str(anim/f'{n}_slide_{i}.mp4'),str(out/f'{n}_slide_{i}.mp4'),plano_slide(ev,i,tot,K,var,extra),dur=9.0)
    print('ok',n,flush=True)
