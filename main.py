from cenario import *
from tupy import *

e = Ceu(500, 280, 4)
f = Ceu(1500, 280, 4)

c = Chao(860, 500, 10)
ch = Chao(-180, 500, 10)

musica_de_fundo = pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play(-1)

run(globals())