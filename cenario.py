from tupy import *
import pygame
from pygame.locals import * 
from sys import exit

pygame.init()
class Ceu(Image):
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.velocidade = v

    def update(self) -> None:
        if(self.x - self.velocidade) < -500:
            self.x = 1450

        else: self.x -= self.velocidade
        
class Chao(Image):
    def __init__(self, x, y, v):
        self.x = x 
        self.y = y 
        self.velocidade = v


    def update(self) -> None:
        if (self.x - self.velocidade) < -505:
            self.x = 1560
        else:
            self.x -= self.velocidade

e = Ceu(500, 280, 4)
f = Ceu(1500, 280, 4)

c = Chao(860, 500, 10)
ch = Chao(-180, 500, 10)

musica_de_fundo = pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play(-1)
#descomentar  para tocar a música 
run(globals())
