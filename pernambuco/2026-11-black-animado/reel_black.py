#!/usr/bin/env python3
# Reel animado Black Week (padrão branco aprovado + palavras em degradê + trilha própria)
import os, sys, asyncio, subprocess
B = '/home/claude/v2/'; F = B + 'fotos/'; M = B + 'motion/'
src = open(B + 'gen2.py').read()
exec(src.split('\nP = {}\n')[0])            # cores, fontes, CSS, ícones, faixas, logo
K = 1.4   # alonga o tempo de leitura de cada cena (15 s -> 21 s)
FPS, DUR, W, H = 30, 15.0*K, 1080, 1920
VE, VD, AZ, AM, VM = '#0E5A2C', '#2E9E3E', '#1747A6', '#F5C400', '#E1251B'

css = CSS + f"""
.gd{{background:linear-gradient(100deg,{VE} 0%,{VD} 35%,{AZ} 70%,{VE} 100%);background-size:220% 100%;-webkit-background-clip:text;color:transparent;animation:shine 6s linear 0s infinite}}
.gw{{background:linear-gradient(100deg,{AM} 0%,#F08A00 45%,{VM} 90%);background-size:200% 100%;-webkit-background-clip:text;color:transparent;animation:shine 4s linear 0s infinite}}
.cen{{position:absolute;left:0;width:{W}px;text-align:center}}
.w{{display:inline-block}}
@keyframes shine{{from{{background-position:0% 0}}to{{background-position:220% 0}}}}
@keyframes up{{from{{opacity:0;transform:translateY(70px) scale(.92);filter:blur(10px)}}to{{opacity:1;transform:none;filter:none}}}}
@keyframes pop{{0%{{opacity:0;transform:scale(.3)}}70%{{opacity:1;transform:scale(1.12)}}100%{{opacity:1;transform:scale(1)}}}}
@keyframes out{{to{{opacity:0;transform:translateY(-60px);filter:blur(8px)}}}}
@keyframes draw{{from{{clip-path:inset(0 100% 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes fadeout{{to{{opacity:0}}}}
@keyframes kb{{from{{transform:scale(1.02) translateX(0)}}to{{transform:scale(1.16) translateX(-30px)}}}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.06)}}}}
@keyframes slide{{from{{transform:translateX(-110%)}}to{{transform:none}}}}
@keyframes zoomin{{from{{opacity:0;transform:scale(2.4);filter:blur(14px)}}to{{opacity:1;transform:none;filter:none}}}}
"""
E = 'cubic-bezier(.2,.9,.25,1.15)'
def a(name, dur, delay, fill='both', ease=E, it=1):
    return f"{name} {dur}s {ease} {delay*K:.2f}s {it} normal {fill}"
def cena(t0, t1, html):   # entra junto com os filhos e some em t1
    return f"<div class='abs' style='inset:0;animation:{a('out',.35,t1,'forwards','ease-in')}'>{html}</div>"
def words(txt, t, cls, size, step=.12, extra=''):
    out = []
    for i, w in enumerate(txt.split()):
        out.append(f"<span class='w {cls}' style='font-size:{size}px;margin:0 .12em;animation:{a('up',.55,t+i*step)}, shine 6s linear 0s infinite;{extra}'>{w}</span>")
    return ''.join(out)
def chip(txt, t, cor=VE):
    return f"<div style='display:inline-block;animation:{a('pop',.45,t)}'><span class='selo' style='font-size:30px;background:{cor}'>{txt}</span></div>"
def script(txt, t, size=110, cls='gw'):
    return (f"<div style='animation:{a('up',.5,t)}'><span class='sc {cls}' style='font-size:{size}px;display:inline-block;transform:rotate(-4deg);padding:0 20px'>{txt}</span></div>"
            f"<div style='margin:-6px auto 0;width:{int(size*3.2)}px;height:12px;border-radius:12px;background:{AM};transform:rotate(-2deg);animation:{a('draw',.5,t+.35,'both','ease-out')}'></div>")
def sub(txt, t, size=44):
    return f"<div class='sub' style='font-size:{size}px;margin-top:26px;animation:{a('up',.5,t)}'>{txt}</div>"
def fotoc(nome, t0, t1, pos='center'):
    return (f"<div class='abs' style='left:0;top:1040px;width:{W}px;height:880px;overflow:hidden;animation:{a('fade',.5,t0,'both','ease')}, {a('fadeout',.4,t1,'forwards','ease')};"
            f"-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 22%)'>"
            f"<div style='width:100%;height:100%;background:url(file://{F}{nome}.jpg) {pos}/cover;animation:{a('kb',(t1-t0)*K+.6,t0,'both','linear')}'></div></div>")

LOGO = f"<img src='file://{B}logo.png' style='width:600px'>"
corpo = f"""
<div class='cen' style='top:80px;animation:{a('fade',.6,0)}'>{LOGO}
 <div style='font-weight:600;font-size:22px;letter-spacing:8px;color:{VE};margin-top:10px'>MOBILIDADE EM TODO CAMINHO</div></div>
{fotoc('banner_suv',0,3.1)}{fotoc('familia',3.1,6.3)}{fotoc('carros',6.3,9.5,'center 40%')}{fotoc('praia',9.5,12.2)}{fotoc('aeroporto',12.2,15.4)}

{cena(0,2.85, f"<div class='cen' style='top:350px'>{chip('BLACK <em>WEEK</em>',.3)}"
   f"<div style='margin-top:30px;line-height:.95;font-weight:900;letter-spacing:-4px'>{words('Black Week',.55,'gd',185)}</div>"
   f"<div style='line-height:1;font-weight:900;letter-spacing:-3px'>{words('Pernambuco',.85,'gd',140)}</div>"
   f"{script('dois presentes pra você',1.35,96,'gw')}</div>")}

{cena(3.1,6.05, f"<div class='cen' style='top:350px'>{chip('PRESENTE 1',3.2,AZ)}"
   f"<div style='margin-top:30px;line-height:1;font-weight:900;letter-spacing:-4px'>{words('Condutor adicional',3.4,'gd',140,.18)}</div>"
   f"{script('grátis!',3.95,165)}{sub('Em todas as reservas até 30/11.',4.4)}</div>")}

{cena(6.3,9.25, f"<div class='cen' style='top:350px'>{chip('PRESENTE 2',6.4,VD)}"
   f"<div style='margin-top:30px;line-height:1;font-weight:900;letter-spacing:-4px'>{words('Lavagem',6.6,'gd',180)}</div>"
   f"{script('grátis!',7.05,165)}{sub('Em locações a partir de 4 diárias.',7.5)}</div>")}

{cena(9.5,11.95, f"<div class='cen' style='top:350px'>{chip('ÚLTIMOS DIAS',9.6,VM)}"
   f"<div style='margin-top:20px;font-weight:800;font-size:90px;color:{VE};animation:{a('up',.5,9.8)}'>Só até</div>"
   f"<div class='gd' style='font-weight:900;font-size:300px;letter-spacing:-12px;line-height:.9;animation:{a('zoomin',.6,10.05)}, shine 6s linear 0s infinite'>30/11</div>"
   f"{script('retire quando quiser',10.6,92,'gd')}</div>")}

<div class='cen' style='top:350px'>
 <div style='font-weight:800;font-size:84px;color:{VE};line-height:1.05;animation:{a('up',.5,12.3)}'>Reserve agora</div>
 <div style='line-height:1;font-weight:900;letter-spacing:-3px'>{words('pelo site ou WhatsApp',12.5,'gd',100,.12)}</div>
 <div style='display:inline-block;margin-top:46px;animation:{a('pop',.5,13.1)}, {a('pulse',1,13.6,'none','ease-in-out',3)}'>
  <div class='cta' style='height:130px;padding:0 44px 0 22px;gap:22px;width:auto'>
   <div class='w' style='width:96px;height:96px'>{ico('wa',VE,60)}</div>
   <div class='tx' style='text-align:left'><small>Chama no WhatsApp</small><strong style='font-size:54px'>{WPP}</strong></div></div></div>
 <div style='font-weight:700;font-size:38px;color:{AZ};margin-top:26px;animation:{a('up',.5,13.4)}'>{SITE}</div>
</div>

<div class='abs' style='left:0;bottom:0;width:{W}px;height:200px;animation:{a('slide',.8,.2,'both','cubic-bezier(.2,.8,.2,1)')}'>
<svg width='{W}' height='200' viewBox='0 0 {W} 200'>
 <path d='M0 90 C300 40 700 60 1080 110 L1080 200 L0 200Z' fill='{VD}'/>
 <path d='M0 125 C320 80 720 95 1080 140 L1080 160 C700 118 320 105 0 150Z' fill='{AM}'/>
 <path d='M0 158 C330 120 730 130 1080 170 L1080 200 L0 200 L0 175Z' fill='{VM}'/></svg></div>
<div class='abs legal' style='left:60px;right:60px;bottom:12px;text-align:center;color:#fff;font-size:17px;z-index:3'>Reservas até 30/11/2026 pelo site ou WhatsApp, retirada em qualquer data. Lavagem a partir de 4 diárias. Sujeito à disponibilidade.</div>
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div class='c' style='width:{W}px;height:{H}px'>{corpo}</div></body></html>"
fn = M + 'reel_black.html'; open(fn, 'w').write(html)
FR = M + 'frames/'; os.makedirs(FR, exist_ok=True)

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get('CHROME') or None, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = await br.new_page(viewport={'width': W, 'height': H})
        await pg.goto('file://' + fn); await pg.wait_for_timeout(600)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        n = int(FPS * DUR)
        only = [int(x) for x in sys.argv[1:]]
        for i in (only or range(n)):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/FPS})")
            await pg.screenshot(path=f'{FR}f{i:04d}.jpg', type='jpeg', quality=93)
        await br.close()
asyncio.run(main())
print('frames ok')
