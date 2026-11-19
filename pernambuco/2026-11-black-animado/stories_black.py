#!/usr/bin/env python3
# Stories animados da Black Week (23–30/11): 9:16, 8 s, padrão branco aprovado, palavras em degradê e efeitos sonoros (sem música)
import os, sys, asyncio, subprocess, shutil
B = '/home/claude/v2/'; M = B + 'motion/'; SFX = '/home/claude/dedikar-midia/sfx/'
src = open(M + 'reel_black.py').read()
exec(src.split("LOGO = ")[0])          # css, a(), words(), chip(), script(), sub(), fotoc()
K = 1.0; DUR = 8.0
OUT = '/home/claude/entrega/stories_black/'; os.makedirs(OUT, exist_ok=True)

def big(txt, t):
    return f"<div class='gd' style='font-weight:900;font-size:330px;letter-spacing:-12px;line-height:.9;animation:{a('zoomin',.6,t)}, shine 6s linear 0s infinite'>{txt}</div>"
def l1(txt, t, s=84):
    return f"<div style='font-weight:800;font-size:{s}px;color:{VE};line-height:1.05;animation:{a('up',.5,t)}'>{txt}</div>"
CTA = f"""<div class='cen' style='top:1335px;z-index:4'>
 <div style='display:inline-block;animation:{a('pop',.5,2.4)}, {a('pulse',1,3.0,'none','ease-in-out',4)}'>
  <div class='cta' style='height:112px;padding:0 40px 0 18px;gap:20px'>
   <div class='w' style='width:84px;height:84px'>{ico('wa',VE,52)}</div>
   <div class='tx' style='text-align:left'><small>Reserve pelo WhatsApp</small><strong style='font-size:48px'>{WPP}</strong></div></div></div>
 <div style='font-weight:700;font-size:32px;color:{AZ};margin-top:16px;animation:{a('up',.5,2.7)}'>{SITE} · link na bio</div></div>"""
FAIXA = f"""<div class='abs' style='left:0;bottom:0;width:{W}px;height:200px;animation:{a('slide',.8,.2,'both','cubic-bezier(.2,.8,.2,1)')}'>
<svg width='{W}' height='200' viewBox='0 0 {W} 200'><path d='M0 90 C300 40 700 60 1080 110 L1080 200 L0 200Z' fill='{VD}'/>
<path d='M0 125 C320 80 720 95 1080 140 L1080 160 C700 118 320 105 0 150Z' fill='{AM}'/><path d='M0 158 C330 120 730 130 1080 170 L1080 200 L0 200 L0 175Z' fill='{VM}'/></svg></div>"""
LOGO = f"""<div class='cen' style='top:200px;animation:{a('fade',.6,0)}'><img src='file://{B}logo.png' style='width:520px'>
 <div style='font-weight:600;font-size:20px;letter-spacing:8px;color:{VE};margin-top:8px'>MOBILIDADE EM TODO CAMINHO</div></div>"""

def story(nome, chip_txt, chip_cor, foto, l1_txt='', palavras='', psize=150, scr='', scls='gw', sub_txt='', grande=''):
    corpo = []
    if l1_txt: corpo.append(l1(l1_txt, .55))
    if grande: corpo.append(big(grande, .85))
    if palavras: corpo.append(f"<div style='line-height:1;font-weight:900;letter-spacing:-4px;margin-top:6px'>{words(palavras,.8,'gd',psize,.15)}</div>")
    if scr: corpo.append(script(scr, 1.3, 96 if len(scr) < 14 else 76, scls))
    if sub_txt: corpo.append(f"<div class='sub' style='font-size:40px;margin:24px 70px 0;animation:{a('up',.5,1.7)}'>{sub_txt}</div>")
    html_corpo = (LOGO + fotoc(foto, 0, 8.6) + f"<div class='cen' style='top:440px'>{chip(chip_txt,.3,chip_cor)}<div style='margin-top:26px'>{''.join(corpo)}</div></div>"
                  + "<div class='abs' style='left:0;top:1260px;width:1080px;height:420px;background:linear-gradient(to bottom,rgba(255,255,255,0),rgba(255,255,255,.85) 35%,rgba(255,255,255,.85) 75%,rgba(255,255,255,0));z-index:3'></div>"
                  + CTA + FAIXA)
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div class='c' style='width:{W}px;height:{H}px'>{html_corpo}</div></body></html>"
    fn = M + f'_st_{nome}.html'; open(fn, 'w').write(html); return fn

async def frames(fn, fr):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get('CHROME') or None, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = await br.new_page(viewport={'width': W, 'height': H})
        await pg.goto('file://' + fn); await pg.wait_for_timeout(500)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(int(DUR*FPS)):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/FPS})")
            await pg.screenshot(path=f'{fr}/{i:04d}.jpg', type='jpeg', quality=92)
        await br.close()

EV = [('entrada_reveal',0.05,.5),('pop_card',.3,.42),('impacto_titulo',.85,.45),('nota_vidro',1.35,.35),('meio_bolha',1.75,.3),('chime_cta',2.45,.55)]
def video(nome, fn):
    fr = M + '_fs_' + nome; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    asyncio.run(frames(fn, fr))
    a_ = ['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',fr+'/%04d.jpg']
    for n,_,_ in EV: a_ += ['-i', SFX+n+'.mp3']
    f = [f'[{j+1}:a]adelay={int(t*1000)}|{int(t*1000)},volume={v}[a{j}]' for j,(n,t,v) in enumerate(EV)]
    f.append(''.join(f'[a{j}]' for j in range(len(EV))) + f'amix=inputs={len(EV)}:normalize=0,apad,atrim=0:{DUR},afade=t=out:st=7.4:d=0.6[o]')
    a_ += ['-filter_complex',';'.join(f),'-map','0:v','-map','[o]','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-t',str(DUR),'-movflags','+faststart',OUT+nome+'.mp4']
    subprocess.run(a_, check=True); shutil.rmtree(fr); print('ok', nome)

S = {
 'stbw_23_09': dict(chip_txt='BLACK <em>WEEK</em>', chip_cor=VE, foto='banner_suv', l1_txt='Começou a', palavras='Black Week', psize=170, scr='Pernambuco', sub_txt='Condutor adicional e lavagem grátis nas reservas até 30/11.'),
 'stbw_23_19': dict(chip_txt='PRESENTE 2', chip_cor=VD, foto='carros', palavras='Lavagem', psize=190, scr='grátis!', sub_txt='Em locações a partir de 4 diárias.'),
 'stbw_24_09': dict(chip_txt='ENQUETE', chip_cor=AZ, foto='praia', l1_txt='Pra onde você vai', palavras='nessa Black?', psize=150, scr='vote aqui', sub_txt='Porto de Galinhas ou Carneiros?'),
 'stbw_24_19': dict(chip_txt='DICA DA BLACK', chip_cor=VE, foto='suv_olinda', l1_txt='Reserve agora,', palavras='retire quando quiser', psize=118, scr='até no verão', sub_txt='Reservando até 30/11, a retirada pode ser em qualquer data.'),
 'stbw_25_09': dict(chip_txt='PRESENTE 1', chip_cor=AZ, foto='familia', palavras='Condutor adicional', psize=140, scr='grátis!', sub_txt='Em todas as reservas até 30/11.'),
 'stbw_25_12': dict(chip_txt='TIRE SUA DÚVIDA', chip_cor=VD, foto='atendimento', l1_txt='Dúvida sobre', palavras='a Black?', psize=170, scr='pergunta aqui', sub_txt='A gente responde nos stories.'),
 'stbw_26_09': dict(chip_txt='VOCÊ SABIA?', chip_cor=AZ, foto='carros', l1_txt='Reservou até 30/11?', palavras='Retire em janeiro', psize=128, scr='pode sim!', sub_txt='A retirada pode ser na data que você quiser.'),
 'stbw_26_12': dict(chip_txt='CHEGOU EM RECIFE?', chip_cor=VE, foto='aeroporto', l1_txt='Retirada em Boa Viagem,', palavras='perto do aeroporto', psize=124, scr='e pé na estrada', sub_txt='Condutor adicional grátis nas reservas até 30/11.'),
 'stbw_26_19': dict(chip_txt='DESTINO', chip_cor=VD, foto='praia', palavras='Porto de Galinhas', psize=130, scr='revezando o volante', sub_txt='Condutor adicional grátis nas reservas até 30/11.'),
 'stbw_27_09': dict(chip_txt='BLACK <em>FRIDAY</em>', chip_cor=VE, foto='banner_suv', l1_txt='É hoje! Faltam', grande='3', scr='dias para acabar', sub_txt='Benefícios válidos para reservas até 30/11.'),
 'stbw_27_19': dict(chip_txt='BLACK <em>FRIDAY</em>', chip_cor=VE, foto='suv_olinda', l1_txt='Hoje é', palavras='Black Friday', psize=165, scr='chama no WhatsApp', sub_txt='Condutor adicional grátis + lavagem grátis a partir de 4 diárias.'),
 'stbw_28_09': dict(chip_txt='CONTAGEM', chip_cor=VM, foto='familia', l1_txt='Faltam', grande='2', scr='dias', sub_txt='Black Pernambuco: reservas até 30/11.'),
 'stbw_28_12': dict(chip_txt='DESTINO', chip_cor=VD, foto='familia', palavras='Carneiros', psize=180, scr='com a família toda', sub_txt='Lavagem grátis em locações a partir de 4 diárias.'),
 'stbw_28_19': dict(chip_txt='RESERVA ONLINE', chip_cor=AZ, foto='celular', l1_txt='Reserve', palavras='pelo site', psize=170, scr='em poucos minutos', sub_txt='Escolha local e datas, o carro, e pague no Pix ou cartão.'),
 'stbw_29_09': dict(chip_txt='CONTAGEM', chip_cor=VM, foto='suv_olinda', l1_txt='Falta', grande='1', scr='dia', sub_txt='Amanhã é o último dia da Black.'),
 'stbw_29_12': dict(chip_txt='RESUMO DA BLACK', chip_cor=VE, foto='banner_suv', l1_txt='Os 2 presentes', palavras='da Black', psize=170, scr='só até amanhã', sub_txt='Condutor adicional grátis + lavagem grátis a partir de 4 diárias.'),
 'stbw_30_09': dict(chip_txt='ÚLTIMO DIA', chip_cor=VM, foto='praia', l1_txt='Hoje é o', palavras='último dia', psize=165, scr='da Black Pernambuco', sub_txt='Reserve hoje e retire na data que quiser.'),
 'stbw_30_12': dict(chip_txt='ÚLTIMAS HORAS', chip_cor=VM, foto='familia', l1_txt='Acaba', palavras='hoje!', psize=200, scr='corre pro WhatsApp', sub_txt='Condutor adicional e lavagem grátis só até hoje.'),
 'stbw_30_19': dict(chip_txt='ÚLTIMA CHAMADA', chip_cor=VM, foto='banner_suv', l1_txt='Últimas horas', palavras='da Black', psize=170, scr='reserve agora', sub_txt='Pelo site ou WhatsApp, com retirada em qualquer data.'),
}
if __name__ == '__main__':
    for nome in (sys.argv[1:] or list(S)):
        video(nome, story(nome, **S[nome]))
