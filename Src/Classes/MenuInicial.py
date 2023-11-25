from typing import Optional
from tupy import *
from Classes.Animacao import *


CupMug = []
for i in range(1, 35):
    if i == 1 or i == 7 or i == 23 or i == 29:
        pass    
    else:
        CupMug.append(f"../Img/Menus/CupheadAndMugman/cuphead_title_screen_{i:04d}.png")
Qtd_de_imag = 30
delay = 1

# A imagem de "../Img/Menus/texto0002.png" é um png vazio para que a imagem 'pisque' ao ser animada
lista_textao = ["../Img/Menus/texto0001.png", '../Img/Menus/texto0002.png']
Qtd_de_imag_texto = 2
delay_texto = 6

class FundoDoMenu(Image):
    def __init__(self):
        self._x = 450
        self._y = 250
        self._file = "../Img/Menus/title_screen_background.png"
    
    def update(self) -> None:
        if keyboard.is_key_just_down('Tab') == True:
            self._hide()
            self._destroy()

class PressioneTab(Image):
    def __init__(self):
        self._x = 450
        self._y = 205
        self._file = "../Img/Menus/texto0001.png"
        self.animacaoo = Animacao(Qtd_de_imag_texto, lista_textao, delay_texto)

    def update(self) -> None:
        self._file = self.animacaoo.anima()
        if keyboard.is_key_just_down('Tab') == True:
            self._hide()
            self._destroy()

class CupAndMug(Image):
    def __init__(self):
        self._x = 450
        self._y = 360
        self._file = "../Img/Menus/CupheadAndMugman/cuphead_title_screen_0001.png"
        self._animacao = Animacao(Qtd_de_imag, CupMug, delay)

    def update(self) -> None:
        self._file = self._animacao.anima()
        if keyboard.is_key_just_down('Tab') == True:
            self._hide()
            self._destroy()


