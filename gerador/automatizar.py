from base import *
T=6
S=[
slide(1,T,f'''<div class=k>— Trabalho repetido</div>
<h1 style="font-size:90px">Sua equipe trabalha muito.<br><i>No que um sistema faria.</i></h1>
<div style="display:flex;align-items:center;gap:40px"><p style="flex:1">As rotinas que mais comem horas numa empresa pequena e o que muda <b>quando elas rodam sozinhas.</b></p>
<div class=ph><img src="otto_a.jpg"></div></div>''',capa=True),
slide(2,T,'''<div class=k>— O problema</div>
<h2>Parece pouco.<br><i>Somando, não é.</i></h2>
<div style="display:flex;flex-direction:column;gap:14px">'''+
num(1,'Responder as mesmas perguntas','preço, horário, endereço, “ainda tem?”')+
num(2,'Copiar dado de um lugar para outro','do WhatsApp para a planilha, da planilha para o sistema')+
num(3,'Lembrar cliente que a conta venceu','quando alguém lembra de lembrar')+'</div>'),
slide(3,T,'''<div class=k>— Quanto custa</div>
<h2>Uma hora por dia<br><i>parece nada.</i></h2>
<div class=big><div class=v><span class=g data-count=264 data-at=1.6>264</span> horas</div><div class=l>por ano, de uma pessoa só. São <b style="color:#fff">33 dias inteiros</b> de trabalho.</div></div>
<p>Agora multiplique pelas pessoas da equipe que fazem isso todo dia.</p>
<div class=note>Exemplo: 1 h × 22 dias úteis × 12 meses · jornada de 8 h</div>'''),
slide(4,T,'''<div class=k>— O que dá para tirar das costas da equipe</div>
<h2>O que um sistema<br><i>já faz sozinho.</i></h2>
<div style="display:flex;flex-direction:column;gap:14px">'''+
chk('Primeiro atendimento no WhatsApp','responde, qualifica e passa para a pessoa certa')+
chk('Orçamento e agenda','sem ida e volta de mensagem')+
chk('Cobrança na data certa','lembrete antes e depois do vencimento')+
chk('Relatório pronto de manhã','sem ninguém montar planilha')+'</div>'),
slide(5,T,'''<div class=k>— Como funciona</div>
<h2>Sem trocar<br><i>o que já funciona.</i></h2>
<div style="display:flex;flex-direction:column;gap:14px">'''+
num(1,'Mapeamos as rotinas que se repetem','no diagnóstico gratuito, com você')+
num(2,'Construímos o sistema','em cima das ferramentas que você já usa')+
num(3,'A equipe fica com o que precisa de gente','vender, resolver, cuidar do cliente')+'</div>'),
slide(6,T,'''<div style="display:flex;align-items:center;gap:30px"><div class=ph style="width:160px;height:160px"><img src="otto_b.jpg"></div>
<div><div style="font:600 50px 'Cormorant Garamond'">Otto Gurgel</div><div style="font-size:25px;color:#c9cad2">Dedikar IA · diagnóstico + implementação</div></div></div>
<h2>Qual rotina <i>você tiraria primeiro?</i></h2>
<p style="margin-bottom:-8px">Comente a palavra</p>
<div class=pill><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#0b0b10" stroke-width="2.6"><path d="M4 12a8 8 0 1 1 3.2 6.4L4 20l1.1-3.6A8 8 0 0 1 4 12z"/></svg>AUTOMATIZAR</div>
<p>e escolha o <b>dia e o período</b> em que quer ser chamado para o <b>diagnóstico gratuito</b>.</p>''',foot=('@dedikar.ia · dedikaria.com.br','Envie para quem vive sem tempo')),
]
if __name__=='__main__':
    print(render('Automatizar',S,'out/2026-11-10-automatizar'))
