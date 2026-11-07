"""Tema @ottogurgel.ofc (azul, Poppins) com a mesma API do base.py."""
from base import render, F, ff, CHECK
P=F/'poppins/package/files'
FONTS='\n'.join([ff('Poppins',P/f'poppins-latin-{w}-normal.woff2',w) for w in (400,600,700,800)])
CSS=FONTS+"""
*{margin:0;padding:0;box-sizing:border-box}
body{font-variant-numeric:lining-nums;width:1080px;height:1350px;background:radial-gradient(ellipse 900px 700px at 85% 15%,#0a3aa8 0%,rgba(10,58,168,0) 70%),radial-gradient(ellipse 800px 700px at 0% 100%,#06307e 0%,rgba(6,48,126,0) 70%),#020a2c;color:#fff;font-family:'Poppins';overflow:hidden;position:relative}
canvas{position:absolute;inset:0}
.glow{position:absolute;border-radius:50%;filter:blur(110px)}
.top{position:absolute;left:84px;right:84px;top:80px;display:flex;justify-content:space-between;align-items:center}
.br{display:flex;align-items:center;gap:18px;font:400 30px 'Poppins';letter-spacing:9px}
.cnt{font:500 26px 'Poppins';color:#cfd8ff}.tag{font:700 22px 'Poppins';letter-spacing:3px;color:#4fc3f7;text-transform:uppercase}
.main{position:absolute;left:84px;right:84px;top:190px;bottom:170px;display:flex;flex-direction:column;justify-content:center;gap:32px}
.k{font:700 24px 'Poppins';letter-spacing:4px;color:#4fc3f7;text-transform:uppercase}
h1{font:800 92px/1.04 'Poppins';text-transform:uppercase;letter-spacing:-1px}
h2{font:700 78px/1.1 'Poppins';letter-spacing:-1px}
h1 i,h2 i,.g{font-style:normal;background:linear-gradient(100deg,#4fc3f7 0%,#2f8cff 45%,#8fb8ff 70%,#4fc3f7 100%);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
.bar{width:140px;height:7px;border-radius:4px;background:#29a8f0}
p{font:400 38px/1.42 'Poppins';color:#d5ddf5}p b{color:#fff;font-weight:700}
.card{display:flex;align-items:center;gap:24px;background:rgba(8,24,80,.72);border:1px solid rgba(120,170,255,.22);border-radius:22px;padding:26px 30px}
.n{width:56px;height:56px;flex-shrink:0;border-radius:50%;background:#29a8f0;color:#020a2c;font:800 28px 'Poppins';display:flex;align-items:center;justify-content:center}
.ck{width:56px;height:56px;flex-shrink:0;border-radius:50%;background:#29a8f0;display:flex;align-items:center;justify-content:center}
.card b{display:block;font:700 37px/1.22 'Poppins'}.card small{display:block;font:400 28px/1.3 'Poppins';color:#b9c6ee;margin-top:4px}
.big{border:2.5px solid #29a8f0;border-radius:26px;padding:34px 36px;background:rgba(8,24,80,.6);box-shadow:0 0 70px rgba(41,168,240,.25)}
.big .v{font:800 160px/1 'Poppins'}.big .l{font:400 34px 'Poppins';color:#d5ddf5;margin-top:8px}
.ph{width:300px;height:360px;border-radius:26px;padding:5px;background:linear-gradient(135deg,#4fc3f7,#2f8cff);box-shadow:0 0 60px rgba(41,168,240,.5)}
.ph img{width:100%;height:100%;border-radius:22px;object-fit:cover;object-position:50% 20%}
.pill{display:inline-flex;align-items:center;gap:22px;background:#29a8f0;color:#020a2c;border-radius:80px;padding:28px 50px;font:800 52px 'Poppins';letter-spacing:2px;box-shadow:0 0 70px rgba(41,168,240,.55);align-self:flex-start}
.note{font:400 24px 'Poppins';color:#9fb0e0}
.quote{font:800 150px/0.6 'Poppins';color:#29a8f0}
.foot{position:absolute;left:84px;right:84px;bottom:76px;padding-top:24px;border-top:1px solid rgba(160,190,255,.2);display:flex;justify-content:space-between;align-items:center;font:700 28px 'Poppins'}.foot span:last-child{color:#4fc3f7}
.sig{display:flex;align-items:center;gap:16px}.sig img{width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:50% 20%;border:2px solid #4fc3f7}.sig small{display:block;font:400 22px 'Poppins';color:#b9c6ee}
"""
LOGO='<svg width="78" height="62" viewBox="0 0 78 62" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="26" cy="26" r="22"/><path d="M73 30a22 22 0 1 1-6-15"/><path d="M73 36h-14"/></svg>'
def bg(seed):
    return f"""<canvas id=c></canvas><script>const c=document.getElementById('c');c.width=1080;c.height=1350;const x=c.getContext('2d');let s={seed};const r=()=>{{s=(s*16807)%2147483647;return s/2147483647}};
const p=[];for(let i=0;i<85;i++)p.push([r()*1080,r()*1350]);x.lineWidth=1.2;
for(const a of p)for(const b of p){{const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<190){{x.strokeStyle='rgba(80,150,255,'+(.28*(1-d/190))+')';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}}}
for(const a of p){{x.shadowColor='#4fa8ff';x.shadowBlur=12;x.fillStyle='rgba(140,200,255,.85)';x.beginPath();x.arc(a[0],a[1],2.8,0,7);x.fill()}}x.shadowBlur=0;</script>"""
def num(i,b,s=''): return f'<div class=card><div class=n>{i}</div><div><b>{b}</b>{f"<small>{s}</small>" if s else ""}</div></div>'
def chk(b,s=''): return f'<div class=card><div class=ck>{CHECK}</div><div><b>{b}</b>{f"<small>{s}</small>" if s else ""}</div></div>'
SIG_T='<div class=sig><img src="fotos/{f}.jpg"><div>Otto Gurgel<small>@ottogurgel.ofc</small></div></div>'
SIGFOTO="otto_14_polo_azul_claro"
def slide(i,tot,body,foot=None,capa=False,tag=''):
    right=f'<div class=tag>{tag}</div>' if tag else (f'<div class=cnt>{i}/{tot}</div>' if tot>1 else '')
    foot=foot or ('<span>@ottogurgel.ofc</span><span>Arraste →</span>' if tot>1 else SIG_T.format(f=SIGFOTO)+'<span>Envie para seu time ↗</span>')
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body data-tema=og>{bg(23+i*71)}
<div class=top><div class=br>{LOGO}OTTO GURGEL</div>{right}</div>
<div class=main>{body}</div><div class=foot>{foot}</div></body></html>"""
