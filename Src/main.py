from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto, PedraY3, PedraY5
import pygame
from pygame.locals import * 
from Classes.cenario import *
from HildaBerg.hildaBerg import *
from Classes.chalice import Chalice
pygame.init()

e = Ceu(500, 280, 4)
f = Ceu(1500, 280, 4)

c = Chao(860, 500, 10)
ch = Chao(-180, 500, 10)

#musica_de_fundo = pygame.mixer.music.load('../music/music.mpeg')
#pygame.mixer.music.play(-1)

pedra = Arma(1, PedraSeno)
fogo = Arma(1, FogoReto)
pedray3 = Arma(1, PedraY3)
pedray5 = Arma(1, PedraY5)
#vi = Vilao_test_1(800, 300, ["../Img/blimp_idle_0001.png", "../Img/blimp_idle_0001.png" ],200, [pedra, fogo, pedray3, pedray5])

vi = HildaBerg(700, 220)
s = Chalice(vi)

run(globals())