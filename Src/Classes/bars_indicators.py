from tupy import *

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