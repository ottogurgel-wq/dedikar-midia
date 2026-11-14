from reel_narrado import fazer_story
def s(k,h,pal): return f'<div class=k>— {k}</div><div class=h>{h}</div><div class="chip st"><u>💬</u>Comenta {pal} no post de hoje</div><div class=p>e o link chega no seu direct.</div>'
S={
'1117':s('Pergunta do dia','Quanto a sua empresa perdeu este mês <i>sem perceber?</i>','RECEITA'),
'1118':s('Clientes antigos','Quem foi o último cliente que você chamou <i>sem ele pedir?</i>','AUTOMATIZAR'),
'1119':s('Alerta ao empresário','Se o vendedor der desconto hoje, <i>você fica sabendo quando?</i>','DIAGNÓSTICO'),
'1120':s('Sexta-feira','Qual proposta ficou <i>sem resposta esta semana?</i>','SEXTA'),
'1121':s('Financeiro','Seu cliente paga em dia porque quer ou <i>porque alguém lembrou?</i>','CAIXA'),
'1123':s('Segunda-feira','Qual tarefa repetida você vai tirar <i>da sua equipe este mês?</i>','PROJETO'),
}
for n,c in S.items(): fazer_story(n,'dedikar',c)
