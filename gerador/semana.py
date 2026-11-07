import base, base_og
from base import slide, num, chk
T=6
def ph(f,size=None): 
    st=f' style="width:{size}px;height:{size}px"' if size else ''
    return f'<div class=ph{st}><img src="fotos/{f}.jpg"></div>'
def capa(k,h1,p,foto,h1s=None):
    s=f' style="font-size:{h1s}px"' if h1s else ''
    return f'''<div class=k>— {k}</div><h1{s}>{h1}</h1>
<div style="display:flex;align-items:center;gap:40px"><p style="flex:1">{p}</p>{ph(foto)}</div>'''
def bloco(k,h2,itens,extra=''): return f'<div class=k>— {k}</div><h2>{h2}</h2><div style="display:flex;flex-direction:column;gap:14px">{"".join(itens)}</div>{extra}'
def cta(foto,h2,palavra,texto,foot):
    return slide(6,T,f'''<div style="display:flex;align-items:center;gap:30px">{ph(foto,160)}
<div><div style="font:600 50px 'Cormorant Garamond'">Otto Gurgel</div><div style="font-size:25px;color:#c9cad2">Dedikar IA · diagnóstico + implementação</div></div></div>
<h2>{h2}</h2><p style="margin-bottom:-8px">Comente a palavra</p>
<div class=pill><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#0b0b10" stroke-width="2.6"><path d="M4 12a8 8 0 1 1 3.2 6.4L4 20l1.1-3.6A8 8 0 0 1 4 12z"/></svg>{palavra}</div>
<p>{texto}</p>''',foot=('@dedikar.ia · dedikaria.com.br',foot))
D={}
D['Diagnostico']=('dedikar/2026-11-12-termometro',[
 slide(1,T,capa('Teste de 30 segundos','Sua operação está<br><i>quente ou fria?</i>','Conte quantos destes sinais acontecem aí. <b>No fim, veja o resultado.</b>','otto_04_blazer_azul_estrategia'),capa=True),
 slide(2,T,bloco('Sinais de operação fria','Marque os que<br><i>acontecem aí.</i>',[num(1,'O cliente espera mais de 1 hora','por resposta no WhatsApp'),num(2,'Ninguém sabe o caixa da semana','sem abrir uma planilha'),num(3,'A cobrança depende de alguém lembrar','e às vezes ninguém lembra')])),
 slide(3,T,bloco('Continue contando','Mais dois<br><i>sinais.</i>',[num(4,'O relatório leva mais de 1 dia','para ficar pronto'),num(5,'Se uma pessoa falta, um processo para','porque só ela sabe fazer')])),
 slide(4,T,bloco('O resultado','Quantos<br><i>você marcou?</i>',[chk('0 a 1 · operação quente','dá para ajustar o fino'),chk('2 a 3 · operação morna','tem dinheiro escapando todo mês'),chk('4 a 5 · operação fria','organizar vem antes de crescer')])),
 slide(5,T,bloco('O próximo passo','O diagnóstico mostra<br><i>por onde começar.</i>',[num(1,'45 minutos sobre a sua operação','gratuito, com você'),num(2,'As rotinas que mais custam','em horas e em dinheiro'),num(3,'O primeiro sistema a implantar','com prazo e por etapa')])),
 cta('otto_03_blazer_grafite_escritorio','Me conta o seu <i>número.</i>','DIAGNÓSTICO','e eu te mando o link para agendar o <b>diagnóstico gratuito de 45 minutos</b>.','Envie para um sócio'),
])
D['Caixa']=('dedikar/2026-11-13-projecao-caixa',[
 slide(1,T,capa('Projeção de caixa','Você sabe o seu caixa<br><i>daqui a 30 dias?</i>','Quem só olha o saldo de hoje descobre o aperto <b>quando ele já chegou.</b>','otto_02_blazer_cinza_claro',88),capa=True),
 slide(2,T,bloco('O problema','O saldo de hoje<br><i>engana.</i>',[num(1,'Conta grande vencendo no dia 25','e ninguém lembrou no dia 10'),num(2,'Cliente que atrasou e ninguém viu','o dinheiro que contava não entrou'),num(3,'Compra feita sem olhar o mês seguinte','o saldo some na semana errada')])),
 slide(3,T,'''<div class=k>— A visão que falta</div><h2>O caixa dia a dia,<br><i>meses à frente.</i></h2>
<div class=big><div class=v><span class=g data-count=90 data-at=1.6>90</span> dias</div><div class=l>de saldo projetado numa tela: o que entra, o que sai e <b style="color:#fff">o saldo de cada dia.</b></div></div>
<p>É o que construímos no painel financeiro de uma locadora cliente.</p>'''),
 slide(4,T,bloco('O que entra na conta','O que a projeção<br><i>enxerga.</i>',[chk('Contas a receber','com a data prevista de cada uma'),chk('Contas a pagar e parcelas','do mês e dos próximos'),chk('Atrasos de clientes','o que não entrou aparece na hora'),chk('Mais de uma empresa','comparadas na mesma tela')])),
 slide(5,T,bloco('Como funciona','Sem trocar<br><i>o seu sistema.</i>',[num(1,'Conectamos ao que você já usa','sistema, banco ou planilha'),num(2,'O painel atualiza sozinho','sem ninguém montar relatório'),num(3,'Você decide antes do aperto','e não depois')])),
 cta('otto_05_blazer_azul_pessoas','Quer projetar o <i>seu caixa?</i>','CAIXA','e eu te mando no direct a <b>planilha modelo</b> para projetar os próximos dias.','Envie para o financeiro'),
])
D['Agentes']=('dedikar/2026-11-16-tres-agentes',[
 slide(1,T,capa('Agentes de IA','Três agentes de IA.<br><i>Nenhum decide sozinho.</i>','Como funciona uma equipe que trabalha 24h <b>sem passar por cima do dono.</b>','otto_13_blazer_polo_verde',90),capa=True),
 slide(2,T,bloco('A equipe','Cada um com<br><i>uma função.</i>',[num(1,'Atendimento','responde o cliente a qualquer hora'),num(2,'Comercial','faz o follow-up e organiza o CRM'),num(3,'Financeiro','acompanha cobranças e vencimentos')])),
 slide(3,T,bloco('A regra que não muda','O agente executa.<br><i>Você aprova.</i>',[chk('Proposta e desconto','só saem com a sua aprovação'),chk('Caso fora do padrão','o agente chama uma pessoa'),chk('Tudo registrado','você vê o que cada um fez')])),
 slide(4,T,bloco('O que muda no dia a dia','Menos incêndio,<br><i>mais decisão.</i>',[chk('O cliente das 19h é respondido','na hora, não no dia seguinte'),chk('Nenhum lead fica sem retorno','o follow-up sai no prazo'),chk('O relatório do dia fica pronto','antes de você chegar')])),
 slide(5,T,bloco('Como começa','Pequeno primeiro,<br><i>depois cresce.</i>',[num(1,'Diagnóstico das tarefas repetidas','onde a equipe perde mais tempo'),num(2,'Agente treinado com as suas regras','preço, prazo, tom de voz'),num(3,'Um agente por vez','cada etapa com resultado medido')])),
 cta('otto_01_terno_fundo_preto','Qual tarefa <i>você daria primeiro?</i>','AGENTE','e eu te mando no direct o <b>vídeo</b> de como montar uma equipe assim na sua empresa.','Envie para quem vive no WhatsApp'),
])
# ---------- @ottogurgel.ofc ----------
og=base_og
def ogcapa(tag,h1,p,foto): return og.slide(1,T,f'''<div class=k>{tag}</div><h1>{h1}</h1><div class=bar></div>
<div style="display:flex;align-items:flex-end;gap:36px"><p style="flex:1">{p}</p><div class=ph><img src="fotos/{foto}.jpg"></div></div>''',capa=True)
def ogb(i,h2,itens,p=''): return og.slide(i,T,f'<h2>{h2}</h2><div class=bar></div>{f"<p>{p}</p>" if p else ""}<div style="display:flex;flex-direction:column;gap:14px">{"".join(itens)}</div>')
def ogt(i,h2,p1,p2): return og.slide(i,T,f'<h2>{h2}</h2><div class=bar></div><p>{p1}</p><p><b>{p2}</b></p>')
D['OG_Reuniao']=('ottogurgel/2026-11-10-reuniao-segunda',[
 ogcapa('Gestão na prática','A reunião de segunda <i>em 30 minutos</i>','O roteiro que eu uso para o time sair sabendo <b>o que fazer.</b>','otto_15_polo_marinho'),
 ogt(2,'Reunião longa <i>não é reunião boa.</i>','Quando todo mundo fala de tudo, ninguém sai com uma tarefa.','Reunião boa é a que termina com dono e prazo.'),
 ogb(3,'Os primeiros <i>15 minutos.</i>',[og.num(1,'Números da semana · 5 min','o que bateu e o que não bateu, sem discurso'),og.num(2,'Prioridades · 10 min','três por pessoa, não dez')]),
 ogb(4,'Os últimos <i>15 minutos.</i>',[og.num(3,'Bloqueios · 10 min','o que está travando e quem destrava'),og.num(4,'Combinados · 5 min','quem faz o quê, até quando')]),
 ogb(5,'Três regras <i>que não mudam.</i>',[og.chk('Começa e termina no horário'),og.chk('Número antes de opinião'),og.chk('Toda tarefa sai com dono e prazo')]),
 og.slide(6,T,'<h2>Salve para a <i>próxima segunda.</i></h2><div class=bar></div><p>E me conta aqui: <b>quanto tempo dura a reunião do seu time hoje?</b></p>',foot=og.SIG_T.format(f='otto_14_polo_azul_claro')+'<span>Envie para seu time ↗</span>'),
])
D['OG_Indicadores']=('ottogurgel/2026-11-13-indicadores-meio',[
 ogcapa('Gestão comercial','Indicador de fim <i>chega tarde.</i>','Os números do meio que mostram o resultado <b>antes do fechamento.</b>','otto_12_polo_bege'),
 ogt(2,'Faturamento <i>é o placar.</i>','Quando ele aparece, o jogo já acabou.','Quem gere time precisa olhar o que vem antes.'),
 ogb(3,'O que olhar <i>todo dia.</i>',[og.num(1,'Contatos feitos por dia','o primeiro sinal de que o mês vai faltar'),og.num(2,'Propostas abertas há 7+ dias','dinheiro parado esperando retorno'),og.num(3,'Retorno do follow-up','quem respondeu e quem sumiu')]),
 ogb(4,'E mais <i>dois números.</i>',[og.num(4,'Reuniões marcadas','a agenda de hoje é a venda do mês que vem'),og.num(5,'Tempo de resposta ao lead','lead que espera esfria')]),
 ogb(5,'Em 2 minutos, <i>todo dia.</i>',[og.chk('Um painel só','sem planilha de 40 abas'),og.chk('Atualizado sozinho','ninguém monta relatório'),og.chk('Cada líder vê o seu time','e age no mesmo dia')]),
 og.slide(6,T,'''<h2>Quer o painel de <i>indicadores meio?</i></h2><div class=bar></div><p style="margin-bottom:-8px">Comente a palavra</p>
<div class=pill>PAINEL</div><p>e receba no direct o <b>checklist dos 5 números</b> que todo líder deveria olhar.</p>''',foot=og.SIG_T.format(f='otto_11_polo_preta')+'<span>Envie para seu time ↗</span>'),
])
D['OG_Frase12']=('ottogurgel/2026-11-12-frase',[og.slide(1,1,'<div class=quote>“</div><h1>Time sem rotina vira <i>time de desculpa.</i></h1><div class=bar></div><p>Rotina não é burocracia. É o que faz o resultado aparecer <b>sem depender de sorte.</b></p>',tag='Mentalidade')])
D['OG_Domingo15']=('ottogurgel/2026-11-15-perguntas',[og.slide(1,1,'<h2 style="font-size:72px;text-transform:uppercase;font-weight:800">3 perguntas antes <i>de segunda.</i></h2><div class=bar></div><div style="display:flex;flex-direction:column;gap:14px">'+og.num(1,'Qual é a única prioridade da semana?')+og.num(2,'O que eu preciso destravar para o time?')+og.num(3,'Qual número vou olhar todo dia?')+'</div><p>Responda hoje. <b>Segunda fica mais leve.</b></p>',tag='Domingo à noite')])
