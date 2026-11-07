"""Gerador de carrossel @dedikar.ia (1080x1350) · padrão aprovado + palavras em degradê do site."""
import pathlib, asyncio
from playwright.async_api import async_playwright
R = pathlib.Path(__file__).parent
F = R/'fonts'
def ff(n,p,w,s='normal'): return f"@font-face{{font-family:'{n}';src:url('{p}');font-weight:{w};font-style:{s}}}"
CG=F/'fontsource-cormorant-garamond-5.1.0/package/files'; DM=F/'fontsource-dm-sans-5.1.0/package/files'; JB=F/'fontsource-jetbrains-mono-5.1.0/package/files'
FONTS='\n'.join([ff('Cormorant Garamond',CG/'cormorant-garamond-latin-600-normal.woff2',600),ff('Cormorant Garamond',CG/'cormorant-garamond-latin-600-italic.woff2',600,'italic'),
 *[ff('DM Sans',DM/f'dm-sans-latin-{w}-normal.woff2',w) for w in (400,500,600,700)],ff('JetBrains Mono',JB/'jetbrains-mono-latin-500-normal.woff2',500),ff('JetBrains Mono',JB/'jetbrains-mono-latin-700-normal.woff2',700)])
CSS=FONTS+"""
*{margin:0;padding:0;box-sizing:border-box}
body{font-variant-numeric:lining-nums;width:1080px;height:1350px;background:#0b0b10;color:#f6f4ee;font-family:'DM Sans';overflow:hidden;position:relative}
canvas{position:absolute;inset:0}
.glow{position:absolute;border-radius:50%;filter:blur(110px)}
.top{position:absolute;left:80px;right:80px;top:76px;display:flex;justify-content:space-between;align-items:center}
.br{display:flex;align-items:center;gap:18px}.tile{width:58px;height:58px;background:#fff;border-radius:14px;display:flex;align-items:center;justify-content:center}.tile img{width:50px}
.brand{font:600 36px 'Cormorant Garamond'}.brand span{color:#38d9ec}.sub{font:500 13px 'JetBrains Mono';letter-spacing:3px;color:#c9cad2;text-transform:uppercase;margin-top:2px}
.cnt{font:500 24px 'JetBrains Mono';color:#c9cad2;letter-spacing:2px}
.main{position:absolute;left:76px;right:76px;top:170px;bottom:160px;display:flex;flex-direction:column;justify-content:center;gap:30px}
.k{font:500 25px 'JetBrains Mono';letter-spacing:4px;color:#38d9ec;text-transform:uppercase}
h1{font:600 98px/1.02 'Cormorant Garamond';letter-spacing:-1px}
h2{font:600 88px/1.05 'Cormorant Garamond';letter-spacing:-.5px}
h1 i,h2 i,.g{font-style:italic;background:linear-gradient(100deg,#38d9ec 0%,#7aa2ff 45%,#b48cff 70%,#38d9ec 100%);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent;padding-right:.08em}
p{font-size:37px;line-height:1.4;color:#d6d7de}p b{color:#fff}
.card{display:flex;align-items:center;gap:24px;background:rgba(20,22,32,.86);border:1px solid rgba(255,255,255,.10);border-radius:20px;padding:26px 30px}
.n{width:50px;height:50px;flex-shrink:0;border-radius:12px;border:1.5px solid rgba(56,217,236,.6);background:rgba(56,217,236,.10);color:#38d9ec;font:700 24px 'JetBrains Mono';display:flex;align-items:center;justify-content:center}
.ck{width:50px;height:50px;flex-shrink:0;border-radius:50%;background:#38d9ec;display:flex;align-items:center;justify-content:center}
.card b{display:block;font:600 37px/1.2 'DM Sans'}.card small{display:block;font:400 28px/1.3 'DM Sans';color:#a9abb6;margin-top:4px}
.big{border:2.5px solid #38d9ec;border-radius:26px;padding:34px 36px;background:linear-gradient(90deg,rgba(56,217,236,.14),rgba(122,162,255,.05));box-shadow:0 0 70px rgba(56,217,236,.18)}
.big .v{font:600 170px/1 'Cormorant Garamond';font-variant-numeric:lining-nums}.big .l{font:500 34px 'DM Sans';color:#d6d7de;margin-top:8px}
.ph{width:210px;height:210px;border-radius:50%;padding:6px;background:linear-gradient(135deg,#38d9ec,#7aa2ff);box-shadow:0 0 60px rgba(56,217,236,.45)}
.ph img{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 25%;border:5px solid #0b0b10}
.pill{display:inline-flex;align-items:center;gap:22px;background:#38d9ec;color:#0b0b10;border-radius:80px;padding:28px 52px;font:700 70px 'JetBrains Mono';letter-spacing:6px;box-shadow:0 0 70px rgba(56,217,236,.5);align-self:flex-start}
.note{font:500 23px 'JetBrains Mono';color:#8d909c;letter-spacing:1px}
.foot{position:absolute;left:80px;right:80px;bottom:76px;padding-top:24px;border-top:1px solid rgba(255,255,255,.12);display:flex;justify-content:space-between;font:500 24px 'JetBrains Mono';color:#f6f4ee}.foot span:last-child{color:#38d9ec}
"""
def bg(seed):
    return f"""<canvas id=c></canvas>
<div class=glow style="width:620px;height:620px;left:-260px;top:760px;background:rgba(56,217,236,.13)"></div>
<div class=glow style="width:640px;height:640px;right:-300px;top:-240px;background:rgba(56,217,236,.10)"></div>
<script>const c=document.getElementById('c');c.width=1080;c.height=1350;const x=c.getContext('2d');let s={seed};const r=()=>{{s=(s*16807)%2147483647;return s/2147483647}};
const p=[];for(let i=0;i<75;i++)p.push([r()*1080,r()*1350]);x.lineWidth=1;
for(const a of p)for(const b of p){{const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<180){{x.strokeStyle='rgba(56,217,236,'+(.16*(1-d/180))+')';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}}}
for(const a of p){{x.fillStyle=r()>.5?'rgba(56,217,236,.6)':'rgba(122,162,255,.5)';x.beginPath();x.arc(a[0],a[1],2.6,0,7);x.fill()}}
x.fillStyle='rgba(255,255,255,.03)';for(let i=0;i<1080;i+=36)for(let j=0;j<1350;j+=36)x.fillRect(i,j,2,2);</script>"""
CHECK='<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#0b0b10" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def num(i,b,s=''): return f'<div class=card><div class=n>{i}</div><div><b>{b}</b>{f"<small>{s}</small>" if s else ""}</div></div>'
def chk(b,s=''): return f'<div class=card><div class=ck>{CHECK}</div><div><b>{b}</b>{f"<small>{s}</small>" if s else ""}</div></div>'
def slide(i,tot,body,foot=('@dedikar.ia','Arraste →'),capa=False):
    sub='<div class=sub>Sistemas inteligentes para empresas</div>' if capa else ''
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{bg(11+i*97)}
<div class=top><div class=br><div class=tile><img src="logo.png"></div><div><div class=brand>Dedikar <span>IA</span></div>{sub}</div></div><div class=cnt>{i}/{tot}</div></div>
<div class=main>{body}</div><div class=foot><span>{foot[0]}</span><span>{foot[1]}</span></div></body></html>"""
async def _shot(files):
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for h,o in files:
            await pg.goto(h.resolve().as_uri()); await pg.wait_for_timeout(400); await pg.screenshot(path=str(o),type='jpeg',quality=92)
        await b.close()
def render(prefix,slides,out):
    out=pathlib.Path(out); out.mkdir(parents=True,exist_ok=True); files=[]
    for i,s in enumerate(slides,1):
        h=R/f'_{prefix}_{i}.html'; h.write_text(s); files.append((h,out/f'{prefix}_slide_{i}.jpg'))
    asyncio.run(_shot(files)); return [str(o) for _,o in files]
