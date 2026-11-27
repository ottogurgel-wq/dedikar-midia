"""Dedikar Educação · série de posts no @dedikar.ia (mesma identidade visual, selo próprio)."""
import base
from base import num, chk, CSS, bg
T = 6
EDU_CSS = """
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:6px}
.fr{background:rgba(20,22,32,.86);border:1px solid rgba(255,255,255,.10);border-radius:20px;padding:24px 26px}
.fr .t{font:500 20px 'JetBrains Mono';letter-spacing:3px;color:#38d9ec;text-transform:uppercase}
.fr .d{font:500 28px/1.3 'DM Sans';color:#e8e8ee;margin-top:8px}
.card.sm{padding:18px 26px}.card.sm b{font-size:32px}.card.sm small{font-size:25px}
.sig{display:flex;align-items:center;gap:22px}
.mono{width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,#38d9ec,#b48cff);display:flex;align-items:center;justify-content:center;font:600 50px 'Cormorant Garamond';color:#0b0b10;flex-shrink:0}
"""
def slide(i, tot, body, foot=('@dedikar.ia · Dedikar Educação', 'Arraste →'), capa=False):
    sub = '<div class=sub>Escolas particulares · Carpina e região</div>' if capa else ''
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}{EDU_CSS}</style></head><body>{bg(11+i*97)}
<div class=top><div class=br><div class=tile><img src="logo.png"></div><div><div class=brand>Dedikar <span>Educação</span></div>{sub}</div></div><div class=cnt>{i}/{tot}</div></div>
<div class=main>{body}</div><div class=foot><span>{foot[0]}</span><span>{foot[1]}</span></div></body></html>"""
def bloco(k, h2, itens, extra='', gap=14):
    return f'<div class=k>— {k}</div><h2>{h2}</h2><div style="display:flex;flex-direction:column;gap:{gap}px">{"".join(itens)}</div>{extra}'
def sm(html): return html.replace('<div class=card>', '<div class="card sm">')
D = {}
WHATS='(81) 3197-3127'
D['Edu_Lancamento'] = ('dedikar/2026-11-30-educacao-lancamento', [
 slide(1, T, '''<div class=k>— Chegou a Dedikar Educação</div>
<h1 style="font-size:90px">Sua escola cuida dos alunos.<br><i>Quem cuida da escola?</i></h1>
<p>Pedagógico, comercial, marketing e tecnologia para escolas particulares, <b>com uma pedagoga ao lado da direção.</b></p>
<div class=grid4>
<div class=fr><div class=t>01 · Pedagógico</div></div><div class=fr><div class=t>02 · Comercial</div></div>
<div class=fr><div class=t>03 · Marketing</div></div><div class=fr><div class=t>04 · Tecnologia e IA</div></div></div>''', capa=True),
 slide(2, T, bloco('O momento da escola', 'Dezembro<br><i>decide 2027.</i>', [
   num(1, 'Rematrícula', 'cada família que fica é uma vaga que não precisa ser reconquistada'),
   num(2, 'Matrículas novas', 'as famílias da região estão escolhendo a escola agora'),
   num(3, 'Planejamento 2027', 'calendário, projetos e a formação dos professores em janeiro')])),
 slide(3, T, bloco('O que a gente faz', 'Quatro frentes,<br><i>um só time.</i>', [sm(x) for x in [
   num(1, 'Pedagógico', 'planejamento 2027, projetos no calendário e formação de professores'),
   num(2, 'Comercial', 'atendimento de rematrícula e de visitas, acompanhamento das famílias'),
   num(3, 'Marketing', 'divulgação, campanhas e a escola encontrada no Google e no Instagram'),
   num(4, 'Tecnologia e IA', 'assistente que responde as famílias, comunicados e painel de matrículas')]], gap=12)),
 slide(4, T, bloco('Por onde começar', 'Diagnóstico<br><i>360.</i>', [sm(x) for x in [
   chk('Planejamento e organização pedagógica'), chk('Aprendizagem e acompanhamento'),
   chk('Liderança e formação de professores'), chk('Famílias, matrículas e relacionamento'),
   chk('Dados, processos e tecnologia')]],
   extra='<p style="font-size:31px">Um retrato da escola em <b>5 dimensões</b> e um <b>plano de ação de 90 dias.</b></p>', gap=10)),
 slide(5, T, bloco('Quem conduz', 'Mais de 20 anos<br><i>na educação.</i>', [
   chk('Gestão escolar e coordenação pedagógica', 'Ensino Fundamental, Médio e EJA'),
   chk('Formação de professores', 'capacitação de educadores e equipes'),
   chk('Matrículas, calendário e famílias', 'do planejamento ao atendimento')],
   extra='<p style="font-size:30px">A nossa pedagoga é pós-graduada em <b>Gestão Educacional, Neuroeducação e Psicopedagogia.</b></p>')),
 slide(6, T, '''<div class=k>— Carpina e região</div><h2>Vamos planejar<br><i>2027 juntos?</i></h2>
<p>Converse com a nossa pedagoga numa <b>reunião online de 30 minutos</b>, no horário que for melhor para a direção.</p>
<div class=pill style="font-size:46px;padding:22px 42px;letter-spacing:3px">Chame no direct</div>
<p style="font-size:30px;color:#9a9ca8">ou no WhatsApp <b style="color:#fff">'''+WHATS+'''</b> · dedikaria.com.br</p>''',
  foot=('@dedikar.ia · Dedikar Educação', 'Envie para a direção da escola')),
])
def cta(h2, texto):
    return slide(6, T, f'''<div class=k>— Dedikar Educação</div><h2>{h2}</h2><p>{texto}</p>
<div class=pill style="font-size:46px;padding:22px 42px;letter-spacing:3px">Chame no direct</div>
<p style="font-size:30px;color:#9a9ca8">ou no WhatsApp <b style="color:#fff">{WHATS}</b> · dedikaria.com.br</p>''', foot=('@dedikar.ia · Dedikar Educação', 'Envie para a direção da escola'))
def capa(k, h1, p, extra=''):
    return slide(1, T, f'<div class=k>— {k}</div><h1 style="font-size:90px">{h1}</h1><p>{p}</p>{extra}', capa=True)
D['Edu_Rematricula'] = ('dedikar/2026-12-07-educacao-rematricula', [
 capa('Rematrícula 2027', 'A família decide se fica<br><i>antes do boleto.</i>', 'A rematrícula não começa no formulário. <b>Começa no que a família viveu durante o ano.</b>'),
 slide(2, T, '''<div class=k>— O cenário em Carpina</div><h2>Menos alunos<br><i>chegando.</i></h2>
<div class=big><div class=v>−4,9%</div><div class=l>matrículas na rede particular de Carpina, de 2024 para 2025 (Censo Escolar)</div></div>
<p>Quando entram menos alunos, <b>cada família que fica vale mais.</b></p>'''),
 slide(3, T, bloco('Sinais de alerta', 'Quem pode<br><i>não voltar.</i>', [sm(x) for x in [
   num(1, 'Família que sumiu', 'não vem às reuniões nem responde os comunicados'),
   num(2, 'Reclamação sem retorno', 'o assunto ficou no ar até dezembro'),
   num(3, 'Atraso que começou no meio do ano', 'às vezes é sinal de outra conversa'),
   num(4, 'Pedido de documento “só por curiosidade”', 'histórico, declaração, transferência')]], gap=12)),
 slide(4, T, bloco('O que fazer agora', 'Conversa antes<br><i>do contrato.</i>', [
   chk('Ligar para as famílias em dúvida', 'a direção, não só a secretaria'),
   chk('Mostrar o que vem em 2027', 'projetos, novidades e calendário'),
   chk('Facilitar a decisão', 'prazo claro, condição clara, um canal só')])),
 slide(5, T, bloco('Com organização', 'Rematrícula<br><i>acompanhada.</i>', [
   chk('Cada família com a sua situação', 'confirmou, em dúvida ou sem resposta'),
   chk('Comunicado que chega e é respondido', 'WhatsApp com lembretes dentro do prazo'),
   chk('Assistente que tira as dúvidas na hora', 'inclusive fora do horário da secretaria')])),
 cta('Como está a rematrícula<br><i>na sua escola?</i>', 'Numa <b>reunião online de 30 minutos</b>, a nossa pedagoga ajuda a direção a organizar a rematrícula e o planejamento de 2027.'),
])
D['Edu_Calendario'] = ('dedikar/2026-12-14-educacao-calendario', [
 capa('Planejamento 2027', 'O calendário da escola<br><i>também comunica.</i>', 'Projetos que envolvem alunos, famílias e a cidade <b>mostram o trabalho da escola o ano inteiro.</b>'),
 slide(2, T, bloco('Calendário de datas', 'Só feriado<br><i>e prova?</i>', [
   num(1, 'Datas soltas', 'cada professor faz do seu jeito'),
   num(2, 'A família só vê a escola na reunião', 'o que acontece na sala não aparece'),
   num(3, 'Projeto que ninguém fica sabendo', 'o trabalho existe, mas não é visto')])),
 slide(3, T, bloco('Calendário com projetos', 'Um projeto<br><i>por bimestre.</i>', [sm(x) for x in [
   num(1, 'Acolhimento e identidade', 'a turma se apresenta para as famílias'),
   num(2, 'Leitura e cultura local', 'feira, sarau ou mostra com a comunidade'),
   num(3, 'Ciência e cidadania', 'um problema real do bairro ou da cidade'),
   num(4, 'Mostra de encerramento', 'o ano em exposição, com as famílias')]], gap=12)),
 slide(4, T, bloco('Como montar', 'Projeto que<br><i>cabe na rotina.</i>', [
   chk('Ligado ao currículo', 'não é evento a mais, é aula com propósito'),
   chk('Data, responsável e produto final', 'todo mundo sabe o que vai entregar'),
   chk('Registrado e divulgado', 'com autorização das famílias para imagem')])),
 slide(5, T, bloco('O resultado', 'A escola<br><i>vista pela cidade.</i>', [
   chk('Alunos como protagonistas', 'eles apresentam o que aprenderam'),
   chk('Famílias dentro da escola', 'participando, não só assistindo'),
   chk('Conteúdo real para as redes', 'sem precisar inventar post')])),
 cta('Vamos montar o<br><i>calendário de 2027?</i>', 'A nossa pedagoga ajuda a coordenação a planejar os projetos do ano, numa <b>reunião online de 30 minutos.</b>'),
])
D['Edu_Formacao'] = ('dedikar/2026-12-21-educacao-formacao', [
 capa('Semana pedagógica', 'Janeiro define<br><i>o ritmo do ano.</i>', 'A formação dos professores antes das aulas <b>é onde o planejamento vira prática.</b>'),
 slide(2, T, bloco('O que costuma acontecer', 'Formação<br><i>de um dia só.</i>', [
   num(1, 'Palestra e pronto', 'inspira na hora e some na segunda semana'),
   num(2, 'Tema escolhido na última hora', 'sem olhar o que a escola precisa'),
   num(3, 'Nada para acompanhar depois', 'ninguém volta ao assunto no bimestre')])),
 slide(3, T, bloco('Formação que funciona', 'Parte do que<br><i>a escola precisa.</i>', [
   chk('Tema escolhido pelo diagnóstico', 'aprendizagem, inclusão, rotina de sala'),
   chk('Prática, não só teoria', 'o professor sai com a aula planejada'),
   chk('Acompanhamento combinado', 'observação e conversa ao longo do bimestre')])),
 slide(4, T, bloco('Uma pauta possível', 'Três dias<br><i>em janeiro.</i>', [
   num(1, 'A escola que queremos em 2027', 'metas, projetos e combinados do ano'),
   num(2, 'Planejamento por turma', 'currículo, avaliação e projetos'),
   num(3, 'Famílias e inclusão', 'comunicação, acolhimento e adaptações')])),
 slide(5, T, bloco('E a tecnologia?', 'IA a favor<br><i>do professor.</i>', [
   chk('Planejamento mais rápido', 'atividades e adaptações em minutos'),
   chk('O professor revisa e decide', 'a IA sugere, quem ensina é ele'),
   chk('Uso responsável', 'regras claras para alunos e equipe')])),
 cta('Vamos planejar<br><i>o seu janeiro?</i>', 'Com mais de 20 anos na educação, a nossa pedagoga monta a formação junto com a coordenação. Comece por uma <b>reunião online de 30 minutos.</b>'),
])
D['Edu_Google'] = ('dedikar/2026-12-28-educacao-google', [
 capa('Matrículas 2027', 'A família pesquisa<br><i>antes de visitar.</i>', 'Antes de ligar, ela procura a escola no Google e no Instagram. <b>O que ela encontra?</b>'),
 slide(2, T, bloco('O que ela vê', 'A primeira visita<br><i>é online.</i>', [
   num(1, 'Perfil no Google incompleto', 'sem fotos, sem horário, telefone que não atende'),
   num(2, 'Avaliações sem resposta', 'elogio ou reclamação, ficou no vácuo'),
   num(3, 'Instagram parado', 'o último post é de um evento de meses atrás')])),
 slide(3, T, bloco('O básico bem feito', 'Ser encontrada<br><i>e bem vista.</i>', [
   chk('Perfil da escola no Google completo', 'fotos, etapas, horário e como chegar'),
   chk('Todas as avaliações respondidas', 'com cuidado, inclusive as ruins'),
   chk('Uma página com o essencial', 'etapas, endereço e como agendar visita')])),
 slide(4, T, bloco('Instagram da escola', 'Mostrar a escola<br><i>de verdade.</i>', [
   chk('Rotina e projetos', 'com autorização das famílias para imagem'),
   chk('Professores e equipe', 'quem cuida dos alunos todos os dias'),
   chk('Como funciona a matrícula', 'datas, documentos e contato')])),
 slide(5, T, bloco('Atendimento', 'Responder<br><i>na hora.</i>', [
   chk('Assistente no WhatsApp', 'tira dúvidas e agenda a visita, inclusive à noite'),
   chk('Toda família registrada', 'ninguém fica sem retorno'),
   chk('Visita com retorno', 'uma mensagem no dia seguinte')])),
 cta('Como a sua escola<br><i>aparece hoje?</i>', 'Numa <b>reunião online de 30 minutos</b>, a gente mostra o que a família encontra quando procura a sua escola.'),
])
if __name__ == '__main__':
    import sys
    base.render('Edu_Lancamento', D['Edu_Lancamento'][1], 'out/prev')
    print('ok')
