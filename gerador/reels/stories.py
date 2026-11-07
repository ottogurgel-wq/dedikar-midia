from reel_narrado import fazer_story
def s(k,h,p,pal): return f'<div class=k>— {k}</div><div class=h>{h}</div><div class="chip st"><u>💬</u>Comenta {pal} no post de hoje</div><div class=p>e o link chega no seu direct.</div>'
S={
'1110':s('Pergunta rápida','Quantas horas a sua equipe perde <i>em tarefa repetida?</i>','','AUTOMATIZAR'),
'1111':s('Carpina e região','O cliente das 19h <i>ainda está esperando?</i>','','AUTOMATIZAR'),
'1112':s('Teste de 30 segundos','Sua operação está <i>quente ou fria?</i>','','DIAGNÓSTICO'),
'1113':s('Financeiro','Você sabe o caixa <i>de daqui a 30 dias?</i>','','CAIXA'),
'1114':s('A pergunta que eu mais ouço','“A IA vai <i>me substituir?</i>”','','DIAGNÓSTICO'),
'1116':s('Agentes de IA','Um agente que <i>não decide sozinho.</i>','','AGENTE'),
}
for n,c in S.items(): fazer_story(n,'dedikar',c)
