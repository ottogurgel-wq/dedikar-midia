from reel_narrado import fazer_story
def s(k,h): return f'<div class=k>— {k}</div><div class=h>{h}</div><div class="chip st"><u>→</u>Diagnóstico gratuito no link da bio</div><div class=p>dedikaria.com.br</div>'
S={
'1127':s('Black Friday','Quantos contatos de hoje vão estar <i>no seu CRM amanhã?</i>'),
'1128':s('Sábado','Seu site fecha venda às 23h ou <i>só mostra o telefone?</i>'),
'1129':s('Domingo','Quantas empresas a sua equipe <i>procurou esta semana?</i>'),
'1130':s('Fim do mês','Novembro fechou. <i>Você já sabe quanto sobrou?</i>'),
}
for n,c in S.items(): fazer_story(n,'dedikar',c)
