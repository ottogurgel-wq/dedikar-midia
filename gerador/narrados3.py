import sys
from reel_narrado import fazer
T='file:///home/claude/car/telas/'
st=lambda n,txt:f'<div class="chip st"><u>{n}</u>{txt}</div>'
def img(f,rot,h=560): return (f'<div style="border:2px solid rgba(56,217,236,.45);border-radius:18px;overflow:hidden;box-shadow:0 0 60px rgba(56,217,236,.25);margin-top:10px">'
    f'<div style="height:30px;background:#141722;font:500 16px JetBrains Mono;color:#7d8193;padding:6px 14px">● ● ●&nbsp;&nbsp;{rot}</div>'
    f'<div style="max-height:{h}px;overflow:hidden"><img src="{T}{f}.webp" style="width:100%;display:block"></div></div>')
def fim(txt): return dict(t='Agende',html=f'<div class=k>— Diagnóstico gratuito</div><div class=h>Agende pelo <i>link da bio.</i></div><div class=p>{txt}</div><div class=k style="margin-top:20px">dedikaria.com.br</div>',sfx='riser_suave')
J={
'BFPico':('dedikar','voz/2026-11-27_bf_pico',[
 dict(t=0,html='<div class=k>— Black Friday</div><div class=h>O dia em que o WhatsApp <i>mais toca.</i></div>'),
 dict(t='E também',html='<div class=h>E em que mais cliente <i>fica sem resposta.</i></div>',sfx='impacto_titulo'),
 dict(t='Quem responde',html='<div class=h>Quem responde primeiro, <i>vende.</i></div>'),
 dict(t='Um agente',html='<div class=k>— Agente de IA</div>'+st(1,'Atende na hora')+st(2,'Tira as dúvidas comuns')+st(3,'Passa ao vendedor quem está pronto')),
 dict(t='E todo contato',html='<div class=k>— Tudo registrado</div>'+img('crm-dedikar-automacoes','crm · automações',520)+'<div class=p>Pós-venda sem depender da memória de ninguém.</div>'),
 fim('A gente mostra onde o seu atendimento perde venda.'),
]),
'Bastidores':('dedikar','voz/2026-11-28_bastidores',[
 dict(t=0,html='<div class=k>— Bastidores</div><div class=h>Como a Dedikar <i>entrega um sistema?</i></div>'),
 dict(t='Começa',html='<div class=k>— Etapa 1</div><div class=h>Começa por um <i>diagnóstico.</i></div><div class=p>Onde a operação perde <b>tempo e dinheiro.</b></div>'),
 dict(t='Depois',html='<div class=k>— Etapa 2</div><div class=h>A solução <i>por etapas.</i></div><div class=p>Primeiro a que dá <b>retorno mais rápido.</b></div>'),
 dict(t='Cada etapa',html='<div class=k>— Etapa 3</div><div class=h>Entra <i>funcionando.</i></div><div class=p>Com o seu time usando.</div>'+img('portal-inicio','gestão · plataforma dedikar',430)),
 dict(t='E no fim',html='<div class=k>— Etapa 4</div><div class=h>Um painel mostra <i>o que mudou.</i></div>'+img('portal-financeiro','painel financeiro',430)),
 dict(t='Sem trocar',html='<div class=h>Sem trocar tudo <i>de uma vez.</i></div>',sfx='impacto_titulo'),
 fim('O primeiro passo é entender a sua operação.'),
]),
'Orion':('dedikar','voz/2026-11-29_orion',[
 dict(t=0,html='<div class=k>— Prospecção</div><div class=h>Sua empresa só vende <i>para quem chega?</i></div>'),
 dict(t='Prospectar',html='<div class=k>— Prospectar dá trabalho</div>'+st(1,'Achar a empresa certa')+st(2,'O contato certo')+st(3,'Mandar a mensagem')+st(4,'Cobrar a resposta')),
 dict(t='O Orion',html='<div class=k>— Orion, da Dedikar</div>'+img('orion-hoje','orion · hoje · dados de demonstração',480)),
 dict(t='e separa',html='<div class=k>— Quem respondeu</div>'+img('orion-respostas','orion · respostas · dados de demonstração',480)),
 dict(t='O vendedor',html='<div class=h>O vendedor só entra <i>quando tem conversa.</i></div>',sfx='impacto_titulo'),
 fim('A gente mostra como montar a sua prospecção.'),
]),
'FechaMes':('og','voz/2026-11-30_fecha_mes_otto',[
 dict(t=0,html='<div class=k>Gestão de time</div><div class=h>Último dia <i>do mês.</i></div>'),
 dict(t='Antes de fechar',html='<div class=h>Dez minutos <i>com o seu time.</i></div>'),
 dict(t='O que deu',html='<div class=k>Pergunta 1</div><div class=h>O que deu certo <i>em novembro?</i></div>'),
 dict(t='O que a gente',html='<div class=k>Pergunta 2</div><div class=h>O que a gente <i>não vai repetir?</i></div>'),
 dict(t='E qual',html='<div class=k>Pergunta 3</div><div class=h>Qual é a primeira coisa <i>de dezembro?</i></div>'),
 dict(t='Mês que começa',html='<div class=p>Anota e manda para todo mundo.</div><div class=h>Mês que começa com combinado <i>começa na frente.</i></div>',sfx='impacto_titulo'),
 dict(t='Salva aí',html='<div class=h>Salve e me conta:</div><div class=p><b>Você fecha o mês com o time ou sozinho?</b></div>',sfx='riser_suave'),
]),
}
if __name__=="__main__":
 for n in sys.argv[1:] or list(J):
    tema,voz,c=J[n]; fazer(n,tema,voz,c)
