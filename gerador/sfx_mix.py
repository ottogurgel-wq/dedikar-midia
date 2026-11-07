import subprocess, json, pathlib
SFX='/home/claude/dedikar-midia/sfx/'
DUR=9.0
def plano(ev,capa):
    p=[('impacto_titulo',0.0,.45),('digitacao_etiqueta',0.15,.35)] if capa else [('whoosh_entrada',0.0,.4)]
    n=0
    for e in ev:
        t=e['t']
        if e['tipo']=='k': p.append(('digitacao_etiqueta',t+.1,.35))
        elif e['tipo']=='titulo': p.append(('impacto_titulo',t+.15,.42))
        elif e['tipo']=='card': p.append((('pop_card','nota_vidro')[n%2],t+.25,.5)); n+=1
        elif e['tipo']=='big': p.append(('contador',1.6,.55))
        elif e['tipo']=='pill': p+= [('riser_suave',max(0,t-1.4),.35),('chime_cta',t+.45,.6)]
    return p
def mix(src,dst,ev,capa):
    ev=plano(ev,capa); a=['ffmpeg','-v','error','-y','-i',src]
    for n,_,_ in ev: a+=['-i',SFX+n+'.mp3']
    f=[f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={v}[a{j}]' for j,(n,t,v) in enumerate(ev)]
    f.append(''.join(f'[a{j}]' for j in range(len(ev)))+f'amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{DUR},afade=t=out:st={DUR-.5}:d=0.5[o]')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','160k','-t',str(DUR),dst]
    subprocess.run(a,check=True)
def mix_tudo(prefix,anim_dir,final_dir,n):
    fd=pathlib.Path(final_dir); fd.mkdir(parents=True,exist_ok=True); R=pathlib.Path(__file__).parent
    for i in range(1,n+1):
        ev=json.loads((R/f'_{prefix}_anim_{i}.ev.json').read_text())
        mix(f'{anim_dir}/{prefix}_slide_{i}.mp4',str(fd/f'{prefix}_slide_{i}.mp4'),ev,i==1)
if __name__=='__main__':
    mix_tudo('Automatizar','out/2026-11-10-automatizar-anim','out/2026-11-10-automatizar-final',6); print('ok')
