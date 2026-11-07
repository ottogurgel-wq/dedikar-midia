"""Edição dos reels gravados do Otto no padrão Dedikar: gancho, legenda da marca, chamadas, efeitos ElevenLabs e fechamento 'Comente PALAVRA'."""
import json, subprocess, asyncio, pathlib, re, shutil, sys
from playwright.async_api import async_playwright
R=pathlib.Path(__file__).parent; RAW=pathlib.Path('/home/claude/videos_raw'); SFX='/home/claude/dedikar-midia/sfx/'
C=json.load(open(RAW/'clipes.json'))
FPS=30
FIX=[(r'Dedicare?\s*IA','Dedikar IA'),(r'Dedicare?','Dedikar'),(r'dedicareia\.com\.br','dedikaria.com.br'),(r'Carpiiina','Carpina'),(r'regiããão','região'),(r'Olááá','Olá'),(r'ro-rotineiras','rotineiras'),(r'custoooom','custo')]
def fix(w):
    for a,b in FIX: w=re.sub(a,b,w)
    return w
def run(a): subprocess.run(a,check=True)
def montar_base(clip,segs,out,zooms=(),vfim=None):
    (a,b),=segs
    src=str(RAW/C[clip]['arquivo'])
    cond='+'.join(f'between(t,{z0-a:.2f},{z1-a:.2f})' for z0,z1 in zooms) or '0'
    vf=(f"scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.06,"
        f"scale=w='1080*(1+0.12*gt({cond},0))':h='1920*(1+0.12*gt({cond},0))':eval=frame:flags=lanczos,"
        f"crop=1080:1920:x='(iw-1080)/2':y='(ih-1920)*0.30',fps=30")
    if vfim: vf+=f",trim=end={vfim-a:.2f},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={b-vfim:.2f}"
    run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',src,'-vf',vf,'-af','highpass=f=80,loudnorm=I=-15:TP=-1.5:LRA=9,afade=t=out:st='+str(round(b-a-0.08,2))+':d=0.08','-ar','48000','-c:v','libx264','-preset','veryfast','-crf','17','-c:a','aac','-b:a','192k',out])
    W=[{'w':fix(w['w']),'s':round(w['s']-a,2),'e':round(min(w['e'],b)-a,2)} for w in C[clip]['palavras'] if a<=w['s']<b]
    return W,b-a
def montar_multi(cortes,out):
    """cortes: lista de (clip, inicio, fim, zoom). Uma passada: vídeo e áudio cortados juntos, zoom diferente em cada corte."""
    ins=[];fc=[];vlab=[];W=[];off=0
    srcs=[]
    for c,a,b,z in cortes:
        if c not in srcs: srcs.append(c)
    for c in srcs: ins+=['-i',str(RAW/C[c]['arquivo'])]
    for k,(c,a,b,z) in enumerate(cortes):
        n=srcs.index(c)
        fc.append(f"[{n}:v]trim={a}:{b},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.06,scale={int(1080*z)//2*2}:{int(1920*z)//2*2}:flags=lanczos,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.30,fps=30,setsar=1[v{k}]")
        fc.append(f"[{n}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.05:.2f}:d=0.05[a{k}]")
        vlab.append(f'[v{k}][a{k}]')
        for w in C[c]['palavras']:
            if a<=w['s']<b: W.append({'w':fix(w['w']),'s':round(w['s']-a+off,2),'e':round(min(w['e'],b)-a+off,2)})
        off+=b-a
    fc.append(''.join(vlab)+f'concat=n={len(cortes)}:v=1:a=1[vv][aa];[aa]highpass=f=80,loudnorm=I=-15:TP=-1.5:LRA=9[ao]')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[vv]','-map','[ao]','-ar','48000','-c:v','libx264','-preset','veryfast','-crf','17','-c:a','aac','-b:a','192k',out])
    return W,off
def grupos(W,maxw=3):
    G=[];cur=[]
    for w in W:
        if w['w'].startswith('Uuu'): continue
        cur.append(w)
        if len(cur)>=maxw or re.search(r'[.,?!:]$',w['w']): G.append(cur);cur=[]
    if cur: G.append(cur)
    return [{'s':g[0]['s'],'e':(G_next:=None) or g[-1]['e'],'p':[{'w':x['w'],'s':x['s']} for x in g]} for g in G]
CSS=open(R/'reel.css').read()
def html_overlay(cfg,G,dur):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div id=brand class=brand><div class=tile><img src="logo.png"></div><span>Dedikar <b>IA</b></span></div>
<div id=hook class=hook><div class=hk>{cfg['hook_k']}</div><div class=ht>{cfg['hook']}</div></div>
<div id=lt class=lt><b>Otto Gurgel</b><span>fundador da Dedikar IA</span></div>
<div id=chips></div><div id=cap class=cap></div>
<script>const G={json.dumps(G,ensure_ascii=False)};const CH={json.dumps(cfg['chips'],ensure_ascii=False)};const KW={json.dumps(cfg['kw'],ensure_ascii=False)};const HOOK={cfg.get('hook_dur',2.6)};const LT={json.dumps(cfg.get('lt',[2.8,6.3]))};
const ease=x=>1-Math.pow(1-Math.min(1,Math.max(0,x)),3);
function setT(t){{
 const h=document.getElementById('hook');const a=t<HOOK?ease(t/0.45):1-ease((t-HOOK)/0.4);h.style.opacity=a;h.style.transform='translateY('+((1-a)*-40)+'px) scale('+(0.94+0.06*a)+')';
 const l=document.getElementById('lt');const b=(t>=LT[0]&&t<LT[1])?ease((t-LT[0])/0.5)*(1-ease((t-LT[1]+0.4)/0.4)):0;l.style.opacity=b;l.style.transform='translateX('+((1-b)*-60)+'px)';
 let g=null;for(let i=0;i<G.length;i++){{const nx=i+1<G.length?G[i+1].s-0.05:1e9;if(t>=G[i].s-0.05&&t<Math.min(nx,G[i].e+0.9)){{g=G[i];break}}}}const cap=document.getElementById('cap');
 if(!g||t<HOOK-0.3){{cap.innerHTML='';}}else{{const k=ease((t-g.s+0.05)/0.18);cap.style.transform='scale('+(0.86+0.14*k)+')';cap.style.opacity=k;
  cap.innerHTML=g.p.map(p=>{{const kw=KW.some(x=>p.w.toLowerCase().replace(/[.,?!:]/g,'').startsWith(x));const on=t>=p.s;return '<span class="'+(kw?'g ':'')+(on?'on':'')+'">'+p.w+'</span>'}}).join(' ');}}
 const ch=document.getElementById('chips');ch.innerHTML='';CH.forEach((c,i)=>{{if(t>=c.t&&t<c.t+c.d){{const k=ease((t-c.t)/0.35)*(1-ease((t-c.t-c.d+0.35)/0.35));ch.innerHTML+='<div class=chip style="top:'+c.y+'px;opacity:'+k+';transform:translateX('+((1-k)*80)+'px) scale('+(0.9+0.1*k)+')"><i>'+c.i+'</i>'+c.txt+'</div>'}}}});
}}</script></body></html>"""
async def frames(html,dur,outdir,transp=True,w=1080,h=1920):
    async with async_playwright() as pw:
        b=await pw.chromium.launch();pg=await b.new_page(viewport={'width':w,'height':h})
        f=R/'_ov.html';f.write_text(html);await pg.goto(f.resolve().as_uri());await pg.wait_for_timeout(500)
        for i in range(int(dur*FPS)):
            await pg.evaluate(f'setT({i/FPS})');await pg.screenshot(path=str(outdir/f'{i:05d}.png'),omit_background=transp)
        await b.close()
def fecho_html(cfg):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body class=end>
<canvas id=c></canvas><div class=endbox><div class=brand2><div class=tile><img src="logo.png"></div><span>Dedikar <b>IA</b></span></div>
<div id=e1 class=et>{cfg['fecho']}</div><div id=e2 class=ep>Comente a palavra</div><div id=e3 class=pill>{cfg['palavra']}</div><div id=e4 class=ep2>{cfg['fecho_sub']}</div><div id=e5 class=site>dedikaria.com.br</div></div>
<script>const c=document.getElementById('c');c.width=1080;c.height=1920;const x=c.getContext('2d');let s=7;const r=()=>{{s=(s*16807)%2147483647;return s/2147483647}};const p=[];for(let i=0;i<90;i++)p.push([r()*1080,r()*1920,r()*6.28,10+r()*20]);
const ease=x=>1-Math.pow(1-Math.min(1,Math.max(0,x)),3);
function setT(t){{x.clearRect(0,0,1080,1920);const w=t*0.9;const q=p.map(a=>[a[0]+Math.cos(w+a[2])*a[3],a[1]+Math.sin(w+a[2])*a[3]]);
for(const a of q)for(const b of q){{const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<190){{x.strokeStyle='rgba(56,217,236,'+(.16*(1-d/190))+')';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}}}
for(const a of q){{x.fillStyle='rgba(56,217,236,.6)';x.beginPath();x.arc(a[0],a[1],2.6,0,7);x.fill()}}
[['e1',0.1],['e2',0.5],['e3',0.8],['e4',1.2],['e5',1.5]].forEach(([id,d])=>{{const e=document.getElementById(id);const k=ease((t-d)/0.6);e.style.opacity=k;e.style.transform='translateY('+((1-k)*40)+'px)'}});
const pl=document.getElementById('e3');pl.style.boxShadow='0 0 '+(70+40*Math.sin(t*3))+'px rgba(56,217,236,.6)';}}</script></body></html>"""
def editar(nome,cfg):
    out=R/'out'/nome; out.mkdir(parents=True,exist_ok=True)
    base=str(out/'_base.mp4'); W,dur=montar_multi(cfg['cortes'],base) if 'cortes' in cfg else montar_base(cfg['clip'],cfg['segs'],base,cfg.get('zooms',()),cfg.get('vfim'))
    G=grupos(W); (out/'legenda.json').write_text(json.dumps(W,ensure_ascii=False))
    fr=R/'_fr'; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
    asyncio.run(frames(html_overlay(cfg,G,dur),dur,fr))
    ov=str(out/'_ov.mov')
    run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(fr/'%05d.png'),'-c:v','qtrle',ov])
    shutil.rmtree(fr); fr.mkdir()
    END=3.2; asyncio.run(frames(fecho_html(cfg),END,fr,transp=False))
    endv=str(out/'_end.mp4')
    run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(fr/'%05d.png'),'-f','lavfi','-t',str(END),'-i','anullsrc=r=48000:cl=stereo','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-shortest',endv])
    shutil.rmtree(fr)
    # vídeo principal com overlay
    mainv=str(out/'_main.mp4')
    run(['ffmpeg','-v','error','-y','-i',base,'-i',ov,'-filter_complex','[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]','-map','[v]','-map','0:a','-c:v','libx264','-preset','veryfast','-crf','18','-c:a','aac','-b:a','192k',mainv])
    (R/'_l.txt').write_text(f"file '{mainv}'\nfile '{endv}'\n")
    juntos=str(out/'_juntos.mp4')
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(R/'_l.txt'),'-c:v','libx264','-preset','veryfast','-crf','18','-c:a','aac',juntos])
    # efeitos (desenho próprio de cada reels)
    ev=[(n,(dur+float(t[3:]) if isinstance(t,str) else t),v) for n,t,v in cfg['sfx']]
    ev=[(n,t,v) for n,t,v in ev]
    a=['ffmpeg','-v','error','-y','-i',juntos]
    for n,_,_ in ev: a+=['-i','/home/claude/sfx_norm/'+n+'.wav']
    f=[f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={v}[a{j}]' for j,(n,t,v) in enumerate(ev)]
    f.append('[0:a]'+''.join(f'[a{j}]' for j in range(len(ev)))+f'amix=inputs={len(ev)+1}:normalize=0[o]')
    final=str(out/f'Reel_{nome}.mp4')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',final]
    run(a); print('ok',final,dur+END)
    return final
