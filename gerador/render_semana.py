import sys, shutil, pathlib
from semana import D
from base import render
nomes=sys.argv[1:] or list(D)
for n in nomes:
    pasta,S=D[n]; print(render(n,S,f'out/{pasta}'))
