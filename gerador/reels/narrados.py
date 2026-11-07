import sys
from reel_narrado import fazer
st=lambda n,txt:f'<div class="chip st"><u>{n}</u>{txt}</div>'
J={
'LeadEsfriou':('dedikar','voz/2026-11-13_lead_esfriou',[
 dict(t=0,html='<div class=k>— Atendimento</div><div class=big><i>19h</i></div><div class=h>Seu cliente mandou mensagem.</div>'),
 dict(t='Ninguém respondeu',html='<div class=h>Ninguém <i>respondeu.</i></div><div class=p>A mensagem ficou lá. <b>A noite toda.</b></div>'),
 dict(t='No dia seguinte',html='<div class=k>— Dia seguinte, 9h</div><div class=h>Ele já tinha <i>fechado com outro.</i></div>'),
 dict(t='Isso não é',html='<div class=h>Não é falta de vontade.<br><i>É falta de sistema.</i></div>'),
 dict(t='Um agente de',html='<div class=k>— Um agente de IA</div>'+st(1,'Responde na hora')+st(2,'Faz as perguntas certas')+st(3,'Passa ao vendedor só quem está pronto')),
 dict(t='E nada sai',html='<div class=h>Nada sai sem<br><i>a sua regra.</i></div><div class=p>O agente executa. <b>Quem decide é você.</b></div>'),
 dict(t='Comente AGENTE',html='<div class=p style="margin-bottom:-14px">Comente a palavra</div><div class=pill>AGENTE</div><div class=p>e a gente te mostra no direct <b>como montar o seu.</b></div><div class=k style="margin-top:20px">dedikaria.com.br</div>',sfx='riser_suave'),
]),
'Feedback':('og','voz/2026-11-14_feedback_otto',[
 dict(t=0,html='<div class=k>Gestão de pessoas</div><div class=h>Feedback que corrige <i>sem desmotivar.</i></div>'),
 dict(t='Primeiro',html='<div class=k>Passo 1</div><div class=h>Fale do fato, <i>não da pessoa.</i></div><div class=p><s>“Você é desorganizado.”</s><br><b>“O relatório chegou 2 dias depois.”</b></div>'),
 dict(t='Segundo',html='<div class=k>Passo 2</div><div class=h>Mostre <i>o impacto.</i></div><div class=p>O que esse atraso <b>causou no time.</b></div>'),
 dict(t='Terceiro',html='<div class=k>Passo 3</div><div class=h>Combine <i>o próximo passo.</i></div><div class=p>Com <b>prazo</b>.</div>'),
 dict(t='E termine',html='<div class=k>E termine perguntando</div><div class=h>“Do que você precisa <i>de mim?</i>”</div>'),
 dict(t='Feedback bom',html='<div class=h>Feedback não é bronca.<br><i>É direção.</i></div>'),
 dict(t='Salve e use',html='<div class=h>Salve para a <i>próxima conversa.</i></div><div class=p>E envie para quem lidera time com você.</div>',sfx='riser_suave'),
]),
}
if __name__=="__main__":
 for n in sys.argv[1:] or list(J):
    tema,voz,c=J[n]; fazer(n,tema,voz,c)
