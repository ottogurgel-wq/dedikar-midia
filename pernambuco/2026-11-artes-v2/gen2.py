#!/usr/bin/env python3
# Artes do Instagram @pernambucorent no padrão aprovado pela diretoria
# (fundo branco, logo grande, título verde-escuro + azul + manuscrito, ícones em círculos, botão WhatsApp, contatos, faixas).
import os, sys, asyncio
B = os.environ.get('V2', '/home/claude/v2').rstrip('/') + '/'
F, H, O = B + 'fotos/', B + 'html/', B + 'out/'
os.makedirs(H, exist_ok=True); os.makedirs(O, exist_ok=True)

VE, VD, AZ, AM, VM = '#0E5A2C', '#2E9E3E', '#1747A6', '#F5C400', '#E1251B'   # verde escuro, verde, azul, amarelo, vermelho
SITE, WPP = 'pernambucolocadora.com.br', '81 99633.2862'

FONTS = ''.join(f"@font-face{{font-family:P;font-weight:{w};src:url('file://{B}poppins-latin-{w}-normal.woff2')}}" for w in (500, 600, 700, 800, 900))
FONTS += f"@font-face{{font-family:S;font-weight:700;src:url('file://{B}dancing-script-latin-700-normal.woff2')}}"
CSS = FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
.c{{position:relative;overflow:hidden;background:#fff;font-family:P;color:{VE}}}
.abs{{position:absolute}}
.t1{{font-weight:800;color:{VE};letter-spacing:-2px;line-height:.95}}
.t2{{font-weight:900;color:{AZ};letter-spacing:-3px;line-height:.92}}
.sc{{font-family:S;font-weight:700;color:{VE};line-height:1}}
.brush{{display:block;height:10px;border-radius:10px;background:{AM};transform:rotate(-1.5deg)}}
.sub{{font-weight:700;color:{AZ};line-height:1.12}}
.bl{{display:flex;align-items:center;gap:18px;margin-bottom:14px}}
.bl .ci{{width:72px;height:72px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 4px 10px rgba(0,0,0,.12)}}
.bl b{{display:block;font-weight:700;font-size:24px;white-space:nowrap;color:#11233a;line-height:1.1}}
.bl span{{font-weight:500;font-size:19px;color:#4b5563;line-height:1.2}}
.cta{{display:flex;align-items:center;background:linear-gradient(180deg,#147a3a,{VE});border-radius:999px;color:#fff;box-shadow:0 10px 24px rgba(14,90,44,.35)}}
.cta .w{{width:86px;height:86px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}}
.cta .tx small{{display:block;font-weight:500;font-size:23px;line-height:1}}
.cta .tx strong{{display:block;font-weight:800;font-size:40px;line-height:1.05}}
.cta .sep{{width:2px;align-self:stretch;margin:16px 18px;background:rgba(255,255,255,.45)}}
.ct{{font-weight:500;font-size:19px;color:{AZ};line-height:1.25}}
.ct div{{display:flex;align-items:center;gap:10px;margin-bottom:7px}}
.legal{{font-weight:500;font-size:15px;color:#6b7280;line-height:1.3}}
.selo{{display:inline-block;background:{VE};color:#fff;font-weight:800;letter-spacing:3px;border-radius:12px;padding:8px 18px}}
.selo em{{font-style:normal;color:{AM}}}
.foto{{background-size:cover;background-position:center;
 -webkit-mask-image:linear-gradient(to right,transparent 0,#000 30%),linear-gradient(to bottom,transparent 0,#000 16%);-webkit-mask-composite:source-in}}
"""

def ico(n, cor='#fff', s=40):
    p = {
     'car': "<path d='M5 11l1.6-4.6A2 2 0 0 1 8.5 5h7a2 2 0 0 1 1.9 1.4L19 11h1v6h-2v2h-3v-2H9v2H6v-2H4v-6zm2.1 0h9.8l-1-3H8.1zM7 13.3a1.3 1.3 0 1 0 0 2.6 1.3 1.3 0 0 0 0-2.6m10 0a1.3 1.3 0 1 0 0 2.6 1.3 1.3 0 0 0 0-2.6'/>",
     'shield': "<path d='M12 2l8 3v6c0 5-3.4 9.4-8 11-4.6-1.6-8-6-8-11V5zm-1.2 13.4l5.6-5.6-1.4-1.4-4.2 4.2-2-2-1.4 1.4z'/>",
     'people': "<path d='M9 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7m7 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6M2 19c0-3.3 3.1-5.5 7-5.5s7 2.2 7 5.5v1H2zm15-5.4c2.9.3 5 2 5 4.4v2h-4v-1c0-2.1-.4-3.9-1-5.4'/>",
     'chart': "<path d='M4 20V10h4v10zm6 0V4h4v16zm6 0v-7h4v7z'/>",
     'gift': "<path d='M20 7h-2.2A3 3 0 0 0 12 4.2 3 3 0 0 0 6.2 7H4v5h1v8h14v-8h1zM9 5.5c.8 0 1.5.7 1.5 1.5H9a.75.75 0 0 1 0-1.5m6 0a.75.75 0 0 1 0 1.5h-1.5c0-.8.7-1.5 1.5-1.5M6 9h5v2H6zm7 0h5v2h-5zM7 13h4v5H7zm6 0h4v5h-4z'/>",
     'drop': "<path d='M12 2s-7 7.6-7 12.5A7 7 0 0 0 19 14.5C19 9.6 12 2 12 2m-3.5 12.5h2a1.5 1.5 0 0 0 1.5 1.5v2a3.5 3.5 0 0 1-3.5-3.5'/>",
     'cal': "<path d='M7 2h2v2h6V2h2v2h3v16H4V4h3zm-1 7v9h12V9zm2 2h3v3H8z'/>",
     'pin': "<path d='M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7m0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5'/>",
     'globe': "<path d='M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m6.9 6h-2.9a15.6 15.6 0 0 0-1.4-3.6A8 8 0 0 1 18.9 8M12 4c.8 1.2 1.5 2.5 1.9 4h-3.8c.4-1.5 1.1-2.8 1.9-4M4.3 14a8 8 0 0 1 0-4h3.4a16 16 0 0 0 0 4zm.8 2h2.9c.3 1.3.8 2.5 1.4 3.6A8 8 0 0 1 5.1 16M8 8H5.1a8 8 0 0 1 4.3-3.6C8.8 5.5 8.3 6.7 8 8m4 12c-.8-1.2-1.5-2.5-1.9-4h3.8c-.4 1.5-1.1 2.8-1.9 4m2.3-6H9.7a14 14 0 0 1 0-4h4.6a14 14 0 0 1 0 4m.3 5.6c.6-1.1 1.1-2.3 1.4-3.6h2.9a8 8 0 0 1-4.3 3.6m1.7-5.6a16 16 0 0 0 0-4h3.4a8 8 0 0 1 0 4z'/>",
     'wa': "<path d='M12 2a10 10 0 0 0-8.7 14.9L2 22l5.2-1.3A10 10 0 1 0 12 2m5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5.1-4.5-.1-.2-1.2-1.6-1.2-3s.8-2.2 1-2.5c.3-.3.6-.4.8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 .9c.3.2.5.2.6.4.1.1.1.8-.1 1.5'/>",
     'mail': "<path d='M3 5h18v14H3zm2 2v.5l7 4.5 7-4.5V7zm0 2.9V17h14V9.9l-7 4.5z'/>",
     'key': "<path d='M7 14a5 5 0 1 1 4.6-7H22v4h-2v3h-3v-3h-5.4A5 5 0 0 1 7 14m0-3a2 2 0 1 0 0-4 2 2 0 0 0 0 4'/>",
     'clock': "<path d='M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m1 10.4V6h-2v7.6l5.2 3.1 1-1.7z'/>",
     'plane': "<path d='M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z'/>",
    }[n]
    return f"<svg width='{s}' height='{s}' viewBox='0 0 24 24' fill='{cor}'>{p}</svg>"

CORES = [VD, AZ, AM, VM]

def bullets(itens, x, y, w=420):
    h = ''.join(f"<div class='bl'><div class='ci' style='background:{CORES[i % 4]}'>{ico(ic)}</div><div><b>{t}</b><span>{s}</span></div></div>" for i, (ic, t, s) in enumerate(itens))
    return f"<div class='abs' style='left:{x}px;top:{y}px;width:{w}px'>{h}</div>"

def cta(x, y, l1='Reserve pelo', l2='WhatsApp', w=470, icon='wa'):
    return (f"<div class='abs cta' style='left:{x}px;top:{y}px;width:{w}px;padding:9px 26px 9px 10px'>"
            f"<div class='w'>{ico(icon, VE, 54)}</div><div class='tx' style='margin-left:18px;flex:1'><small>{l1}</small><strong>{l2}</strong></div>"
            f"<div class='sep'></div><svg width='26' height='40' viewBox='0 0 26 40'><path d='M6 5l14 15L6 35' stroke='#fff' stroke-width='5' fill='none' stroke-linecap='round'/></svg></div>")

def contatos(x, y):
    return (f"<div class='abs ct' style='left:{x}px;top:{y}px'>"
            f"<div>{ico('globe', AZ, 24)}<b style='font-weight:700'>{SITE}</b></div>"
            f"<div>{ico('wa', VD, 24)}<b style='font-weight:700'>{WPP}</b>&nbsp;·&nbsp;WhatsApp 24h</div>"
            f"<div>{ico('pin', VE, 24)}Av. 20 de Janeiro, 469 · Boa Viagem</div></div>")

def faixas(w, h):
    # faixas verde/amarela/vermelha no canto inferior direito, como nas artes aprovadas
    return (f"<svg class='abs' style='left:0;top:0' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
            f"<path d='M{w*0.52} {h} C{w*0.75} {h-60} {w*0.9} {h-130} {w} {h-215} L{w} {h}Z' fill='{VD}'/>"
            f"<path d='M{w*0.6} {h} C{w*0.8} {h-50} {w*0.92} {h-110} {w} {h-180} L{w} {h}Z' fill='{AM}'/>"
            f"<path d='M{w*0.66} {h} C{w*0.83} {h-40} {w*0.94} {h-95} {w} {h-152} L{w} {h}Z' fill='{VM}'/></svg>")

def canto(w, txt):
    # painel verde-escuro curvo no canto superior direito com texto branco e traço amarelo
    return (f"<svg class='abs' style='left:0;top:0' width='{w}' height='300' viewBox='0 0 {w} 300'>"
            f"<path d='M{w-360} 0 C{w-330} 120 {w-200} 215 {w} 236 L{w} 0Z' fill='{VE}'/>"
            f"<path d='M{w-372} 0 C{w-346} 128 {w-210} 226 {w} 248 L{w} 240 C{w-200} 219 {w-334} 124 {w-360} 0Z' fill='{VD}'/></svg>"
            f"<div class='abs' style='right:26px;top:34px;width:250px;color:#fff;font-weight:500;font-size:24px;line-height:1.25;text-align:left'>{txt}"
            f"<span class='brush' style='width:110px;height:7px;margin-top:12px'></span></div>")

def logo(x, y, w=500, tag=True):
    t = (f"<div style='display:flex;align-items:center;gap:14px;margin-top:10px;color:{AZ};font-weight:500;font-size:{int(w*0.034)}px;letter-spacing:{int(w*0.012)}px'>"
         f"<i style='flex:1;height:2px;background:{AZ}'></i>MOBILIDADE EM TODO CAMINHO<i style='flex:1;height:2px;background:{AZ}'></i></div>") if tag else ''
    return f"<div class='abs' style='left:{x}px;top:{y}px;width:{w}px'><img src='file://{B}logo.png' style='width:100%;display:block'>{t}</div>"

def titulo(x, y, l1, l2, l3=None, s1=78, s2=118, s3=92, w=700, sub=''):
    sc = f"<div class='sc' style='font-size:{s3}px;margin-top:6px'>{l3}</div><span class='brush' style='width:{int(w*0.55)}px;margin-left:30px;margin-top:-4px'></span>" if l3 else ''
    a = f"<div class='t1' style='font-size:{s1}px'>{l1}</div>" if l1 else ''
    sb = f"<div class='sub' style='font-size:31px;width:620px;margin-top:20px'>{sub}</div>" if sub else ''
    return f"<div class='abs' style='left:{x}px;top:{y}px;width:{w}px'>{a}<div class='t2' style='font-size:{s2}px;margin-top:{max(4, (s2 - 100) // 2)}px'>{l2}</div>{sc}{sb}</div>"

def foto(nome, x, y, w, h, pos='center'):
    return f"<div class='abs foto' style='left:{x}px;top:{y}px;width:{w}px;height:{h}px;background-image:url(file://{F}{nome}.jpg);background-position:{pos}'></div>"

def frase(x, y, s=50, txt='Pernambuco<br>te leva mais longe.'):
    return f"<div class='abs sc' style='left:{x}px;top:{y}px;font-size:{s}px;transform:rotate(-6deg)'>{txt}<span class='brush' style='width:{int(s*4.2)}px;margin-top:10px'></span></div>"

LEGAL = 'Reservas feitas até 30/11/2026 pelo site ou WhatsApp, com retirada em qualquer data. Sujeito à disponibilidade.'
LEGAL_L = 'Lavagem grátis em locações a partir de 4 diárias. Reservas até 30/11/2026 pelo site ou WhatsApp, retirada em qualquer data. Sujeito à disponibilidade.'

P = {}
W, HH = 1080, 1350

def feed(nome, l1, l2, l3, sub, ft, itens, canto_txt, selo='', legal=LEGAL, s=(78, 118, 92), fpos='center', extra='', ty=262):
    sel = f"<div class='abs' style='left:52px;top:{ty-58}px'><span class='selo' style='font-size:22px'>{selo}</span></div>" if selo else ''
    P[nome] = (W, HH, f"""
{foto(ft, 400, 600, 680, 540, fpos)}
{canto(W, canto_txt)}
{logo(50, 46, 500)}
{sel}
{titulo(52, ty, l1, l2, l3, *s, sub=sub)}
{bullets(itens, 52, 700)}
{cta(36, 1140)}
{contatos(530, 1146)}
<div class='abs legal' style='left:40px;top:1262px;width:610px'>{legal}</div>
{faixas(W, HH)}
{extra}""")

BEN_C = [('gift', 'Condutor grátis', 'reservas até 30/11.'), ('cal', 'Retire quando quiser', 'qualquer data.'),
         ('shield', 'Veículos revisados', 'e com total segurança.'), ('people', 'Atendimento', 'próximo e humano.')]
BEN_2 = [('gift', 'Condutor grátis', 'em todas as reservas.'), ('drop', 'Lavagem grátis', 'a partir de 4 diárias.'),
         ('cal', 'Retire quando quiser', 'reserve até 30/11.'), ('people', 'Site ou WhatsApp', 'você escolhe.')]

feed('01_fixo_esquenta_black_condutor', 'Condutor', 'adicional', 'grátis!', 'Divida o volante sem pagar a mais.', 'suv_olinda', BEN_C,
     'Esquenta<br>Black Friday<br>Pernambuco.', selo='ESQUENTA <em>BLACK FRIDAY</em>', fpos='60% center')
feed('02_feed_condutor_adicional', 'Dois no volante,', 'zero custo', 'extra.', 'Condutor adicional grátis nas reservas até 30/11.', 'familia', BEN_C,
     'Mais que aluguel,<br>novos caminhos<br>por Pernambuco.', s=(70, 112, 92))
feed('04_feed_aeroporto_praia', 'Do aeroporto', 'à praia,', 'revezando o volante.', 'Porto de Galinhas, Carneiros e Maragogi.', 'aeroporto', BEN_C,
     'Chegou em Recife?<br>Seu carro está<br>perto de você.', s=(74, 118, 74))
feed('05_feed_feriadao_20nov', 'Feriadão', 'pede estrada.', '20 de novembro', 'Gravatá, Porto de Galinhas ou Olinda: você escolhe o destino.', 'praia',
     [('car', 'Carro revisado', 'pronto para a estrada.'), ('gift', 'Condutor grátis', 'reservas até 30/11.'), ('pin', 'Retirada fácil', 'em Boa Viagem.'), ('people', 'Atendimento', 'próximo e humano.')],
     'Pernambuco<br>te leva<br>mais longe.', s=(84, 92, 76))
feed('06_feed_blackweek_lavagem', 'Black Week:', 'lavagem', 'grátis!', 'Em locações a partir de 4 diárias, reservando até 30/11.', 'revisao', BEN_2,
     'Black Week<br>Pernambuco<br>Rent a Car.', selo='<em>BLACK</em> WEEK', legal=LEGAL_L, fpos='70% center')
feed('07_fixo_black_2beneficios', 'Black Friday', 'Pernambuco', 'dois presentes pra você.', 'Para reservas feitas até 30/11, pelo site ou WhatsApp.', 'banner_suv', BEN_2,
     'Benefícios<br>válidos até<br>30 de novembro.', selo='<em>BLACK</em> FRIDAY', legal=LEGAL_L, s=(78, 104, 70))
feed('08_feed_black_friday_hoje', 'É hoje:', 'Black Friday!', 'Pernambuco te leva mais longe.', 'Condutor adicional grátis e lavagem grátis a partir de 4 diárias.', 'suv_olinda', BEN_2,
     'Reserve hoje,<br>retire quando<br>quiser.', selo='<em>BLACK</em> FRIDAY', legal=LEGAL_L, s=(82, 100, 58), fpos='60% center')
feed('09_feed_ultima_chance', 'Acaba amanhã:', '30/11', 'última chance.', 'Último dia para garantir os benefícios da Black.', 'familia', BEN_2,
     'Não deixe para<br>a última hora.', selo='<em>ÚLTIMA</em> CHAMADA', legal=LEGAL_L, s=(76, 130, 76))

# Carrossel do site
PHONE = f"""<div class='abs' style='left:640px;top:420px;width:370px;height:700px;border-radius:52px;background:#111;padding:14px;box-shadow:0 30px 60px rgba(0,0,0,.3);transform:rotate(4deg)'>
<div style='width:100%;height:100%;border-radius:40px;background:#f4f7fb;overflow:hidden'>
 <div style='background:#fff;padding:24px 20px 12px'><img src='file://{B}logo.png' style='width:200px'></div>
 <div style='background:linear-gradient(135deg,{VE},#147a3a);color:#fff;padding:20px'><div style='font-size:24px;font-weight:800;line-height:1.1'>Aluguel de carros<br>em Recife</div><div style='font-size:14px;margin-top:6px'>Reserve online em minutos</div></div>
 <div style='padding:16px'><div style='background:#fff;border-radius:14px;padding:12px;box-shadow:0 4px 12px rgba(0,0,0,.08);font-size:14px;color:#33475b'>
  <div style='font-weight:700;color:{VE};margin-bottom:6px'>Retirada</div><div style='border:1px solid #dde3ea;border-radius:10px;padding:9px'>Boa Viagem · Recife</div>
  <div style='display:flex;gap:6px;margin-top:8px'><div style='flex:1;border:1px solid #dde3ea;border-radius:10px;padding:9px'>Retirada</div><div style='flex:1;border:1px solid #dde3ea;border-radius:10px;padding:9px'>Devolução</div></div>
  <div style='margin-top:12px;background:{AZ};color:#fff;border-radius:999px;text-align:center;padding:11px;font-weight:800;font-size:16px'>Ver carros e preços</div></div>
 <div style='margin-top:12px;background:#fff8d6;border:2px dashed {AM};border-radius:12px;padding:10px;font-size:14px;color:#5a4500;font-weight:700'>Condutor adicional grátis até 30/11</div></div></div></div>"""
P['03a_carrossel_site_capa'] = (W, HH, f"""
{canto(W, 'Arraste para o lado<br>e veja como<br>é fácil →')}
{logo(50, 46, 500)}
{titulo(52, 262, 'Sua reserva', 'na palma', 'da sua mão.', 78, 112, 88, 600, sub='Escolha o carro, veja o preço na hora e pague no Pix ou no cartão.')}
{bullets([('car', 'Escolha o carro', 'econômico, sedan ou SUV.'), ('cal', 'Defina as datas', 'retire quando quiser.'), ('shield', 'Pague seguro', 'Pix ou cartão.')], 52, 720, 520)}
{PHONE}
{cta(36, 1140, 'Reserve pelo', 'site', 470, 'globe')}
{contatos(530, 1146)}
{faixas(W, HH)}""")
P['03b_carrossel_site_passos'] = (W, HH, f"""
{foto('carros', 400, 600, 680, 540)}
{canto(W, 'Simples assim.<br>Do celular<br>à estrada.')}
{logo(50, 46, 500)}
{titulo(52, 262, 'Em 3 passos,', 'seu carro', 'reservado.', 78, 112, 88, sub='Pelo site ou pelo WhatsApp, como preferir.')}
{bullets([('pin', '1. Local e datas', 'retirada em Boa Viagem.'), ('car', '2. Escolha o carro', 'econômico, sedan ou SUV.'), ('shield', '3. Pague e pronto', 'Pix ou cartão.')], 52, 720)}
{cta(36, 1140)}
{contatos(530, 1146)}
{faixas(W, HH)}""")
feed('03c_carrossel_site_beneficio', 'Reservou até', '30/11?', 'Ganhou!', 'Condutor adicional grátis. E vem mais novidade na Black Week.', 'atendimento', BEN_C,
     'Ativa o sininho:<br>vem novidade<br>na Black Week.', s=(78, 128, 96))

# ---------- Stories 1080x1920 ----------
SW, SH = 1080, 1920
def story(nome, l1, l2, l3, sub, ft, selo='', itens=None, s=(84, 124, 96), legal=LEGAL, fpos='center'):
    sel = f"<div class='abs' style='left:0;right:0;top:330px;text-align:center'><span class='selo' style='font-size:26px'>{selo}</span></div>" if selo else ''
    bl = bullets(itens, 70, 1250, 600) if itens else ''
    P[nome] = (SW, SH, f"""
<div class='abs foto' style='left:0;top:880px;width:{SW}px;height:820px;background-image:url(file://{F}{ft}.jpg);background-position:{fpos};-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 22%,#000 82%,transparent 100%)'></div>
{logo(190, 140, 700)}
{sel}
<div class='abs' style='left:0;right:0;top:{400 if selo else 360}px;text-align:center'>
 {f"<div class='t1' style='font-size:{s[0]}px'>{l1}</div>" if l1 else ''}<div class='t2' style='font-size:{s[1]}px'>{l2}</div>
 {f"<div class='sc' style='font-size:{s[2]}px;margin-top:8px'>{l3}</div><span class='brush' style='width:420px;margin:0 auto'></span>" if l3 else ''}
 <div class='sub' style='font-size:38px;margin:26px auto 0;width:860px'>{sub}</div></div>
{bl}
{cta(170, 1640, 'Toque no link da bio', 'ou chame no WhatsApp', 740)}
<div class='abs legal' style='left:70px;top:1790px;width:640px'>{legal}</div>
{faixas(SW, SH)}""")

story('10_story_condutor', 'Condutor', 'adicional', 'grátis!', 'Nas reservas feitas até 30/11 pelo site ou WhatsApp.', 'familia', 'ESQUENTA <em>BLACK FRIDAY</em>')
story('11_story_lavagem_black', 'Black Week:', 'lavagem', 'grátis!', 'Em locações a partir de 4 diárias + condutor adicional grátis.', 'revisao', '<em>BLACK</em> WEEK', legal=LEGAL_L, fpos='70% center')
for k, t, s_, ft in [('olinda', 'Olinda', 'Ladeiras, frevo e vista para o mar a 20 min do Recife.', 'suv_olinda'),
                     ('porto', 'Porto de Galinhas', 'Piscinas naturais a 1h de carro. Vá no seu ritmo.', 'praia'),
                     ('carneiros', 'Carneiros', 'A igrejinha na areia mais famosa do Nordeste.', 'banner_suv'),
                     ('gravata', 'Gravatá', 'Clima de serra a 1h20 do Recife.', 'aeroporto')]:
    story(f'14_story_destino_{k}', 'Destino da semana:', t, 'Pernambuco te leva mais longe.', s_, ft, s=(60, 120 if len(t) < 12 else 96, 64))
story('15_story_site_3passos', 'Reserve em', '3 passos', 'rapidinho.', 'Local e datas · carro · Pix ou cartão. Pelo site ou WhatsApp.', 'carros')
for n, (a, b) in enumerate([('Faltam', '3 dias'), ('Faltam', '2 dias'), ('Acaba', 'amanhã!'), ('Último dia:', 'é hoje!')]):
    story(f'16_story_contagem_{n+1}', a, b, 'Black Friday Pernambuco', 'Condutor adicional grátis + lavagem grátis a partir de 4 diárias.',
          ['suv_olinda', 'praia', 'familia', 'banner_suv'][n], '<em>BLACK</em> FRIDAY', legal=LEGAL_L, s=(90, 150, 70))
# Reels (quadros 9:16)
story('13_reels_capa_dividir_volante', '3 motivos', 'pra dividir', 'o volante.', 'Viaje por Pernambuco revezando a direção.', 'aeroporto')
story('r1_2', 'Motivo 1:', 'ninguém chega', 'cansado.', 'Revezando, a estrada até a praia fica leve.', 'familia', s=(84, 100, 96))
story('r1_3', 'Motivo 2:', 'todo mundo', 'curte a vista.', 'Cada um dirige um trecho e aproveita a paisagem.', 'praia', s=(84, 110, 96))
story('r1_4', 'Motivo 3:', 'sai de graça!', 'até 30/11.', 'Condutor adicional grátis nas reservas pelo site ou WhatsApp.', 'suv_olinda', s=(84, 110, 96))
story('r2_1', 'Roteiro de', '5 dias', 'saindo do Recife.', 'Salva esse roteiro para a sua viagem.', 'carros')
for i, (d, t, ft) in enumerate([('Dia 1', 'Olinda', 'suv_olinda'), ('Dia 2', 'Porto de Galinhas', 'praia'), ('Dia 3', 'Carneiros', 'banner_suv'), ('Dia 4', 'Gravatá', 'aeroporto'), ('Dia 5', 'Recife Antigo', 'familia')]):
    story(f'r2_{i+2}', d, t, 'Pernambuco te leva mais longe.', '', ft, s=(90, 120 if len(t) < 12 else 96, 64))
story('r2_7', 'Carro revisado,', 'retirada fácil', 'em Boa Viagem.', 'Reserve pelo site ou WhatsApp.', 'atendimento', s=(76, 100, 90))
story('r3_1', 'Black Week', 'Pernambuco', 'dois presentes pra você.', 'Para reservas feitas até 30/11.', 'suv_olinda', '<em>BLACK</em> WEEK', s=(84, 116, 70))
story('r3_2', 'Presente 1:', 'condutor', 'adicional grátis.', 'Em todas as reservas até 30/11.', 'familia', '<em>BLACK</em> WEEK', s=(84, 130, 80))
story('r3_3', 'Presente 2:', 'lavagem', 'grátis!', 'Em locações a partir de 4 diárias.', 'revisao', '<em>BLACK</em> WEEK', legal=LEGAL_L, fpos='70% center', s=(84, 130, 96))
story('r3_4', 'Só até', '30/11', 'retire quando quiser.', 'Reserve pelo site ou WhatsApp.', 'banner_suv', '<em>BLACK</em> WEEK', legal=LEGAL_L, s=(84, 170, 76))

def pagina(w, h, corpo):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='c' style='width:{w}px;height:{h}px'>{corpo}</div></body></html>"

async def render(nomes):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get('CHROME') or None, args=['--allow-file-access-from-files', '--no-sandbox'])
        for n in nomes:
            w, h, corpo = P[n]
            fn = H + n + '.html'; open(fn, 'w').write(pagina(w, h, corpo))
            pg = await br.new_page(viewport={'width': w, 'height': h})
            await pg.goto('file://' + fn); await pg.wait_for_timeout(350)
            await pg.screenshot(path=O + n + '.png'); await pg.close()
        await br.close()
    print('renderizadas', len(nomes))

asyncio.run(render(sys.argv[1:] or list(P)))
