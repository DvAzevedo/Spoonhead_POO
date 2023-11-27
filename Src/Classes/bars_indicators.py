from tupy import *
from Classes.Contador import Contador
from Classes.Chalice.listasDeImagens import *
from Classes.Personagem import Personagem

class Life_vilao(BaseGroup):

    def __init__(self, vilao: Personagem, life: int, x: int = 0, y: int = 0):
        self.x0 = -35
        self.y0 = 110
        self.vilao = vilao
        self.life = life
        self.texto = str(life)
        self.label = Label(self.texto,0,0)
        self._rectangle = Rectangle(0,0, self.label._width, self.label._height)
        self._add(self._rectangle)
        self._add(self.label)
        self._x = x + self.x0
        self._y = y + self.y0


    # def update(self):
    #     if self.is_mouse_over():
    #         self._rectangle.outline = "black"
    #         if mouse.is_button_just_down():
    #             self.funcao()
    #     else:
    #         self._rectangle.outline = "#ccc"

# b = Life_vilao("20")

# run(globals())

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
            



