import json, pathlib
from sfx2 import KITS, plano_slide, mix
C=pathlib.Path('/home/claude/car')
PECAS=[ # nome, pasta anim, pasta final, kit, var, extra(big)
 ('Automatizar',C/'out/2026-11-10-automatizar-anim','dedikar/2026-11-10-automatizar','ritmo',0,'contador'),
 ('Diagnostico',C/'out/anim/dedikar/2026-11-12-termometro','dedikar/2026-11-12-termometro','tech',1,None),
 ('Caixa',C/'out/anim/dedikar/2026-11-13-projecao-caixa','dedikar/2026-11-13-projecao-caixa','classico',2,'fecho_caixa'),
 ('Agentes',C/'out/anim/dedikar/2026-11-16-tres-agentes','dedikar/2026-11-16-tres-agentes','cinema',0,None),
 ('OG_Reuniao',C/'out/anim/ottogurgel/2026-11-10-reuniao-segunda','ottogurgel/2026-11-10-reuniao-segunda','leve',2,None),
 ('OG_Indicadores',C/'out/anim/ottogurgel/2026-11-13-indicadores-meio','ottogurgel/2026-11-13-indicadores-meio','tech',0,None),
 ('OG_Frase12',C/'out/anim/ottogurgel/2026-11-12-frase','ottogurgel/2026-11-12-frase','cinema',0,None),
 ('OG_Domingo15',C/'out/anim/ottogurgel/2026-11-15-perguntas','ottogurgel/2026-11-15-perguntas','ritmo',1,None),
]
for nome,anim,final,kit,var,extra in PECAS:
    fs=sorted(anim.glob(f'{nome}_slide_*.mp4')); tot=len(fs); K=KITS[kit]
    out=pathlib.Path('/home/claude/som/final')/final; out.mkdir(parents=True,exist_ok=True)
    for i in range(1,tot+1):
        ev=json.loads((C/f'_{nome}_anim_{i}.ev.json').read_text())
        p=plano_slide(ev,i,tot,K,var,extra)
        if nome=='OG_Reuniao' and i==3: p.append(('meio_relogio',0.9,.3))
        mix(str(anim/f'{nome}_slide_{i}.mp4'),str(out/f'{nome}_slide_{i}.mp4'),p,dur=9.0)
    print('ok',nome,kit,flush=True)
