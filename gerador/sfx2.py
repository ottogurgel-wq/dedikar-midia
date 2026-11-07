"""Desenho de som variado: cada peça tem um kit (entrada, meio, fechamento); nem todo elemento tem som; padrão muda de slide para slide."""
import subprocess, json, pathlib
N='/home/claude/sfx_norm/'
KITS={
 'tech':   dict(ent='entrada_glitch', meio='meio_scanner', meio2='meio_tecla',  fecho='fecho_sucesso'),
 'cinema': dict(ent='entrada_boom',   meio='meio_swish',   meio2='impacto_titulo', fecho='fecho_orquestra'),
 'leve':   dict(ent='entrada_reveal', meio='meio_bolha',   meio2='nota_vidro',  fecho='fecho_mensagem'),
 'ritmo':  dict(ent='entrada_tambor', meio='meio_tecla',   meio2='meio_camera', fecho='chime_cta'),
 'classico':dict(ent='whoosh_entrada',meio='nota_vidro',   meio2='meio_swish',  fecho='fecho_sucesso'),
}
def mix(src,dst,ev,dur=None,voz=None,voz_vol=1.0):
    a=['ffmpeg','-v','error','-y','-i',src]; base=1
    if voz: a+=['-i',voz]; base=2
    for n,_,_ in ev: a+=['-i',N+n+'.wav']
    f=[]; lab=[]
    if voz: f.append(f'[1:a]volume={voz_vol}[vz]'); lab.append('[vz]')
    for j,(n,t,v) in enumerate(ev):
        ms=int(max(0,t)*1000); f.append(f'[{j+base}:a]adelay={ms}|{ms},volume={v}[a{j}]'); lab.append(f'[a{j}]')
    if not lab:
        a+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo']; f.append(f'[{base}:a]anull[x]'); lab=['[x]']
    tail=f',apad,atrim=0:{dur},afade=t=out:st={dur-0.5}:d=0.5' if dur else ''
    f.append(''.join(lab)+f'amix=inputs={len(lab)}:normalize=0{tail}[o]')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart']
    if dur: a+=['-t',str(dur)]
    subprocess.run(a+[dst],check=True)
def plano_slide(ev,i,tot,K,var,extra=None):
    """var: deslocamento do padrão (muda entre peças)."""
    if i==1: return [(K['ent'],0.0,.55)]+([(K['meio2'],1.2,.3)] if tot==1 else [])+([(K['fecho'],2.4,.5)] if tot==1 else [])
    tit=[e['t'] for e in ev if e['tipo']=='titulo']; cards=[e['t'] for e in ev if e['tipo']=='card']
    p=[]
    if i==tot:
        pill=[e['t'] for e in ev if e['tipo']=='pill']
        if tit: p.append((K['meio'],tit[0]+.15,.35))
        if pill: p.append((K['fecho'],pill[0]+.45,.6))
        return p
    modo=(i+var)%3
    if modo==0 and tit: p.append((K['meio'],tit[0]+.15,.4))
    if modo==1 and cards: p+= [(K['meio2'],cards[0]+.25,.4)]+([(K['meio2'],cards[-1]+.25,.35)] if len(cards)>2 else [])
    if modo==2: p.append(('meio_swish',0.05,.3))
    for e in ev:
        if e['tipo']=='big': p.append((extra or 'contador',1.6,.55))
    return p
