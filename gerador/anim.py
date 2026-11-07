"""Versão animada do carrossel: cada slide vira MP4 1080x1350 em loop (padrão do site: degradê que corre, entrada em cascata, rede de pontos viva)."""
import asyncio, pathlib, subprocess, re, shutil
from playwright.async_api import async_playwright
DUR=9.0; FPS=30
ANIM_CSS="""
h1 i,h2 i,.g{background-size:250% 100%!important;animation:shine 4.5s linear infinite}
@keyframes shine{to{background-position:-250% 0}}
.ent{animation:up 1.15s cubic-bezier(.2,.8,.2,1) both}
@keyframes up{from{opacity:0;transform:translateY(46px);filter:blur(6px)}}
.ck svg{animation:pop .6s cubic-bezier(.3,1.6,.5,1) both;animation-delay:inherit}
@keyframes pop{from{transform:scale(0)}}
.pill{animation:pulse 2.25s ease-in-out infinite}
.pill.ent{animation:up 1.15s cubic-bezier(.2,.8,.2,1) both,pulse 2.25s ease-in-out 1.2s infinite}
@keyframes pulse{50%{box-shadow:0 0 120px rgba(56,217,236,.85);transform:scale(1.035)}}
.ph{animation:ring 4.5s ease-in-out infinite}
@keyframes ring{50%{box-shadow:0 0 95px rgba(56,217,236,.75)}}
"""
ANIM_JS="""<script>
(function(){
const OG=document.body.dataset.tema==='og';
const cv=document.getElementById('c');cv.width=1080;cv.height=1350;const x=cv.getContext('2d');let s=SEED;const r=()=>{s=(s*16807)%2147483647;return s/2147483647};
const p=[];for(let i=0;i<75;i++)p.push([r()*1080,r()*1350,r()*6.28,10+r()*22,r()>.5]);
window.drawBG=function(t){x.clearRect(0,0,1080,1350);const w=2*Math.PI*t/DUR;
 const q=p.map(a=>[a[0]+Math.cos(w+a[2])*a[3],a[1]+Math.sin(w+a[2])*a[3],a[4]]);x.lineWidth=1;
 for(const a of q)for(const b of q){const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<180){x.strokeStyle=OG?'rgba(80,150,255,'+(.28*(1-d/180))+')':'rgba(56,217,236,'+(.16*(1-d/180))+')';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}
 for(const a of q){if(OG){x.shadowColor='#4fa8ff';x.shadowBlur=12;x.fillStyle='rgba(140,200,255,.85)'}else{x.fillStyle=a[2]?'rgba(56,217,236,.6)':'rgba(122,162,255,.5)'};x.beginPath();x.arc(a[0],a[1],2.6,0,7);x.fill()}x.shadowBlur=0;
 if(!OG){x.fillStyle='rgba(255,255,255,.03)';for(let i=0;i<1080;i+=36)for(let j=0;j<1350;j+=36)x.fillRect(i,j,2,2);}};
const capa=CAPA;let k=0;
if(!capa){document.querySelectorAll('.main > *').forEach(el=>{
 if(el.querySelector(':scope > .card')){el.querySelectorAll(':scope > .card').forEach(c=>{c.classList.add('ent');c.style.animationDelay=(0.35+0.55*k++)+'s'})}
 else{el.classList.add('ent');const d=0.35+0.55*k++;el.style.animationDelay=el.classList.contains('pill')?(d+'s,'+(d+1)+'s'):(d+'s')}});}
window.eventos=function(){return [...document.querySelectorAll('.ent')].map(e=>({t:parseFloat(e.style.animationDelay),tipo:e.classList.contains('card')?'card':e.classList.contains('pill')?'pill':e.classList.contains('k')?'k':/^H[12]$/.test(e.tagName)?'titulo':e.classList.contains('big')?'big':'outro'}))};
window.setT=function(t){drawBG(t);document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000});
 document.querySelectorAll('[data-count]').forEach(el=>{const v=+el.dataset.count,a=+el.dataset.at||0.8;const f=Math.min(1,Math.max(0,(t-a)/1.6));el.textContent=Math.round(v*(1-Math.pow(1-f,3)))})};
})();</script>"""
def animar(html,capa,seed):
    html=html.replace('</style>',ANIM_CSS+'</style>')
    html=re.sub(r'<script>const c=.*?</script>','',html,flags=re.S)
    html=html.replace('h1 i,h2 i,.g{background-size','h1 i,h2 i,.g{background-size')
    return html.replace('</body>',ANIM_JS.replace('SEED',str(seed)).replace('DUR',str(DUR)).replace('CAPA','true' if capa else 'false')+'</body>')
async def _rec(jobs):
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for h,mp4 in jobs:
            fr=h.parent/('_fr_'+h.stem); shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
            await pg.goto(h.resolve().as_uri()); await pg.wait_for_timeout(500)
            import json; (h.parent/(h.stem+'.ev.json')).write_text(json.dumps(await pg.evaluate('eventos()')))
            for i in range(int(DUR*FPS)):
                await pg.evaluate(f'setT({i/FPS})'); await pg.screenshot(path=str(fr/f'{i:04d}.jpg'),type='jpeg',quality=93)
            subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.jpg'),'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],check=True)
            shutil.rmtree(fr)
        await b.close()
def render_anim(prefix,slides,out,only=None):
    out=pathlib.Path(out); out.mkdir(parents=True,exist_ok=True); jobs=[]
    R=pathlib.Path(__file__).parent
    for i,s in enumerate(slides,1):
        if only and i not in only: continue
        h=R/f'_{prefix}_anim_{i}.html'; h.write_text(animar(s,i==1,11+i*97)); jobs.append((h,out/f'{prefix}_slide_{i}.mp4'))
    asyncio.run(_rec(jobs)); return [str(m) for _,m in jobs]
