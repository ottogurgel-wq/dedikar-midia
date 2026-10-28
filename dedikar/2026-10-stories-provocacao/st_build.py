"""Stories automáticos 28/10–08/11 · provocação (12h) + oferta (19h) + domingo. Sem figurinha (publicados pela API)."""
src=open('cx_build.py').read(); exec(src[:src.index('\nS={}')])
K=lambda s,c='#38d9ec': f'<div style="font:500 28px \'JetBrains Mono\';letter-spacing:4px;color:{c};text-transform:uppercase">{s}</div>'
TOPS='<div style="display:flex;align-items:center;justify-content:space-between"><div class="br"><div class="tile"><img src="logo.png"></div><div class="brand">Dedikar <span>IA</span></div></div><div class="cnt">@dedikar.ia</div></div>'
def cta(palavra,onde):
    return f'''<div style="border:2.5px solid #38d9ec;border-radius:28px;padding:34px 36px;background:linear-gradient(90deg,rgba(56,217,236,.16),rgba(56,217,236,.04));box-shadow:0 0 60px rgba(56,217,236,.2);display:flex;flex-direction:column;gap:18px">
<div style="font-size:38px;color:#c9cad2">Comenta <b style="font:500 48px 'JetBrains Mono';letter-spacing:4px;color:#38d9ec">{palavra}</b> {onde}</div>
<div style="font:500 26px 'JetBrains Mono';color:#8e909c">→ o link chega no seu direct na hora</div></div>'''
def prov(k,h1,p,palavra,onde='no post de hoje',fs=118):
    return story(f'''{TOPS}
<div style="display:flex;flex-direction:column;gap:34px">{K(k,'#ff6b61')}
<h1 style="font-size:{fs}px;letter-spacing:-1px;line-height:1.02">{h1}</h1>
<p style="font-size:44px;line-height:1.4">{p}</p></div>
{cta(palavra,onde)}''',70)
CK2='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#061015" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def item(t): return f'<div class="card" style="padding:22px 28px"><div class="ck" style="width:54px;height:54px">{CK2}</div><div style="font-size:38px;font-weight:600;line-height:1.25">{t}</div></div>'
def oferta(k,h1,itens,foto_,fs=112):
    li=''.join(item(i) for i in itens)
    return story(f'''{TOPS}
<div style="display:flex;align-items:center;gap:30px">{foto(foto_,170,'center 20%')}<div>{K(k)}<div style="font-size:30px;color:#a9abb6;margin-top:10px">Otto Gurgel · Dedikar IA</div></div></div>
<h1 style="font-size:{fs}px;letter-spacing:-1px;line-height:1.02">{h1}</h1>
<div style="display:flex;flex-direction:column;gap:14px">{li}</div>
{cta('DIAGNÓSTICO','em qualquer post da @dedikar.ia')}
<div style="font:500 30px 'JetBrains Mono';color:#c9cad2;text-align:center">ou chama no WhatsApp (81) 96000-1152</div>''',46)
S={}
# provocação 12h (ligada ao carrossel do dia)
S['P1028']=prov("Dinheiro parado","Você trabalhou. Entregou. <em>E o dinheiro não entrou.</em>","Cliente atrasado não é azar. <b>É falta de régua de cobrança.</b>","CAIXA")
S['P1029']=prov("Pergunta incômoda","Você paga alguém para fazer o que a IA faz <em>em 2 minutos?</em>","Ata de reunião, resposta a cliente, proposta comercial. <b>Tudo isso já dá para passar para a IA.</b>","PROMPTS")
S['P1030']=prov("Custo invisível","Quanto custa um carro parado <em>que ninguém viu?</em>","Planilha não avisa manutenção, multa nem carro parado. <b>Sistema avisa.</b>","PROJETO")
S['P1031']=prov("Erro caro","Comprar IA antes de organizar a empresa <em>é jogar dinheiro fora.</em>","Faça o teste de 1 minuto do post de hoje e veja <b>por onde começar.</b>","DIAGNÓSTICO",fs=104)
S['P1102']=prov("Você às 23h","Financeiro numa planilha. Frota em outro sistema. <em>Quem cruza tudo isso?</em>","Se a resposta é \"eu, à noite\", <b>a sua empresa precisa de um portal, não de mais horas.</b>","PROJETO",fs=104)
S['P1103']=prov("Verdade incômoda","O saldo do banco <em>mente.</em>","Ele mostra o hoje. <b>O aperto está nas próximas semanas</b>, e só aparece quando já chegou.","CAIXA",fs=150)
S['P1104']=prov("Pergunta de dono","Tem carro na sua frota dando prejuízo. <em>Você sabe qual?</em>","A frota inteira dá lucro. <b>Cada carro, sozinho, talvez não.</b>","DIAGNÓSTICO")
S['P1105']=prov("Venda perdida","Seu site manda o cliente para o WhatsApp. <em>E o WhatsApp fecha às 18h.</em>","Quem quer reservar à noite <b>reserva no concorrente.</b>","PROJETO",fs=104)
S['P1106']=prov("Teste rápido","Se você precisa perguntar a alguém como está a empresa, <em>não tem painel. Tem dependência.</em>","5 números, numa tela, <b>todo dia no mesmo horário.</b>","PAINEL",fs=96)
S['P1107']=prov("Cartão de visita caro","Site bonito que não vende <em>é cartão de visita caro.</em>","Site bom agenda, vende ou capta, <b>mesmo com você dormindo.</b>","DIAGNÓSTICO")
# oferta 19h (dias sem Alerta ao empresário)
S['O1028']=oferta("O que a Dedikar faz","Agente de IA <em>no seu WhatsApp</em>",["Responde na hora, 24h por dia","Qualifica e agenda sozinho","Passa para um humano quando precisa"],'otto_04.jpg')
S['O1030']=oferta("O que a Dedikar faz","CRM do <em>jeito da sua empresa</em>",["Funil, WhatsApp e IA numa tela","Nenhum lead esquecido","Relatórios sem planilha"],'otto_09.jpg')
S['O1102']=oferta("O que a Dedikar faz","Painéis que se <em>atualizam sozinhos</em>",["Financeiro, frota e vendas","Dados puxados do seu sistema","O problema aparece no mesmo dia"],'otto_06.jpg')
S['O1104']=oferta("O que a Dedikar faz","Cobrança que <em>roda sozinha</em>",["Lembra antes do vencimento","Cobra no WhatsApp ou e-mail","Registra quem pagou"],'otto_10.jpg')
S['O1106']=oferta("O que a Dedikar faz","Site que <em>vende de verdade</em>",["Preço em tempo real","Pagamento no Pix ou cartão","Integrado ao CRM e ao WhatsApp"],'otto_03.jpg')
# domingo 18h
S['D1101']=prov("Domingo à noite","Amanhã é segunda. <em>A semana já tem plano ou vai ser incêndio de novo?</em>","Use o modelo de fechamento e planejamento da semana. <b>15 minutos, toda sexta.</b>","SEXTA","em qualquer post",fs=100)
S['D1108']=prov("Domingo à noite","Quantas horas do seu fim de semana <em>foram para resolver o que um sistema resolveria?</em>","Diagnóstico gratuito de 45 minutos: <b>eu te mostro o primeiro passo.</b>","DIAGNÓSTICO","em qualquer post",fs=96)
for k,v in S.items(): open(f'{k}.html','w').write(v)
print(list(S))
