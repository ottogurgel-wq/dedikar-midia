import sys; from narrados import J; from reel_narrado import fazer
tema,_,c=J['Feedback']
nome,voz=sys.argv[1],sys.argv[2]
fazer(nome,tema,voz,c)
