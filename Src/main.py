from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto, PedraY3, PedraY5
from Classes.personagem import Vilao_test_1, Heroi_test_1
import pygame
from pygame.locals import * 
from Classes.cenario import *

pygame.init()

e = Ceu(500, 280, 4)
f = Ceu(1500, 280, 4)

c = Chao(860, 500, 10)
ch = Chao(-180, 500, 10)

musica_de_fundo = pygame.mixer.music.load('music/musica1.mp3')
pygame.mixer.music.play(-1)

pedra = Arma(1, PedraSeno)
fogo = Arma(1, FogoReto)
pedray3 = Arma(1, PedraY3)
pedray5 = Arma(1, PedraY5)
vi = Vilao_test_1(800, 300, ["../Img/fork.png", "../Img/fork.png" ],200, [pedra, fogo, pedray3, pedray5])
s = Heroi_test_1(["../Img/Test1.png", "../Img/Test2.png", "../Img/Test3.png", "../Img/Test4.png"], vi)
run(globals())