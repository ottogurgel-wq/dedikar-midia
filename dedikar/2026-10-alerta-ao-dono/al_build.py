"""Série 'Alerta ao dono' · @dedikar.ia · 5 posts de imagem única (feed 4:5) + versão story (9:16)."""
src=open('cx_build.py').read(); exec(src[:src.index('\nS={}')])
K=lambda s: f'<div style="font:500 26px \'JetBrains Mono\';letter-spacing:4px;color:#38d9ec;text-transform:uppercase">{s}</div>'
X='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#ff6b61" stroke-width="3.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
def it(a,fs=34): return f'<div class="card" style="padding:19px 26px;gap:18px"><div style="width:44px;height:44px;flex-shrink:0;border-radius:12px;background:rgba(255,107,97,.12);border:1.5px solid rgba(255,107,97,.55);display:flex;align-items:center;justify-content:center">{X}</div><div style="font-size:{fs}px;font-weight:600;line-height:1.25">{a}</div></div>'
def faixa(t,fs=37): return f'<div style="border:2.5px solid #38d9ec;border-radius:22px;padding:24px 30px;background:linear-gradient(90deg,rgba(56,217,236,.16),rgba(56,217,236,.04));box-shadow:0 0 60px rgba(56,217,236,.18);font:700 {fs}px \'DM Sans\';letter-spacing:.5px;line-height:1.25;text-transform:uppercase;color:#f6f4ee">{t}</div>'
TOPA=lambda n:f'<div class="top"><div class="br"><div class="tile"><img src="logo.png"></div><div class="brand">Dedikar <span>IA</span></div></div><div class="cnt" style="color:#ff6b61">● ALERTA AO DONO</div></div>'
FOOTA='<div class="foot" style="font-size:21px"><span>Salve · mande para um dono</span><span>Diagnóstico grátis: link na bio</span></div>'
def post(k,h1,lead,itens,fx,fecho,h1s=88):
    corpo=''.join(it(i) for i in itens)
    led=f'<p style="font-size:35px">{lead}</p>' if lead else ''
    return feed(TOPA(0)+f'''
<div style="display:flex;flex-direction:column;gap:26px">
 <div class="k">{k}</div>
 <h1 style="font-size:{h1s}px;letter-spacing:-1px">{h1}</h1>
 {led}
 <div style="display:flex;flex-direction:column;gap:11px">{corpo}</div>
 {faixa(fx)}
 <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:600;font-size:50px;line-height:1.1;color:#38d9ec">{fecho}</div>
</div>'''+FOOTA)
def sto(k,h1,lead,itens,fx,fecho,h1s=104):
    corpo=''.join(it(i,40) for i in itens)
    led=f'<p style="font-size:42px">{lead}</p>' if lead else ''
    return story(f'''<div style="display:flex;align-items:center;justify-content:space-between"><div class="br"><div class="tile"><img src="logo.png"></div><div class="brand">Dedikar <span>IA</span></div></div><div class="cnt" style="color:#ff6b61">● ALERTA AO DONO</div></div>
<div style="display:flex;flex-direction:column;gap:30px">{K(k)}
<h1 style="font-size:{h1s}px;letter-spacing:-1px">{h1}</h1>{led}</div>
<div style="display:flex;flex-direction:column;gap:13px">{corpo}</div>
{faixa(fx,44)}
<div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:600;font-size:64px;line-height:1.1;color:#38d9ec">{fecho}</div>
<p style="font-size:34px;font:500 32px 'JetBrains Mono';color:#c9cad2">Diagnóstico gratuito · dedikaria.com.br</p>''',46)
D=[
 ('AL1',"Empresa refém de pessoas","Sua empresa <em>funciona sem você?</em>","Se ela para quando alguém falta, você não tem uma empresa. <b>Tem um emprego caro.</b>",
  ["O cliente que chama às 19h espera até amanhã","O financeiro só fecha no dia 30","A cobrança depende de alguém lembrar","O relatório depende de uma planilha só"],
  "Antes de contratar mais, veja o que um sistema faz sozinho.","Quem não organizar agora paga mais caro depois.",96),
 ('AL2',"Checklist do dono","Cansou de <em>apagar incêndio?</em>",None,
  ["Pare de responder cliente às 22h","Pare de descobrir o prejuízo no dia 30","Pare de cobrar inadimplente “quando lembra”","Pare de depender de uma planilha","Pare de contratar para o que um sistema faz"],
  "Comece a olhar 5 números todo dia.","E pare de chamar de rotina o que é desperdício.",108),
 ('AL3',"Teste de 10 segundos","Se o seu melhor funcionário sair amanhã, <em>o que para?</em>",None,
  ["Quem sabe o preço de cada cliente?","Quem sabe o que vence esta semana?","Onde estão os contatos que ele atendia?","Quem sabe o que foi prometido a quem?"],
  "Processo que mora na cabeça de alguém não é processo. É risco.","Empresa organizada não depende de memória.",92),
 ('AL4',"Venda perdida","O seu concorrente <em>já respondeu.</em>","Enquanto você lê isto, o cliente que te chamou ontem à noite <b>fechou com quem respondeu primeiro.</b>",
  ["Mensagem fora do horário fica sem resposta","Fim de semana, ninguém atende","No pico, quem chega por último desiste","Ninguém sabe quantos foram embora"],
  "Cliente não espera. O seu atendimento espera?","Resposta em minutos vende. Em horas, não.",108),
 ('AL5',"Verdade incômoda","Planilha <em>não é sistema.</em>","Ela guarda números. <b>Não toma conta da sua empresa.</b>",
  ["Não avisa quando o caixa vai apertar","Não cobra quem atrasou","Não responde cliente","Não mostra o problema no mesmo dia"],
  "Ela só guarda o estrago para você ver depois.","Dado parado não decide nada.",120),
]
S={}
for k,kk,h1,lead,its,fx,fe,hs in D:
    S[k]=post(kk,h1,lead,its,fx,fe,hs)
    S[k+'S']=sto(kk,h1,lead,its,fx,fe,min(int(hs*1.25),118))
for k,v in S.items(): open(f'{k}.html','w').write(v)
print(list(S))
