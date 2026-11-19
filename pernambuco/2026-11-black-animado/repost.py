import os, sys, asyncio, subprocess
B='/home/claude/v2/'; M=B+'motion/'
src=open(B+'gen2.py').read(); exec(src.split('\nP = {}\n')[0])
OUT='/home/claude/entrega/stories_black/'
def bg(txt):
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='c' style='width:1080px;height:1920px;background:linear-gradient(180deg,#fff 0,#eef6f0 100%)'>
<div class='abs' style='left:0;right:0;top:170px;text-align:center'><img src='file://{B}logo.png' style='width:460px'></div>
<div class='abs' style='left:0;right:0;top:300px;text-align:center'><span class='selo' style='font-size:30px'>{txt}</span></div>
<div class='abs' style='left:0;right:0;top:1570px;text-align:center;font-weight:800;font-size:40px;color:{AZ}'>Reserve pelo WhatsApp <span style='color:{VE}'>{WPP}</span></div>
<svg class='abs' style='left:0;bottom:0' width='1080' height='200' viewBox='0 0 1080 200'><path d='M0 90 C300 40 700 60 1080 110 L1080 200 L0 200Z' fill='{VD}'/>
<path d='M0 125 C320 80 720 95 1080 140 L1080 160 C700 118 320 105 0 150Z' fill='{AM}'/><path d='M0 158 C330 120 730 130 1080 170 L1080 200 L0 200 L0 175Z' fill='{VM}'/></svg></div></body></html>"""
async def main(jobs):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path=os.environ.get('CHROME') or None,args=['--allow-file-access-from-files','--no-sandbox'])
        pg=await br.new_page(viewport={'width':1080,'height':1920})
        for nome,txt,v in jobs:
            fn=M+f'_bg_{nome}.html'; open(fn,'w').write(bg(txt)); await pg.goto('file://'+fn); await pg.wait_for_timeout(400)
            await pg.screenshot(path=M+f'_bg_{nome}.png')
        await br.close()
    for nome,txt,v in jobs:
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',M+f'_bg_{nome}.png','-i',v,'-filter_complex',
          "[1:v]scale=960:1200,format=yuv420p[v];[0:v][v]overlay=60:375:shortest=1,format=yuv420p[o]",'-map','[o]','-map','1:a',
          '-c:v','libx264','-preset','veryfast','-crf','19','-c:a','copy','-movflags','+faststart',OUT+nome+'.mp4'],check=True); print('ok',nome)
E='/home/claude/entrega/black_animado/'
asyncio.run(main([('stbw_23_12','<em>NOVO</em> POST NO FEED',E+'23nov_Feed_BlackWeek_Lavagem.mp4'),
 ('stbw_24_12','<em>NOVO</em> POST NO FEED',E+'24nov_Fixo_BlackFriday_2presentes.mp4'),
 ('stbw_27_12','<em>NOVO</em> POST NO FEED',E+'27nov_Feed_EHoje_BlackFriday.mp4'),
 ('stbw_29_19','<em>NOVO</em> POST NO FEED',E+'29nov_Feed_AcabaAmanha.mp4')]))
