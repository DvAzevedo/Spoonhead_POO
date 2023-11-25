from typing import Optional
from tupy import *
from Classes.Animacao import *
import pygame

'''
SE VC VEIO PARA PELA MÚSICA:
- Vá para a linha 66 na função "update" dentro da classe "Ready"
'''
pygame.init()

listaTransicao = []
for i in range(1, 18):
    listaTransicao.append(f"../Img/InicioDeJogo/Transitions/Transition{i:04d}.png")
Qtd_de_imag_transicao = 17
delay_transicao = 1

listaReady = []
for i in range(1, 52):
    if i == 2 or i == 8 or i == 14 or i == 20 or i == 26 or i == 32 or i == 38 or i == 44 or i == 50:
        pass    
    else:
        listaReady.append(f"../Img/InicioDeJogo/ReadyWALLOP!/FightText_GetReady_{i:04d}.png")
Qtd_de_imag_ready = 42
delay_ready = 1


class Transicao(Image):
    def __init__(self):
        self._x = 450
        self._y = 250
        self._file = "../Img/InicioDeJogo/Transitions/Transition0001.png"
        self.animacaoo = Animacao(Qtd_de_imag_transicao, listaTransicao, delay_transicao)
        self.ApertouTabUmaVez = False

    def update(self) -> None:
        if keyboard.is_key_just_down('Tab') == True:
            self.ApertouTabUmaVez = True


        if self.ApertouTabUmaVez == True:
            self._file = self.animacaoo.anima()
            if self._file == "../Img/InicioDeJogo/Transitions/Transition0017.png" :
                self._hide()
                self._destroy()
            

class Ready(Image):
    def __init__(self):
        self._x = 450
        self._y = 250
        self._file = "../Img/InicioDeJogo/ReadyWALLOP!/FightText_GetReady_0001.png"
        self.animacaoo = Animacao(Qtd_de_imag_ready, listaReady, delay_ready)
        self.ApertouTabUmaVez2 = False

    def update(self) -> None:
        if keyboard.is_key_just_down('Tab') == True:
            self.ApertouTabUmaVez2 = True
            pygame.mixer.music.load('Sound/SoundEffects/GameStartAnnouncer.wav')
            pygame.mixer.music.play(-1)

        if self.ApertouTabUmaVez2 == True:
            self._file = self.animacaoo.anima()
            if self._file == "../Img/InicioDeJogo/ReadyWALLOP!/FightText_GetReady_0051.png" :
                    self._hide()
                    #comentar/descomentar as duas linhas abaixo para retirar/colocar a música, se quiser mudar basta mudar o caminho do arquivo
                    pygame.mixer.music.load('Sound/Music/MusicaDaGameplay.mp3')
                    pygame.mixer.music.play(-1)
                    self._destroy()

            

