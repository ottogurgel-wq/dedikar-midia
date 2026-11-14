"""Telas reais (anonimizadas) nos carrosséis da semana 17–23/11 (pedido do Otto em 14/11)."""
from base import slide, num, chk
from semana import T
import semana2
TCSS='''<style>.tela{position:relative;border:2px solid rgba(56,217,236,.45);border-radius:20px;overflow:hidden;background:#0d0f16;box-shadow:0 0 70px rgba(56,217,236,.22),0 20px 60px rgba(0,0,0,.55)}
.tela .bar{height:34px;background:#141722;display:flex;align-items:center;gap:9px;padding:0 16px;border-bottom:1px solid rgba(255,255,255,.07)}
.tela .bar b{width:12px;height:12px;border-radius:50%;background:#2c3040}.tela .bar span{margin-left:12px;font:500 17px 'JetBrains Mono';color:#7d8193;letter-spacing:1px}
.tela .im{overflow:hidden}.tela img{display:block;width:100%;transform-origin:30% 20%;animation:kb 9s ease-in-out both}
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.07)}}
.leg{font-size:26px!important;color:#9a9ca8!important;margin-top:-6px}</style>'''
def tela(k,h2,img,rotulo,leg,itens=None):
    extra=f'<div style="display:flex;flex-direction:column;gap:12px">{"".join(itens)}</div>' if itens else ''
    return f'''{TCSS}<div class=k>— {k}</div><h2>{h2}</h2>
<div class=tela><div class=bar><b></b><b></b><b></b><span>{rotulo}</span></div><div class=im><img src="telas/{img}.webp"></div></div>
<p class=leg>{leg}</p>{extra}'''
D=semana2.D
# Portfólio: telas reais nos slides 2 a 5
p,S=D['Portfolio']
S[1]=slide(2,T,tela('Locadora','Portal <i>de gestão.</i>','portal-inicio','gestão · plataforma dedikar','Financeiro, frota, site e CRM numa entrada só. Tela real, dados protegidos.'))
S[2]=slide(3,T,tela('Locadora · financeiro','Saldo projetado <i>dia a dia.</i>','portal-financeiro','painel financeiro','Caixa de hoje, a receber, a pagar e o saldo dos próximos meses. Valores ocultos.'))
S[3]=slide(4,T,tela('Pousada','Receita × <i>caixa.</i>','pousada','painel financeiro · pousada','Ocupação, diária média, canais de venda e auditoria entre maquininha, banco e reservas.'))
S[4]=slide(5,T,tela('Comercial','Dedikar <i>CRM.</i>','crm-dedikar','crm · início','Receita, vendas, funil e o que pede atenção agora, numa tela. Dados de demonstração.'))
# Desconto: a regra de alçada no precificador real
p,S=D['Desconto']
S[4]=slide(5,T,tela('Com sistema','Alçada de desconto <i>na tela.</i>','precificador','precificador · locadora','O vendedor vê até onde pode ir. Acima da alçada, o pedido vai para aprovação.'))
# Receita: o painel que mostra o dinheiro voltando
p,S=D['Receita']
S[4]=slide(5,T,tela('Como estancar','Medir, atacar <i>e acompanhar.</i>','portal-fluxo','painel financeiro · fluxo','Um painel como este mostra, semana a semana, o dinheiro que entra e o que ficou para trás.'))
# Sexta: o fechamento já pronto
p,S=D['Sexta']
S[4]=slide(5,T,tela('Com sistema','O resumo já <i>vem pronto.</i>','portal-frota-mes','painel · mês a mês','Os números da semana e do mês reunidos sozinhos. Você só decide o que fazer na segunda.'))
