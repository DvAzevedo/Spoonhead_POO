from tupy import *
from Classes.animacao import Contador
from Classes.chaliceImgLists import*

class Life_vilao(BaseGroup):

    def __init__(self,vilao,life,x=0,y=0):
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
    def __init__(self,life):
        self.hp_inicial = life
        self.hp = self.hp_inicial
        self.file = f"../Img/Chalice/Life/hp_0{life}.png"
        self.x = 60
        self.y = 470
        self.contador_critical = Contador(2)
        self.alternate = False

    def decrease_hp(self):
        if self.hp > 1:
            self.hp -= 1
            self.file = f"../Img/Chalice/Life/hp_0{self.hp}.png"
    
    def update(self):
        if self.hp == 1:
            self.contador_critical.incrementa()
            if self.contador_critical._contador == 0:
                if self.alternate == True:
                    self.file = f"../Img/Chalice/Life/hp_01_critical.png"
                else:
                    self.file = f"../Img/Chalice/Life/hp_01_lowlevel.png"
                self.alternate = not self.alternate
                

            



