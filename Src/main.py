from tupy import*
import pygame
from pygame.locals import *
from Classes.Cenario import *
from Classes.MenuInicial import *
from Classes.Chalice.Chalice import Chalice
from Classes.cena import cena
from Classes.HildaBerg.HildaBerg import *

pygame.init()

Cenario.criar_cenario()

#comentar/descomentar as duas linhas abaixo para retirar/colocar a música
#musica_de_fundo = pygame.mixer.music.load('music/this-time.mp3')
#musica_de_fundo = pygame.mixer.music.load('../music/deus_lhe_page_sound_track.mpeg')



vilao = HildaBerg(700, 220)
jogador = Chalice(vilao)

cena.heroi = jogador


run(globals())