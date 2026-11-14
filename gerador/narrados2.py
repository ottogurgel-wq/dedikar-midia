import sys
from reel_narrado import fazer
st=lambda n,txt:f'<div class="chip st"><u>{n}</u>{txt}</div>'
def fim(pal,txt,site=True): return dict(t=f'Comente {pal}',html=f'<div class=p style="margin-bottom:-14px">Comente a palavra</div><div class=pill>{pal}</div><div class=p>{txt}</div>'+('<div class=k style="margin-top:20px">dedikaria.com.br</div>' if site else ''),sfx='riser_suave')
J={
'Orcamento':('dedikar','voz/2026-11-17_orcamento',[
 dict(t=0,html='<div class=k>— Pergunta rápida</div><div class=h>Quantos orçamentos você <i>mandou este mês?</i></div>'),
 dict(t='E quantos',html='<div class=h>E quantos alguém <i>cobrou de volta?</i></div>',sfx='impacto_titulo'),
 dict(t='O cliente diz',html='<div class=k>— O cliente</div><div class=h>“Vou <i>pensar.</i>”</div><div class=p>E a conversa <b>morre ali.</b></div>'),
 dict(t='Não porque',html='<div class=p>Não porque ele desistiu.</div><div class=h>Ninguém voltou a <i>falar com ele.</i></div>'),
 dict(t='Orçamento sem',html='<div class=h>Não é venda perdida.<br><i>É venda esquecida.</i></div>',sfx='impacto_titulo'),
 dict(t='Um sistema',html='<div class=k>— Com sistema</div>'+st(1,'Avisa quem precisa de retorno')+st(2,'Avisa quando')+st(3,'O seu time só responde')),
 fim('DIAGNÓSTICO','e receba o link do <b>diagnóstico gratuito.</b>'),
]),
'ListaParada':('dedikar','voz/2026-11-18_lista_parada',[
 dict(t=0,html='<div class=k>— Venda mais barata</div><div class=h>É para quem <i>já comprou de você.</i></div>'),
 dict(t='Mas na',html='<div class=h>Mas essa lista está <i>parada.</i></div><div class=p>Nome e telefone numa planilha <b>que ninguém abre.</b></div>'),
 dict(t='Ninguém lembra',html='<div class=k>— Ninguém lembra</div>'+st(1,'Da recompra')+st(2,'Da revisão')+st(3,'Da data especial')),
 dict(t='Um sistema',html='<div class=h>O cliente certo,<br><i>na hora certa.</i></div><div class=p>Com a <b>mensagem certa.</b> Sem depender da memória de ninguém.</div>'),
 fim('AUTOMATIZAR','e escolha o dia do seu <b>diagnóstico gratuito.</b>'),
]),
'Governanca':('dedikar','voz/2026-11-19_governanca',[
 dict(t=0,html='<div class=k>— Antes de ligar a IA</div><div class=h>Responda <i>três perguntas.</i></div>'),
 dict(t='Quem é o dono',html='<div class=k>— Pergunta 1</div><div class=h>Quem é o dono <i>dessa IA?</i></div>'),
 dict(t='O que ela',html='<div class=k>— Pergunta 2</div><div class=h>O que ela responde <i>sozinha?</i></div><div class=p>E o que tem que <b>passar por uma pessoa.</b></div>'),
 dict(t='E quem revisa',html='<div class=k>— Pergunta 3</div><div class=h>Quem revisa <i>o que ela fez?</i></div>'),
 dict(t='IA sem regra',html='<div class=h>IA sem regra é contratar sem dizer <i>o que pode prometer.</i></div>',sfx='impacto_titulo'),
 fim('GOVERNANÇA','e receba o <b>checklist</b> para responder antes de ligar a IA.'),
]),
'Prompts':('dedikar','voz/2026-11-20_prompts',[
 dict(t=0,html='<div class=k>— IA no dia a dia</div><div class=h>Resposta genérica?<br><i>Olhe o pedido.</i></div>'),
 dict(t='Diga quem',html='<div class=k>— Um bom pedido tem</div>'+st(1,'Quem ela é')+st(2,'O que você precisa')+st(3,'Para quem é')+st(4,'Como quer a resposta')),
 dict(t='Em vez de',html='<div class=k>— Em vez de</div><div class=p><s>“Escreve uma cobrança.”</s></div>'),
 dict(t='peça',html='<div class=k>— Peça assim</div><div class=p><b>“Você é do financeiro de uma loja. Escreva uma mensagem educada para um cliente com boleto vencido há cinco dias, em três linhas, com o link de pagamento no final.”</b></div>'),
 fim('PROMPTS','e receba o <b>guia com seis pedidos prontos.</b>'),
]),
'Cobranca':('dedikar','voz/2026-11-21_cobranca',[
 dict(t=0,html='<div class=k>— Financeiro</div><div class=h>Vergonha <i>de cobrar?</i></div>'),
 dict(t='E o dinheiro',html='<div class=h>O dinheiro fica parado <i>no bolso do cliente.</i></div>'),
 dict(t='Cobrança boa',html='<div class=h>Cobrança não é bronca.<br><i>É lembrete no tempo certo.</i></div>',sfx='impacto_titulo'),
 dict(t='Antes de vencer',html='<div class=k>— A régua</div>'+st(1,'Antes de vencer: um aviso')+st(2,'No dia: o link de pagamento')+st(3,'Depois: mensagem educada')+st(4,'Só então: uma pessoa liga')),
 dict(t='Isso é',html='<div class=h>Régua de cobrança.<br><i>Roda sozinha.</i></div>'),
 fim('CAIXA','e receba a <b>planilha</b> para ver o que vai entrar nas próximas semanas.'),
]),
'CobrarResultado':('og','voz/2026-11-21_cobrar_resultado_otto',[
 dict(t=0,html='<div class=k>Gestão de pessoas</div><div class=h>Cobrar resultado <i>não é dar bronca.</i></div>'),
 dict(t='Primeiro',html='<div class=k>Passo 1</div><div class=h>Combine <i>antes.</i></div><div class=p>O <b>número</b> e o <b>prazo.</b></div>'),
 dict(t='Segundo',html='<div class=k>Passo 2</div><div class=h>Acompanhe <i>no caminho.</i></div><div class=p>E não só no fim do mês.</div>'),
 dict(t='Terceiro',html='<div class=k>Passo 3</div><div class=h>Pergunte <i>o que travou.</i></div><div class=p>Antes de dizer <b>o que você acha.</b></div>'),
 dict(t='Cobrança que',html='<div class=p>Cobrança que chega no fim <b>vira susto.</b></div><div class=h>A que acompanha <i>vira resultado.</i></div>',sfx='impacto_titulo'),
 dict(t='Salva aí',html='<div class=h>Salve e me conta:</div><div class=p><b>Como você cobra o seu time hoje?</b></div>',sfx='riser_suave'),
]),
}
if __name__=="__main__":
 for n in sys.argv[1:] or list(J):
    tema,voz,c=J[n]; fazer(n,tema,voz,c)
