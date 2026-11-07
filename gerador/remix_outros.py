import sys, pathlib, subprocess
sys.path.insert(0,'/home/claude/reels')
from sfx2 import mix
from reel_narrado import palavras, achar
R=pathlib.Path('/home/claude/reels/out'); M=pathlib.Path('/home/claude/dedikar-midia'); F=pathlib.Path('/home/claude/som/final')
# stories: kits diferentes, alguns só com entrada e fechamento
ST={'1110':[('entrada_tambor',0,.5),('fecho_mensagem',2.4,.5)],
    '1111':[('meio_relogio',0,.35),('fecho_mensagem',1.0,.55)],
    '1112':[('entrada_glitch',0,.5),('meio_scanner',0.45,.4),('fecho_sucesso',2.6,.45)],
    '1113':[('entrada_reveal',0,.5),('fecho_caixa',2.2,.5)],
    '1114':[('entrada_boom',0,.55)],
    '1116':[('whoosh_entrada',0,.45),('meio_bolha',0.45,.45),('chime_cta',2.6,.45)]}
(F/'dedikar/2026-11-stories-animados').mkdir(parents=True,exist_ok=True)
for k,ev in ST.items(): mix(str(R/f'stories/_{k}.mp4'),str(F/f'dedikar/2026-11-stories-animados/Story_{k}.mp4'),ev,dur=8.0)
print('ok stories')
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
# narrado Mayla
W=palavras(M/'voz/2026-11-13_lead_esfriou.json'); t=lambda f: achar(W,f)-0.15
ev=[('fecho_mensagem',0.15,.5),('meio_relogio',0.6,.28),('entrada_glitch',t('Ninguém respondeu'),.35),('meio_swish',t('No dia seguinte'),.35),
    ('entrada_boom',t('É falta de'),.45),('meio_scanner',t('Um agente de')+0.4,.35),('meio_camera',t('E nada sai'),.3),('fecho_sucesso',t('Comente AGENTE')+0.9,.55)]
v=str(R/'LeadEsfriou/_v.mp4'); d=dur(v); (F/'dedikar/2026-11-13-reel-lead-esfriou').mkdir(parents=True,exist_ok=True)
mix(v,str(F/'dedikar/2026-11-13-reel-lead-esfriou/Reel_LeadEsfriou.mp4'),ev,dur=d,voz=str(M/'voz/2026-11-13_lead_esfriou.mp3'))
# narrado Otto
W=palavras(M/'voz/2026-11-14_feedback_otto.json'); t=lambda f: achar(W,f)-0.15
ev=[('entrada_reveal',0.0,.45),('meio_swish',t('Primeiro'),.35),('meio_swish',t('Segundo'),.35),('meio_swish',t('Terceiro'),.35),('nota_vidro',t('E termine')+0.3,.35),('impacto_titulo',t('Feedback bom'),.4),('fecho_orquestra',t('Salve e use')+0.6,.5)]
v=str(R/'Feedback/_v.mp4'); d=dur(v); (F/'ottogurgel/2026-11-14-reel-feedback').mkdir(parents=True,exist_ok=True)
mix(v,str(F/'ottogurgel/2026-11-14-reel-feedback/Reel_Feedback.mp4'),ev,dur=d,voz=str(M/'voz/2026-11-14_feedback_otto.mp3'))
print('ok narrados')
