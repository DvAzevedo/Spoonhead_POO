from tupy import *
from Classes.Contador import Contador
from Classes.Chalice.listasDeImagens import *

class Chalice_Life_bar(Image):
    def __init__(self,life: int) -> None:
        self.hp_inicial = life
        self.hp = self.hp_inicial
        self.file = f"../Img/Chalice/Life/hp_0{life}.png"
        self.x = 60
        self.y = 470
        self.contador_critical = Contador(2)
        self.alternate = False

    def decrease_hp(self) -> None:
        if self.hp > 0:
            self.hp -= 1
            if self.hp > 0:
                self.file = f"../Img/Chalice/Life/hp_0{self.hp}.png"
            else:
                self.file = f"../Img/Chalice/Life/hp_01_dead.png"
                
    def update(self) -> None:
        if self.hp == 1:
            self.contador_critical.incrementa()
            if self.contador_critical._contador == 0:
                if self.alternate == True:
                    self.file = f"../Img/Chalice/Life/hp_01_critical.png"
                else:
                    self.file = f"../Img/Chalice/Life/hp_01_lowlevel.png"
                self.alternate = not self.alternate
                
class Chalice_special_card(Image):
    def __init__(self,k: int, level: int = 0) -> None:
        self.s_inicial = level
        self.s_level = self.s_inicial
        self.file = f"../Img/Chalice/SpecialCards/SC00.png"
        self.k = k
        self.x = 120 + 27*self.k
        self.y = 470
        self.contador_critical = Contador(2)
        self.alternate = False

    def increase_special_bar(self) -> None:
        self.s_level += 1
        if self.s_level < 10:
            self.file = f"../Img/Chalice/SpecialCards/SC0{self.s_level}.png"
        elif (self.s_level >= 10 and self.s_level < 45):
            self.file = f"../Img/Chalice/SpecialCards/SC{self.s_level}.png"
    
    def atualiza_imagem(self,img_numb:int) -> None:
        self.file = f"../Img/Chalice/SpecialCards/SC{img_numb}.png"
            

    def update(self) -> None:
        if self.file == "../Img/Chalice/SpecialCards/SC00.png":
            self._hide()
        else:
            self._show()
            



