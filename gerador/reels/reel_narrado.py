"""Reels narrados (ElevenLabs) em motion graphics: cenas de texto grande, legenda sincronizada pelos tempos da voz, efeitos."""
import json, subprocess, asyncio, pathlib, shutil, re
from playwright.async_api import async_playwright
R=pathlib.Path(__file__).parent; M=pathlib.Path('/home/claude/dedikar-midia'); SFX=str(M/'sfx')+'/'
FPS=30
def palavras(js):
    a=json.load(open(js))['alignment']; ch=a['characters']; st=a['character_start_times_seconds']; en=a['character_end_times_seconds']
    W=[];cur='';s=None
    for c,t0,t1 in zip(ch,st,en):
        if c.isspace():
            if cur: W.append({'w':cur,'s':s,'e':t1}); cur=''
        else:
            if not cur: s=t0
            cur+=c; e=t1
    if cur: W.append({'w':cur,'s':s,'e':e})
    return W
def achar(W,frase):
    alvo=frase.lower().split()
    for i in range(len(W)):
        if all(W[i+j]['w'].lower().strip('.,?!:"“”').startswith(alvo[j]) for j in range(len(alvo)) if i+j<len(W)): return W[i]['s']
    raise ValueError(frase)
TEMAS={
'dedikar':dict(bg='#0b0b10',lin='56,217,236',pt='rgba(56,217,236,.6)',fh="600 {s}px/1.04 'Cormorant Garamond'",it="italic",acc='#38d9ec',grad='#38d9ec 0%,#7aa2ff 50%,#b48cff 100%',cap="700 64px/1.2 'DM Sans'",handle='@dedikar.ia',up='none'),
'og':dict(bg='radial-gradient(ellipse 900px 900px at 85% 10%,#0a3aa8,rgba(10,58,168,0) 70%),radial-gradient(ellipse 900px 900px at 0% 100%,#06307e,rgba(6,48,126,0) 70%),#020a2c',lin='80,150,255',pt='rgba(140,200,255,.85)',fh="800 {s}px/1.06 'Poppins'",it="normal",acc='#4fc3f7',grad='#4fc3f7 0%,#2f8cff 50%,#8fb8ff 100%',cap="700 60px/1.2 'Poppins'",handle='@ottogurgel.ofc',up='uppercase'),
}
FONTS="""@font-face{font-family:'DM Sans';src:url('fonts/fontsource-dm-sans-5.1.0/package/files/dm-sans-latin-700-normal.woff2');font-weight:700}
@font-face{font-family:'DM Sans';src:url('fonts/fontsource-dm-sans-5.1.0/package/files/dm-sans-latin-500-normal.woff2');font-weight:500}
@font-face{font-family:'Cormorant Garamond';src:url('fonts/fontsource-cormorant-garamond-5.1.0/package/files/cormorant-garamond-latin-600-normal.woff2');font-weight:600}
@font-face{font-family:'Cormorant Garamond';src:url('fonts/fontsource-cormorant-garamond-5.1.0/package/files/cormorant-garamond-latin-600-italic.woff2');font-weight:600;font-style:italic}
@font-face{font-family:'JetBrains Mono';src:url('fonts/fontsource-jetbrains-mono-5.1.0/package/files/jetbrains-mono-latin-700-normal.woff2');font-weight:700}
""" + ''.join(f"@font-face{{font-family:'Poppins';src:url('fonts/poppins/package/files/poppins-latin-{w}-normal.woff2');font-weight:{w}}}" for w in (400,600,700,800))
def html(T,cenas,W,dur):
    css=FONTS+f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:{T['bg']};color:#fff;overflow:hidden;position:relative;font-family:'DM Sans';font-variant-numeric:lining-nums}}canvas{{position:absolute;inset:0}}
.sc{{position:absolute;left:84px;right:84px;top:330px;height:900px;display:flex;flex-direction:column;justify-content:center;gap:34px;opacity:0}}
.k{{font:700 30px 'JetBrains Mono';letter-spacing:5px;color:{T['acc']};text-transform:uppercase}}
.h{{font:{T['fh'].format(s=112)};text-transform:{T['up']}}}.h i,.big i{{font-style:{T['it']};background:linear-gradient(100deg,{T['grad']});background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}}
.big{{font:{T['fh'].format(s=300)}}}
.p{{font:500 46px/1.35 'DM Sans';color:#d6dbea}}.p b{{color:#fff}}.p s{{color:#ff6b61}}
.chip{{display:flex;align-items:center;gap:22px;background:rgba(12,16,34,.85);border:2px solid {T['acc']};border-radius:26px;padding:26px 32px;font:700 46px 'DM Sans'}}.chip u{{text-decoration:none;width:60px;height:60px;border-radius:50%;background:{T['acc']};color:#0b0b10;display:flex;align-items:center;justify-content:center;font:800 32px 'DM Sans';flex-shrink:0}}
.pill{{align-self:flex-start;background:{T['acc']};color:#0b0b10;border-radius:90px;padding:30px 56px;font:700 76px 'JetBrains Mono';letter-spacing:6px}}
.brand{{position:absolute;left:84px;top:160px;display:flex;align-items:center;gap:16px;font:600 38px 'Cormorant Garamond'}}.tile{{width:58px;height:58px;background:#fff;border-radius:14px;display:flex;align-items:center;justify-content:center}}.tile img{{width:48px}}.brand b{{color:{T['acc']};font-weight:600}}
.og{{position:absolute;left:84px;top:160px;font:400 34px 'Poppins';letter-spacing:10px;display:flex;align-items:center;gap:18px}}
.cap{{position:absolute;left:70px;right:70px;top:1330px;text-align:center;font:{T['cap']}}}.cap span{{color:rgba(255,255,255,.45)}}.cap span.on{{color:#fff}}
.hd{{position:absolute;left:84px;bottom:360px;font:700 30px 'JetBrains Mono';color:{T['acc']}}}"""
    topo='<div class=brand><div class=tile><img src="logo.png"></div>Dedikar <b>IA</b></div>' if T['handle']=='@dedikar.ia' else '<div class=og><svg width="70" height="56" viewBox="0 0 78 62" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="26" cy="26" r="22"/><path d="M73 30a22 22 0 1 1-6-15"/><path d="M73 36h-14"/></svg>OTTO GURGEL</div>'
    sc=''.join(f'<div class=sc id=s{i}>{c["html"]}</div>' for i,c in enumerate(cenas))
    G=[];cur=[]
    for w in W:
        cur.append(w)
        if len(cur)>=4 or re.search(r'[.,?!:]$',w['w']): G.append(cur);cur=[]
    if cur:G.append(cur)
    G=[{'s':g[0]['s'],'e':g[-1]['e'],'p':[{'w':x['w'],'s':x['s']} for x in g]} for g in G]
    tempos=[c['t'] for c in cenas]+[dur]
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body><canvas id=c></canvas>{topo}{sc}<div id=cap class=cap></div><div class=hd>{T['handle']}</div>
<script>const TS={json.dumps(tempos)};const G={json.dumps(G,ensure_ascii=False)};const FIM={cenas[-1]['t']};
const c=document.getElementById('c');c.width=1080;c.height=1920;const x=c.getContext('2d');let sd=13;const r=()=>{{sd=(sd*16807)%2147483647;return sd/2147483647}};const p=[];for(let i=0;i<95;i++)p.push([r()*1080,r()*1920,r()*6.28,12+r()*22]);
const ease=v=>1-Math.pow(1-Math.min(1,Math.max(0,v)),3);
function setT(t){{x.clearRect(0,0,1080,1920);const w=t*0.7;const q=p.map(a=>[a[0]+Math.cos(w+a[2])*a[3],a[1]+Math.sin(w+a[2])*a[3]]);x.lineWidth=1.2;
for(const a of q)for(const b of q){{const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<200){{x.strokeStyle='rgba({T['lin']},'+(.2*(1-d/200))+')';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}}}
for(const a of q){{x.fillStyle='{T['pt']}';x.beginPath();x.arc(a[0],a[1],2.8,0,7);x.fill()}}
for(let i=0;i<TS.length-1;i++){{const e=document.getElementById('s'+i);const a=ease((t-TS[i])/0.5),b=(i<TS.length-2)?ease((t-TS[i+1]+0.25)/0.3):0;const k=Math.max(0,a-b);e.style.opacity=k;e.style.transform='translateY('+((1-a)*50-b*30)+'px)';
 [...e.querySelectorAll('.st')].forEach((el,j)=>{{const kk=ease((t-TS[i]-0.35-0.45*j)/0.45);el.style.opacity=kk;el.style.transform='translateX('+((1-kk)*60)+'px)'}});
 [...e.querySelectorAll('i')].forEach(el=>el.style.backgroundPosition=(-(t*55)%250)+'% 0');}}
const cap=document.getElementById('cap');let g=null;for(let i=0;i<G.length;i++){{const nx=i+1<G.length?G[i+1].s-0.05:1e9;if(t>=G[i].s-0.05&&t<Math.min(nx,G[i].e+0.6)){{g=G[i];break}}}}
cap.innerHTML=(g&&t<FIM)?g.p.map(p=>'<span class="'+(t>=p.s?'on':'')+'">'+p.w+'</span>').join(' '):'';}}</script></body></html>"""
async def frames(h,dur,fr):
    async with async_playwright() as pw:
        b=await pw.chromium.launch();pg=await b.new_page(viewport={'width':1080,'height':1920})
        f=R/'_nar.html';f.write_text(h);await pg.goto(f.resolve().as_uri());await pg.wait_for_timeout(500)
        for i in range(int(dur*FPS)):
            await pg.evaluate(f'setT({i/FPS})');await pg.screenshot(path=str(fr/f'{i:05d}.jpg'),type='jpeg',quality=92)
        await b.close()
def fazer(nome,tema,voz,cenas_def,fim_extra=3.4):
    W=palavras(M/f'{voz}.json'); mp3=str(M/f'{voz}.mp3')
    adur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',mp3]))
    cenas=[]
    for c in cenas_def:
        t=c['t'] if isinstance(c['t'],(int,float)) else achar(W,c['t'])-0.15
        cenas.append({'t':max(0,t),'html':c['html'],'sfx':c.get('sfx','whoosh_entrada'),'n':c['html'].count('class=st')})
    dur=adur+fim_extra
    fr=R/'_frn'; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
    asyncio.run(frames(html(TEMAS[tema],cenas,W,dur),dur,fr))
    out=R/'out'/nome; out.mkdir(parents=True,exist_ok=True); v=str(out/'_v.mp4')
    subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(fr/'%05d.jpg'),'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',v],check=True); shutil.rmtree(fr)
    ev=[]
    for i,c in enumerate(cenas):
        ev.append((c['sfx'],c['t'],.4))
        for j in range(c['n']): ev.append((('pop_card','nota_vidro')[j%2],c['t']+0.4+0.45*j,.45))
    ev.append(('chime_cta',cenas[-1]['t']+0.9,.55))
    a=['ffmpeg','-v','error','-y','-i',v,'-i',mp3]
    for n,_,_ in ev: a+=['-i',SFX+n+'.mp3']
    f=['[1:a]volume=1.0[vz]']+[f'[{j+2}:a]adelay={int(t*1000)}|{int(t*1000)},volume={vol}[a{j}]' for j,(n,t,vol) in enumerate(ev)]
    f.append('[vz]'+''.join(f'[a{j}]' for j in range(len(ev)))+f'amix=inputs={len(ev)+1}:normalize=0,apad,atrim=0:{dur}[o]')
    final=str(out/f'Reel_{nome}.mp4')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',final]
    subprocess.run(a,check=True); print('ok',final,dur); return final

def fazer_story(nome,tema,corpo,dur=8.0):
    cenas=[{'t':0,'html':corpo,'n':corpo.count('class=st')}]
    fr=R/f'_frs_{nome}'; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
    asyncio.run(frames(html(TEMAS[tema],cenas,[],dur),dur,fr))
    out=R/'out'/'stories'; out.mkdir(parents=True,exist_ok=True); v=str(out/f'_{nome}.mp4')
    subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(fr/'%05d.jpg'),'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',v],check=True); shutil.rmtree(fr)
    ev=[('impacto_titulo',0.05,.45)]+[(('pop_card','nota_vidro')[j%2],0.4+0.45*j,.45) for j in range(cenas[0]['n'])]+[('chime_cta',2.6,.5)]
    a=['ffmpeg','-v','error','-y','-i',v]
    for n,_,_ in ev: a+=['-i',SFX+n+'.mp3']
    f=[f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={vol}[a{j}]' for j,(n,t,vol) in enumerate(ev)]
    f.append(''.join(f'[a{j}]' for j in range(len(ev)))+f'amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{dur}[o]')
    final=str(out/f'Story_{nome}.mp4')
    a+=['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','160k','-movflags','+faststart',final]
    subprocess.run(a,check=True); print('ok',final); return final
