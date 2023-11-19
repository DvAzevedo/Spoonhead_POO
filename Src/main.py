from tupy import*
import pygame
from pygame.locals import *
from Classes.Cenario import *
from Classes.Chalice.Chalice import Chalice
from Classes.cena import cena
from Classes.HildaBerg.HildaBerg import *

pygame.init()

Cenario.criar_cenario()

#comentar/descomentar as duas linhas abaixo para retirar/colocar a música
#musica_de_fundo = pygame.mixer.music.load('../music/this-time.mp3')
#musica_de_fundo = pygame.mixer.music.load('../music/deus_lhe_page_sound_track.mpeg')
pygame.mixer.music.play(-1)

#vi = Vilao_test_1(800, 300, ["../Img/blimp_idle_0001.png", "../Img/blimp_idle_0001.png" ],200, [pedra, fogo, pedray3, pedray5])
vilao = HildaBerg(700, 220)
jogador = Chalice(vilao)

#cena.heroi = s


run(globals())