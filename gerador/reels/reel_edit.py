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
def montar_base(clip,segs,out):
    src=str(RAW/C[clip]['arquivo']); parts=[]
    for j,(a,b) in enumerate(segs):
        p=R/f'_seg{j}.mp4'; parts.append(p)
        run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',src,'-vf','scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.06,fps=30','-af','highpass=f=80,loudnorm=I=-15:TP=-1.5:LRA=9','-ar','48000','-c:v','libx264','-preset','veryfast','-crf','17','-c:a','aac','-b:a','192k',str(p)])
    (R/'_l.txt').write_text(''.join(f"file '{p}'\n" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(R/'_l.txt'),'-c','copy',out])
    # palavras com tempo remapeado
    W=[];off=0
    for a,b in segs:
        for w in C[clip]['palavras']:
            if a<=w['s']<b: W.append({'w':fix(w['w']),'s':round(w['s']-a+off,2),'e':round(min(w['e'],b)-a+off,2)})
        off+=b-a
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
    base=str(out/'_base.mp4'); W,dur=montar_base(cfg['clip'],cfg['segs'],base)
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
    # efeitos
    ev=[('whoosh_entrada',0.0,.5),('impacto_titulo',0.1,.45)]+[('nota_vidro' if k%2 else 'pop_card',c['t'],.45) for k,c in enumerate(cfg['chips'])]
    ev+=[('digitacao_etiqueta',cfg.get('lt',[2.8])[0],.3),('riser_suave',dur-1.6,.35),('whoosh_entrada',dur-0.1,.45),('chime_cta',dur+0.8,.6)]
    a=['ffmpeg','-v','error','-y','-i',juntos]
    for n,_,_ in ev: a+=['-i',SFX+n+'.mp3']
    f=[f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={v}[a{j}]' for j,(n,t,v) in enumerate(ev)]
    f.append('[0:a]'+''.join(f'[a{j}]' for j in range(len(ev)))+f'amix=inputs={len(ev)+1}:normalize=0[o]')
    final=str(out/f'Reel_{nome}.mp4')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',final]
    run(a); print('ok',final,dur+END)
    return final
