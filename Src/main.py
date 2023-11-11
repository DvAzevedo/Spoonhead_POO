from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto, PedraY3, PedraY5
import pygame
from pygame.locals import * 
from Classes.cenario import *
from Classes.cenario import criar_cenario
from HildaBerg.hildaBerg import *
from Classes.chalice import Chalice
pygame.init()

criar_cenario()

#comentar/descomentar as duas linhas abaixo para retirar/colocar a música
musica_de_fundo = pygame.mixer.music.load('../music/this-time.mp3')
pygame.mixer.music.play(-1)

pedra = Arma(1, PedraSeno)
fogo = Arma(1, FogoReto)
pedray3 = Arma(1, PedraY3)
pedray5 = Arma(1, PedraY5)

pedra = Arma(1, PedraSeno)
fogo = Arma(1, FogoReto)
pedray3 = Arma(1, PedraY3)
pedray5 = Arma(1, PedraY5)
#vi = Vilao_test_1(800, 300, ["../Img/blimp_idle_0001.png", "../Img/blimp_idle_0001.png" ],200, [pedra, fogo, pedray3, pedray5])

vi = HildaBerg(700, 220)
s = Chalice(vi)

run(globals())