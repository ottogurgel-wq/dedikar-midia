#!/usr/bin/env python3
# Anima os posts de feed já aprovados (mesmo HTML do gen2) e mistura os efeitos sonoros da Dedikar (sem música: música entra no Instagram)
import os, sys, asyncio, subprocess, shutil
B = '/home/claude/v2/'; M = B + 'motion/'; SFX = '/home/claude/dedikar-midia/sfx/'
FPS, D = 30, 11.0
JS = """
const VE='#0E5A2C',VD='#2E9E3E',AZ='#1747A6';
const c=document.querySelector('.c');const kids=[...c.children];const E='cubic-bezier(.2,.9,.25,1.15)';
function A(el,kf,dur,delay,o={}){if(!el)return;el.animate(kf,Object.assign({duration:dur*1000,delay:delay*1000,fill:'both',easing:E},o));}
const up=[{opacity:0,transform:'translateY(60px)',filter:'blur(8px)'},{opacity:1,transform:'none',filter:'blur(0)'}];
const pop=[{opacity:0,transform:'scale(.3)'},{opacity:1,transform:'scale(1.12)',offset:.7},{opacity:1,transform:'scale(1)'}];
const foto=c.querySelector('.foto');A(foto,[{opacity:0},{opacity:1}],.7,.3,{easing:'ease'});
foto.style.transformOrigin='60% 100%';A(foto,[{transform:'scale(1)'},{transform:'scale(1.08)'}],DUR,0,{easing:'linear',composite:'add'});
const svgs=kids.filter(k=>k.tagName.toLowerCase()=='svg');const canto=svgs[0],fx=svgs[svgs.length-1];
A(canto,[{transform:'translate(380px,-260px)'},{transform:'none'}],.8,.15,{easing:'cubic-bezier(.2,.8,.2,1)'});
A(canto.nextElementSibling,[{opacity:0,transform:'translateX(40px)'},{opacity:1,transform:'none'}],.6,.7);
A(fx,[{transform:'translate(560px,240px)'},{transform:'none'}],.9,.2,{easing:'cubic-bezier(.2,.8,.2,1)'});
const logo=c.querySelector('img').parentElement;A(logo,[{opacity:0,transform:'translateY(-40px)'},{opacity:1,transform:'none'}],.6,.1);
const selo=c.querySelector('.selo');if(selo){selo.style.display='inline-block';A(selo,pop,.5,.55);}
const t1=c.querySelector('.t1');A(t1,up,.6,.75);
const t2=c.querySelector('.t2');const ws=t2.textContent.trim().split(/\\s+/);
t2.innerHTML=ws.map(w=>'<span class=gw style="display:inline-block;margin-right:.18em">'+w+'</span>').join('');
[...t2.querySelectorAll('.gw')].forEach((s,i)=>{s.style.cssText+=';background:linear-gradient(100deg,'+AZ+' 0%,'+VD+' 45%,'+AZ+' 90%);background-size:250% 100%;-webkit-background-clip:text;color:transparent';
 A(s,up,.6,.95+i*.16);A(s,[{backgroundPosition:'0% 0'},{backgroundPosition:'-250% 0'}],4,0,{easing:'linear',iterations:Infinity,fill:'none'});});
const sc=c.querySelector('.sc');A(sc,up,.55,1.35);
const br=sc&&sc.nextElementSibling;A(br,[{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0 0 0)'}],.5,1.75,{easing:'ease-out'});
A(c.querySelector('.sub'),up,.55,1.95);
[...c.querySelectorAll('.bl')].forEach((b,i)=>{A(b,[{opacity:0,transform:'translateX(-70px)'},{opacity:1,transform:'none'}],.5,2.3+i*.25);A(b.querySelector('.ci'),pop,.45,2.38+i*.25);});
const cta=c.querySelector('.cta');A(cta,pop,.55,3.5);A(cta,[{transform:'scale(1)'},{transform:'scale(1.05)'},{transform:'scale(1)'}],1.1,4.2,{easing:'ease-in-out',iterations:5,fill:'none',composite:'add'});
[...c.querySelectorAll('.ct > div')].forEach((d,i)=>A(d,[{opacity:0,transform:'translateY(20px)'},{opacity:1,transform:'none'}],.45,3.75+i*.14));
A(c.querySelector('.legal'),[{opacity:0},{opacity:1}],.6,4.3,{easing:'ease'});
"""
EV = [('entrada_reveal',0.05,.5),('meio_swish',0.7,.35),('pop_card',.55,.4),('impacto_titulo',.95,.45),('nota_vidro',1.4,.35),
      ('pop_card',2.35,.38),('meio_bolha',2.6,.35),('pop_card',2.85,.38),('meio_bolha',3.1,.35),('riser_suave',2.4,.25),('chime_cta',3.6,.55)]
async def frames(nome, fr):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get('CHROME') or None, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = await br.new_page(viewport={'width': 1080, 'height': 1350})
        await pg.goto('file://' + B + 'html/' + nome + '.html'); await pg.wait_for_timeout(500)
        await pg.evaluate('const DUR=%s;' % D + JS + ';document.getAnimations().forEach(a=>a.pause())')
        for i in range(int(D*FPS)):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/FPS})")
            await pg.screenshot(path=f'{fr}/{i:04d}.jpg', type='jpeg', quality=93)
        await br.close()
def fazer(nome, saida):
    fr = M + '_fr_' + nome; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    asyncio.run(frames(nome, fr))
    v = M + '_v_' + nome + '.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',fr+'/%04d.jpg','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',v], check=True)
    a = ['ffmpeg','-v','error','-y','-i',v]
    for n,_,_ in EV: a += ['-i', SFX+n+'.mp3']
    f = [f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={vol}[a{j}]' for j,(n,t,vol) in enumerate(EV)]
    f.append(''.join(f'[a{j}]' for j in range(len(EV))) + f'amix=inputs={len(EV)}:normalize=0,apad,atrim=0:{D},afade=t=out:st={D-0.6:.1f}:d=0.6[o]')
    a += ['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','copy','-c:a','aac','-b:a','160k','-movflags','+faststart',saida]
    subprocess.run(a, check=True); shutil.rmtree(fr); os.remove(v); print('ok', saida)
if __name__ == '__main__':
    for nome, saida in [a.split('=') for a in sys.argv[1:]]: fazer(nome, saida)
