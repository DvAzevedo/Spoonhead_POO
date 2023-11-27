import pygame
from tupy import*
from pygame.locals import *
from Classes.Cenario import *
from Classes.MenuInicial import *
from Classes.InicioDeJogo import *

pygame.init()

Cenario.criar_cenario()

mensagemDeReady = Ready()
transicaoParaAGameplay = Transicao()    
fundoDoMenuInicial = FundoDoMenu()
cupAndMugMenu = CupAndMug()
mensagemDoMenu = PressioneTab()
 
run(globals())
