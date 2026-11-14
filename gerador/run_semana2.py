import sys, json, pathlib
sys.path.insert(0,'/home/claude/som')
from semana2 import D
from anim import render_anim
from sfx2 import KITS, plano_slide, mix
C=pathlib.Path('/home/claude/car')
SOM={'Receita':('tech',2,None),'Desconto':('ritmo',0,'contador'),'Sexta':('leve',1,None),'Portfolio':('cinema',2,None),
     'OG_UmAUm':('classico',1,None),'OG_VendedorNovo':('ritmo',2,None),'OG_Frase19':('leve',0,None),'OG_Domingo22':('tech',0,None)}
for n in (sys.argv[1:] or list(D)):
    pasta,S=D[n]; anim=C/'out/anim'/pasta
    render_anim(n,S,anim)
    kit,var,extra=SOM[n]; K=KITS[kit]; tot=len(S)
    out=pathlib.Path('/home/claude/som/final')/pasta; out.mkdir(parents=True,exist_ok=True)
    for i in range(1,tot+1):
        ev=json.loads((C/f'_{n}_anim_{i}.ev.json').read_text())
        mix(str(anim/f'{n}_slide_{i}.mp4'),str(out/f'{n}_slide_{i}.mp4'),plano_slide(ev,i,tot,K,var,extra),dur=9.0)
    print('ok',n,flush=True)
