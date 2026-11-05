import subprocess, pathlib
D = pathlib.Path('/home/claude/prev')
F = D / 'fonts'
def ff(name, path, w, style='normal'):
    return f"@font-face{{font-family:'{name}';src:url('{path}');font-weight:{w};font-style:{style}}}"
FONTS = '\n'.join([
    ff('Cormorant Garamond', F/'fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond-latin-600-normal.woff2', 600),
    ff('Cormorant Garamond', F/'fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond-latin-600-italic.woff2', 600, 'italic'),
    ff('Cormorant Garamond', F/'fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond-latin-700-italic.woff2', 700, 'italic'),
    *[ff('DM Sans', F/f'fontsource-dm-sans-5.3.0/files/dm-sans-latin-{w}-normal.woff2', w) for w in (400, 500, 600, 700, 800)],
    ff('JetBrains Mono', F/'fontsource-jetbrains-mono-5.3.0/files/jetbrains-mono-latin-500-normal.woff2', 500),
])
CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:var(--h);background:#0b0b10;color:#f6f4ee;font-family:'DM Sans';overflow:hidden;position:relative}
canvas{position:absolute;inset:0}
.glow{position:absolute;border-radius:50%;filter:blur(90px)}
.wrap{position:absolute;left:80px;right:80px;top:var(--top);display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center}
.br{display:flex;align-items:center;gap:16px}
.tile{width:58px;height:58px;background:#fff;border-radius:14px;display:flex;align-items:center;justify-content:center}
.tile img{width:48px}
.brand{font:600 36px 'Cormorant Garamond'}.brand span{color:#38d9ec}
.tag{font:500 23px 'JetBrains Mono';letter-spacing:2px;color:#fff;background:#e5483d;padding:10px 18px;border-radius:10px;box-shadow:0 0 40px rgba(229,72,61,.45)}
.kick{font:500 22px 'JetBrains Mono';letter-spacing:3px;color:#38d9ec;text-transform:uppercase;margin-top:30px}
h1{font:600 96px/1.0 'Cormorant Garamond';letter-spacing:-1px;margin-top:16px}
h1 i{color:#38d9ec;font-style:italic}
.row{display:flex;gap:30px;margin-top:40px;align-items:stretch}
.col{flex:1;display:flex;flex-direction:column;gap:12px}
.lead{font-size:28px;color:#c9cad2;margin-bottom:2px}
.card{display:flex;align-items:center;gap:16px;background:rgba(20,22,32,.88);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:15px 18px}
.x{width:40px;height:40px;flex-shrink:0;border-radius:11px;background:rgba(229,72,61,.14);border:1.5px solid rgba(229,72,61,.7);display:flex;align-items:center;justify-content:center;color:#ff6b61;font:700 24px 'DM Sans'}
.card div:last-child{font:600 26px/1.22 'DM Sans'}
.ph{width:370px;flex-shrink:0;position:relative;border-radius:22px;overflow:hidden;border:2.5px solid #38d9ec;box-shadow:0 0 60px rgba(56,217,236,.35)}
.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;display:block}
.ph .nm{position:absolute;left:0;right:0;bottom:0;padding:60px 18px 16px;background:linear-gradient(transparent,rgba(5,8,15,.95));}
.nm b{display:block;font:700 28px 'DM Sans'}.nm span{font:500 18px 'JetBrains Mono';color:#38d9ec;letter-spacing:1px}
.fx{margin-top:36px;border:2.5px solid #e5483d;border-radius:20px;padding:22px 28px;background:linear-gradient(90deg,rgba(229,72,61,.16),rgba(229,72,61,.03));box-shadow:0 0 50px rgba(229,72,61,.2);font:800 33px/1.22 'DM Sans';text-transform:uppercase}
.fx em{font-style:normal;color:#ff6b61}
.fecho{font:600 italic 44px/1.12 'Cormorant Garamond';color:#38d9ec;margin-top:22px}
.foot{margin-top:22px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);display:flex;justify-content:space-between;font:500 23px 'JetBrains Mono';color:#f6f4ee}
.foot span:last-child{color:#38d9ec}
"""
BG = """<canvas id=c></canvas>
<div class=glow style="width:520px;height:520px;left:-200px;top:%dpx;background:rgba(56,217,236,.10)"></div>
<div class=glow style="width:600px;height:600px;right:-260px;top:-200px;background:rgba(56,217,236,.08)"></div>
<script>
const c=document.getElementById('c');c.width=1080;c.height=%d;const x=c.getContext('2d');
let s=7;const r=()=>{s=(s*16807)%%2147483647;return s/2147483647};
const p=[];for(let i=0;i<70;i++)p.push([r()*1080,r()*%d]);
x.strokeStyle='rgba(56,217,236,.10)';x.lineWidth=1;
for(const a of p)for(const b of p){const d=Math.hypot(a[0]-b[0],a[1]-b[1]);if(d>0&&d<190){x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke()}}
for(const a of p){x.fillStyle=r()>.5?'rgba(56,217,236,.55)':'rgba(120,130,255,.45)';x.beginPath();x.arc(a[0],a[1],2.6,0,7);x.fill()}
x.fillStyle='rgba(255,255,255,.035)';for(let i=0;i<1080;i+=36)for(let j=0;j<%d;j+=36){x.fillRect(i,j,2,2)}
</script>"""

def page(a, story=False):
    h = 1920 if story else 1350
    top = 250 if story else 70
    itens = ''.join(f'<div class=card><div class=x>✕</div><div>{t}</div></div>' for t in a['itens'])
    foot = '' if story else f'<div class=foot><span>{a["foot"][0]}</span><span>{a["foot"][1]}</span></div>'
    extra = f'<div style="margin-top:26px;font:500 26px \'JetBrains Mono\';color:#c9cad2;text-align:center">{a["foot"][0]} · {a["foot"][1]}</div>' if story else ''
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head>
<body style="--h:{h}px;--top:{top}px">{BG % (h-700, h, h, h)}
<div class=wrap>
 <div class=top><div class=br><div class=tile><img src="logo.png"></div><div class=brand>Dedikar <span>IA</span></div></div><div class=tag>● {a['tag']}</div></div>
 <div class=kick>— {a['kick']}</div>
 <h1>{a['h1']}</h1>
 <div class=row><div class=col><div class=lead>{a['lead']}</div>{itens}</div>
  <div class=ph><img src="otto.jpg"><div class=nm><b>Otto Gurgel</b><span>{a['cargo']}</span></div></div></div>
 <div class=fx>{a['fx']}</div>
 <div class=fecho>{a['fecho']}</div>{foot}{extra}
</div></body></html>"""

ARTES = {
 'A_empresario': dict(tag='ALERTA AO EMPRESÁRIO', kick='Carpina · Paudalho · Nazaré da Mata e região',
   h1='Sua empresa cresceu.<br><i>Os processos, não.</i>', lead='Se na sua empresa ainda…',
   itens=['O cliente espera horas por resposta no WhatsApp','Orçamento, cobrança e agenda são feitos na mão','Você só descobre se deu lucro no fim do mês','Sua equipe passa o dia em tarefa repetida'],
   cargo='DEDIKAR IA', fx='Antes de aumentar a equipe,<br><em>tire o trabalho repetido das costas dela.</em>',
   fecho='Cada mês sem sistema é dinheiro indo embora.',
   foot=('Comente <b style="color:#38d9ec">AUTOMATIZAR</b> e escolha o dia','dedikaria.com.br')),
 'B_gestor_publico': dict(tag='ALERTA AO GESTOR PÚBLICO', kick='Secretários · Vereadores · Prefeituras de PE',
   h1='O cidadão cobra rápido.<br><i>A gestão responde no papel.</i>', lead='Se na sua secretaria ainda…',
   itens=['A demanda do cidadão chega no WhatsApp e se perde','Ofício, protocolo e relatório são feitos na mão','Ninguém sabe o custo real de cada veículo da frota','O problema só aparece quando já virou cobrança'],
   cargo='DEDIKAR IA', fx='Antes de ampliar a equipe,<br><em>tire a rotina repetida da mesa do servidor.</em>',
   fecho='Gestão que responde rápido é gestão que aparece.',
   foot=('Comente <b style="color:#38d9ec">GESTÃO</b> · Raio-X gratuito','dedikaria.com.br')),
}
for k, a in ARTES.items():
    for story in (False, True):
        n = f"{k}_{'story' if story else 'feed'}"
        (D/f'{n}.html').write_text(page(a, story))
        h = 1920 if story else 1350
        subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',
                        f'--window-size=1080,{h}','--virtual-time-budget=3000',f'--screenshot={D}/{n}.png',f'file://{D}/{n}.html'],capture_output=True)
        print(n)
