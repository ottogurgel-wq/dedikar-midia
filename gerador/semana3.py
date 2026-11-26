"""Black Friday 27–30/11/2026. @dedikar.ia sem foto do Otto (visual institucional com telas reais)."""
from base import slide, num, chk
import base_og as og
from semana import T, bloco, ogcapa, ogb, ogt
from semana2_telas import TCSS

def tela_html(img, rotulo, maxh=None, w=None):
    mh = f' style="max-height:{maxh}px"' if maxh else ''
    ws = f' style="width:{w}px;align-self:center"' if w else ''
    return f'<div class=tela{ws}><div class=bar><b></b><b></b><b></b><span>{rotulo}</span></div><div class=im{mh}><img src="telas/{img}.webp"></div></div>'

def capa_inst(k, h1, p, img, rotulo, maxh=430):
    return f'''{TCSS}<div class=k>— {k}</div><h1 style="font-size:84px">{h1}</h1><p>{p}</p>{tela_html(img, rotulo, maxh)}'''

def tela(k, h2, img, rotulo, leg, maxh=None, w=None):
    return f'''{TCSS}<div class=k>— {k}</div><h2>{h2}</h2>{tela_html(img, rotulo, maxh, w)}<p class=leg>{leg}</p>'''

def cta_inst(h2, texto, foot):
    return slide(6, T, f'''<div class=k>— Diagnóstico gratuito</div><h2>{h2}</h2><div class=bar></div>
<p>{texto}</p>
<div class=pill style="font-size:44px;padding:22px 40px;letter-spacing:3px">Agende pelo link da bio</div>
<p style="font-size:30px;color:#9a9ca8">ou comente <b style="color:#fff">DIAGNÓSTICO</b> e receba o link no direct · dedikaria.com.br</p>''', foot=('@dedikar.ia · dedikaria.com.br', foot))

D = {}
D['BlackFriday'] = ('dedikar/2026-11-27-black-friday-cliente', [
 slide(1, T, capa_inst('Black Friday', 'O cliente de hoje<br><i>volta em janeiro?</i>', 'Promoção traz gente nova. <b>O que faz ela voltar é o que acontece depois.</b>', 'crm-dedikar', 'crm · início'), capa=True),
 slide(2, T, bloco('O que se perde', 'Venda boa,<br><i>cliente perdido.</i>', [num(1, 'Contato não registrado', 'comprou e ninguém sabe quem foi'), num(2, 'Nenhuma mensagem depois', 'nem obrigado, nem pós-venda'), num(3, 'Próxima compra ao acaso', 'ele só volta se lembrar de você')])),
 slide(3, T, bloco('Antes de vender', 'Prepare a casa<br><i>hoje.</i>', [chk('Todo contato entra no CRM', 'WhatsApp, loja e site no mesmo lugar'), chk('Resposta rápida no pico', 'o agente atende enquanto o time vende'), chk('Cada venda vira um próximo passo', 'tarefa de pós-venda criada sozinha')])),
 slide(4, T, tela('Na prática', 'Automações que<br><i>trabalham sozinhas.</i>', 'crm-dedikar-automacoes', 'crm · automações', 'Gatilho, condição e ação: lead novo, negócio parado, lembrete de reunião. Dados de demonstração.')),
 slide(5, T, bloco('Depois da promoção', 'A semana que vem<br><i>vale mais.</i>', [num(1, 'Agradecer em até 24 horas', 'mensagem curta, sem empurrar venda'), num(2, 'Perguntar como foi', 'quem responde está aberto a voltar'), num(3, 'Lembrar na hora certa', 'recompra, revisão, renovação')])),
 cta_inst('Quer o seu cliente <i>voltando?</i>', 'No <b>diagnóstico gratuito</b> a gente mostra onde o seu pós-venda está deixando dinheiro na mesa.', 'Envie para quem cuida das vendas'),
])
D['SiteVende'] = ('dedikar/2026-11-28-site-que-vende', [
 slide(1, T, capa_inst('Sites que vendem', 'Seu site vende<br><i>enquanto você dorme?</i>', 'Ou ele só mostra <b>endereço e telefone?</b>', 'site-locadora', 'site · locadora'), capa=True),
 slide(2, T, bloco('Site vitrine', 'O cliente entra<br><i>e sai.</i>', [num(1, 'Sem preço', 'ele precisa perguntar e desiste'), num(2, 'Sem como fechar', 'só um botão de WhatsApp que ninguém responde à noite'), num(3, 'Sem saber quem entrou', 'o contato não chega a lugar nenhum')])),
 slide(3, T, tela('Na prática · locadora', 'Reserva<br><i>em 4 passos.</i>', 'site-locadora-m', 'site · celular', 'Preço na hora, Pix ou cartão e o pedido direto para a equipe. Site em operação, feito pela Dedikar.', maxh=640, w=330)),
 slide(4, T, bloco('Site que vende', 'O que ele<br><i>precisa ter.</i>', [chk('Preço ou simulação na tela', 'sem precisar perguntar'), chk('Pedido ou reserva sem ligar', 'a qualquer hora'), chk('Contato direto no CRM', 'com origem e horário')])),
 slide(5, T, tela('E por trás do site', 'O dono atualiza<br><i>sozinho.</i>', 'portal-inicio', 'gestão · plataforma dedikar', 'Fotos, regras, locais e pedidos no mesmo painel da gestão, sem depender de agência.')),
 cta_inst('E o seu site, <i>vende?</i>', 'No <b>diagnóstico gratuito</b> a gente olha o seu site e mostra o que falta para ele trazer pedido.', 'Envie para o sócio'),
])
D['Novembro'] = ('dedikar/2026-11-30-fechamento-novembro', [
 slide(1, T, capa_inst('Fim do mês', 'Novembro fecha hoje.<br><i>Você sabe o resultado?</i>', 'Ou vai descobrir daqui a 15 dias, <b>quando o contador mandar?</b>', 'portal-financeiro', 'painel financeiro'), capa=True),
 slide(2, T, bloco('Fechar no dia', 'Os 4 números<br><i>do dia 1º.</i>', [num(1, 'Quanto entrou x quanto vendeu', 'venda não é dinheiro no caixa'), num(2, 'Quanto ficou para receber', 'e de quem'), num(3, 'O que saiu fora do previsto', 'a despesa que surpreendeu'), num(4, 'Quanto sobra em dezembro', 'com as contas já marcadas')])),
 slide(3, T, tela('Na prática', 'O fluxo<br><i>semana a semana.</i>', 'portal-fluxo', 'painel financeiro · fluxo', 'Entradas, saídas e saldo projetado, atualizados sozinhos. Valores ocultos.')),
 slide(4, T, tela('Operação', 'Custo<br><i>mês a mês.</i>', 'portal-frota-manut', 'painel · manutenção', 'Custo médio, avarias e ordens de serviço por mês, sem montar planilha. Valores ocultos.')),
 slide(5, T, bloco('Dezembro', 'Comece o mês<br><i>com o painel.</i>', [chk('Números atualizados sozinhos', 'sem ninguém digitar'), chk('Mesmo critério todo mês', 'dá para comparar de verdade'), chk('Decisão no dia 1º', 'e não no dia 15')])),
 cta_inst('Quer fechar dezembro <i>no dia?</i>', 'No <b>diagnóstico gratuito</b> a gente mostra o que dá para automatizar no seu fechamento.', 'Envie para o financeiro'),
])
# ---------- @ottogurgel.ofc ----------
D['OG_VenderValor'] = ('ottogurgel/2026-11-27-vender-valor', [
 ogcapa('Black Friday', 'Vender no desconto é fácil. <i>Difícil é vender o valor.</i>', 'O que eu ensino ao time <b>na semana em que todo mundo baixa o preço.</b>', 'otto_13_blazer_polo_verde'),
 ogt(2, 'Desconto <i>não é argumento.</i>', 'Ele só diz ao cliente quanto o produto vale menos.', 'Valor é o que ele resolve.'),
 ogb(3, 'O que eu <i>ensino.</i>', [og.num(1, 'Pergunte antes de oferecer', 'o que o cliente precisa resolver'), og.num(2, 'Mostre o que ele ganha', 'em tempo, dinheiro ou tranquilidade')]),
 ogb(4, 'E na <i>negociação.</i>', [og.num(3, 'Desconto com contrapartida', 'à vista, volume ou prazo maior'), og.num(4, 'Combine o próximo passo', 'quem compra hoje precisa ouvir de você amanhã')]),
 ogb(5, 'Cuidado <i>com.</i>', [og.chk('Prometer o que a operação não entrega'), og.chk('Dar desconto para quem já ia comprar'), og.chk('Esquecer o cliente depois do pagamento')]),
 og.slide(6, T, '<h2>Salve e mande <i>para o seu time.</i></h2><div class=bar></div><p>E me conta: na sua empresa, <b>desconto é ferramenta ou muleta?</b></p>', foot=og.SIG_T.format(f='otto_15_polo_marinho') + '<span>Envie para seu time ↗</span>'),
])
D['OG_Frase28'] = ('ottogurgel/2026-11-28-frase', [og.slide(1, 1, '<div class=quote>“</div><h1>Cliente não compra preço. <i>Compra segurança.</i></h1><div class=bar></div><p>O preço só vira o assunto <b>quando faltou confiança.</b></p>', tag='Vendas')])
D['OG_Domingo29'] = ('ottogurgel/2026-11-29-melhor-venda', [og.slide(1, 1, '<h2 style="font-size:72px;text-transform:uppercase;font-weight:800">Qual foi a sua melhor venda <i>de novembro?</i></h2><div class=bar></div><p>Escreva os 3 motivos que fizeram ela dar certo.</p><p><b>E repita em dezembro.</b></p>', tag='Domingo à noite')])
