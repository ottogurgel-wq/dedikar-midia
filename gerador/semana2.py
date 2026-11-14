"""Semana 17–23/11/2026 (validada pelo Otto em 14/11)."""
import base, base_og
from base import slide, num, chk
from semana import T, ph, capa, bloco, cta, og, ogcapa, ogb, ogt
D={}
D['Receita']=('dedikar/2026-11-17-receita-vaza',[
 slide(1,T,capa('Receita que vaza','Sua empresa perde dinheiro<br><i>todo mês.</i>','Não é no grande prejuízo. É no <b>pequeno vazamento que ninguém mede.</b>','otto_02_blazer_cinza_claro',84),capa=True),
 slide(2,T,bloco('Os mais comuns','Onde o dinheiro<br><i>escapa.</i>',[num(1,'Orçamento enviado e nunca cobrado','o cliente pensou e ninguém retomou'),num(2,'Conta a receber que atrasou em silêncio','descoberta só no fim do mês'),num(3,'Cliente que comprou e não voltou','ninguém chamou de novo')])),
 slide(3,T,bloco('Continue contando','E mais<br><i>dois.</i>',[num(4,'Desconto dado sem regra','cada um decide o seu'),num(5,'Retrabalho por informação perdida','pedido refeito, entrega errada')])),
 slide(4,T,bloco('Por que ninguém vê','Pequeno, espalhado<br><i>e sem dono.</i>',[chk('Cada vazamento é pequeno','sozinho, não assusta'),chk('Fica espalhado','WhatsApp, planilha e caderno'),chk('Ninguém é dono','então ninguém mede')])),
 slide(5,T,bloco('Como estancar','Primeiro medir,<br><i>depois resolver.</i>',[num(1,'Medir em reais','quanto cada vazamento custa por mês'),num(2,'Atacar o maior primeiro','um de cada vez'),num(3,'Acompanhar num painel','para ver o dinheiro voltando')])),
 cta('otto_04_blazer_azul_estrategia','Quanto vaza <i>na sua empresa?</i>','RECEITA','e eu te mando no direct o <b>checklist dos 5 vazamentos</b> para medir cada um em reais.','Envie para o sócio'),
])
D['Desconto']=('dedikar/2026-11-19-desconto-sem-regra',[
 slide(1,T,capa('Alerta ao empresário','Desconto sem regra é<br><i>lucro sem dono.</i>','Cada vendedor decide o seu. No fim do mês, <b>ninguém sabe quanto saiu.</b>','otto_03_blazer_grafite_escritorio',86),capa=True),
 slide(2,T,bloco('Onde escapa','O desconto<br><i>que ninguém vê.</i>',[num(1,'Desconto para fechar rápido','e o cliente aprende a pedir sempre'),num(2,'Brinde que não entra na conta','frete, taxa, um item a mais'),num(3,'Condição especial que virou padrão','e ninguém lembra por quê')])),
 slide(3,T,'''<div class=k>— Faça a conta</div><h2>Parece pouco.<br><i>Não é.</i></h2>
<div class=big><div class=v><span class=g data-count=25 data-at=1.6>25</span>% do lucro</div><div class=l>é o que <b style="color:#fff">5% de desconto</b> levam de uma venda com margem de 20%.</div></div>
<p>Exemplo ilustrativo: a margem cai de 20% para 15% do preço.</p>'''),
 slide(4,T,bloco('A regra que protege','Desconto com<br><i>critério.</i>',[chk('Faixa por vendedor','acima disso, precisa de aprovação'),chk('Todo desconto registrado','com o motivo'),chk('Relatório da semana','quanto saiu e para quem')])),
 slide(5,T,bloco('Com sistema','Sem<br><i>burocracia.</i>',[num(1,'O vendedor pede pelo sistema','na hora da negociação'),num(2,'Você aprova pelo celular','em um toque'),num(3,'O painel mostra o mês','quanto de desconto saiu')])),
 cta('otto_05_blazer_azul_pessoas','Quanto o desconto <i>custa aí?</i>','DIAGNÓSTICO','e eu te mando o link do <b>diagnóstico gratuito</b> para a gente medir junto.','Envie para quem vende'),
])
D['Sexta']=('dedikar/2026-11-20-fechamento-sexta',[
 slide(1,T,capa('Rotina de sexta','A semana não acaba.<br><i>Ela é fechada.</i>','15 minutos na sexta evitam <b>a segunda começando no susto.</b>','otto_13_blazer_polo_verde',88),capa=True),
 slide(2,T,bloco('Passo 1','O que<br><i>entrou.</i>',[num(1,'Vendas e recebimentos da semana','comparados com a meta'),num(2,'O que ficou para receber','com data e responsável')])),
 slide(3,T,bloco('Passo 2','O que ficou<br><i>aberto.</i>',[num(3,'Propostas sem resposta','quem retoma na segunda'),num(4,'Problema de cliente','o que precisa de decisão sua')])),
 slide(4,T,bloco('Passo 3','A primeira tarefa<br><i>de segunda.</i>',[chk('Uma só','escrita, não na cabeça'),chk('Com responsável','quem faz'),chk('Com horário','quando começa')])),
 slide(5,T,bloco('Com sistema','O resumo já<br><i>vem pronto.</i>',[chk('Chega sozinho no WhatsApp','sexta à tarde'),chk('Nada depende da memória','vendas, contas e propostas juntas'),chk('Você só decide','o que fazer na segunda')])),
 cta('otto_01_terno_fundo_preto','Quer o modelo de <i>fechamento?</i>','SEXTA','e eu te mando no direct o <b>modelo</b> para usar toda sexta.','Envie para o seu gerente'),
])
D['Portfolio']=('dedikar/2026-11-23-portfolio',[
 slide(1,T,capa('Portfólio','O que a Dedikar<br><i>já entregou.</i>','Sistemas rodando hoje em empresas de Pernambuco. <b>Sem nome de cliente.</b>','otto_05_blazer_azul_pessoas',90),capa=True),
 slide(2,T,bloco('Locadora','Portal<br><i>de gestão.</i>',[chk('Financeiro, frota e site','no mesmo lugar'),chk('Saldo projetado','e as contas da semana'),chk('No servidor do próprio cliente','os dados ficam com ele')])),
 slide(3,T,bloco('Pousada','Agente<br><i>de reservas.</i>',[chk('Responde o hóspede','no WhatsApp, a qualquer hora'),chk('Fecha a reserva com Pix','sem ninguém digitar'),chk('Pedido fora da regra','vai para uma pessoa')])),
 slide(4,T,bloco('Comercial','Dedikar<br><i>CRM.</i>',[chk('Funil, tarefas e WhatsApp','numa tela só'),chk('Lead do Instagram','entra sozinho'),chk('Agentes de follow-up','ninguém fica sem retorno')])),
 slide(5,T,bloco('Em comum','O jeito<br><i>de entregar.</i>',[num(1,'Começa por um diagnóstico','antes de falar em sistema'),num(2,'Entrega por etapa','cada uma funcionando'),num(3,'Resultado medido','o dono vê o que mudou')])),
 cta('otto_04_blazer_azul_estrategia','E o seu, <i>qual seria?</i>','PROJETO','e escolha o dia do <b>diagnóstico gratuito</b> para a gente desenhar o seu.','Envie para o sócio'),
])
# ---------- @ottogurgel.ofc ----------
D['OG_UmAUm']=('ottogurgel/2026-11-17-conversa-1a1',[
 ogcapa('Gestão comercial','15 minutos por semana <i>com cada vendedor.</i>','A conversa que eu uso para desenvolver o time <b>sem esperar o fim do mês.</b>','otto_14_polo_azul_claro'),
 ogt(2,'Reunião em grupo <i>não desenvolve ninguém.</i>','Nela, cada um esconde a dificuldade que tem.','No individual, aparece o que trava de verdade.'),
 ogb(3,'O roteiro, <i>parte 1.</i>',[og.num(1,'Como foi a semana?','deixe ele falar primeiro'),og.num(2,'Um número para olhar junto','o que melhorou e o que caiu')]),
 ogb(4,'O roteiro, <i>parte 2.</i>',[og.num(3,'Uma dificuldade','e o que ele já tentou'),og.num(4,'Um compromisso','uma ação para a próxima semana')]),
 ogb(5,'Três <i>cuidados.</i>',[og.chk('Mesmo dia e horário toda semana'),og.chk('Não vira cobrança de meta'),og.chk('Anote e retome na seguinte')]),
 og.slide(6,T,'''<h2>Quer o roteiro <i>para imprimir?</i></h2><div class=bar></div><p style="margin-bottom:-8px">Comente a palavra</p>
<div class=pill>ROTEIRO</div><p>e receba no direct o <b>roteiro da conversa 1:1</b> com as perguntas prontas.</p>''',foot=og.SIG_T.format(f='otto_15_polo_marinho')+'<span>Envie para seu gestor ↗</span>'),
])
D['OG_VendedorNovo']=('ottogurgel/2026-11-20-vendedor-novo',[
 ogcapa('Gestão de pessoas','Vendedor novo <i>não aprende sozinho.</i>','O que eu faço no primeiro mês para ele vender <b>sem queimar cliente.</b>','otto_11_polo_preta'),
 ogt(2,'Jogar no campo <i>custa caro.</i>','Sem preparo, ele aprende errando com o seu cliente.','E o cliente não volta.'),
 ogb(3,'Semanas <i>1 e 2.</i>',[og.num(1,'Acompanha quem vende bem','ouve antes de falar'),og.num(2,'Estuda produto e objeções','com perguntas reais dos clientes')]),
 ogb(4,'Semanas <i>3 e 4.</i>',[og.num(3,'Atende com alguém do lado','feedback no mesmo dia'),og.num(4,'Assume a própria carteira','com meta de atividade, não de venda')]),
 ogb(5,'O que eu meço <i>no primeiro mês.</i>',[og.chk('Contatos feitos'),og.chk('Qualidade da conversa'),og.chk('Pedido de ajuda: quem pede aprende mais rápido')]),
 og.slide(6,T,'<h2>Salve para o próximo <i>que você contratar.</i></h2><div class=bar></div><p>E me conta: <b>quanto tempo leva hoje para um vendedor novo fazer a primeira venda?</b></p>',foot=og.SIG_T.format(f='otto_12_polo_bege')+'<span>Envie para o RH ↗</span>'),
])
D['OG_Frase19']=('ottogurgel/2026-11-19-frase',[og.slide(1,1,'<div class=quote>“</div><h1>Meta sem acompanhamento <i>é só desejo.</i></h1><div class=bar></div><p>O que faz a meta acontecer é olhar o caminho <b>toda semana.</b></p>',tag='Mentalidade')])
D['OG_Domingo22']=('ottogurgel/2026-11-22-conversa-adiada',[og.slide(1,1,'<h2 style="font-size:76px;text-transform:uppercase;font-weight:800">Qual conversa você está <i>adiando?</i></h2><div class=bar></div><p>Com um vendedor, um sócio, um cliente.</p><p>Adiar não resolve: só deixa mais difícil. <b>Marque para esta semana.</b></p>',tag='Domingo à noite')])
