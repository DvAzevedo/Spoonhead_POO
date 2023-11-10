from tupy import*
from Classes.projeteis import*
import math


class Arma():
    def __init__(self, qtd_ammunition, projectile):
        self.x = 800
        self.y = 300
        self.projectile = projectile
        self.qtd_ammunition = qtd_ammunition
        self.projectilesDisparados = 0
        self.atirou = False
        self.ammunitionList = []
        for i in range(qtd_ammunition):
            x = projectile(self.x, self.y, False)
            self.ammunitionList.append(x)
    def reloadMuni(self):
        self.ammunitionList.clear()
        for i in range(self.qtd_ammunition):
            x = self.projectile(self.x, self.y)
            self.ammunitionList.append(x)
    def shoot(self):
        if self.projectilesDisparados < self.qtd_ammunition:
            self.ammunitionList[self.projectilesDisparados].fired = True
            self.projectilesDisparados += 1
        else:
            self.atirou = False
            self.projectilesDisparados = 0
            self.reloadMuni()
    def update(self):
        if self.atirou == True:
            self.shoot()

class PedraSeno(Projectile):
    def __init__(self, x, y, fired = False):
        super().__init__("../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.x = x
        self.aux_y = y
        self.aux_yBool = False
        self.y = y
    def shootSeno(self):
        self.helper += 0.1
        self.x -= 10
        self.y = ((math.sin(self.helper)*75)+self.aux_y)
    def update(self):
        if self.fired == True:
            if self.aux_yBool == False:
                self.aux_y = self.y
                self.aux_yBool = True
            self._show()
            self.shootSeno()
            super().stopShot(self.x, self.y)
        else:
            self._hide()

class FogoReto(Projectile):
    def __init__(self, x, y, fired = False):
        super().__init__("../Img/fogo_poo.png", 0)
        self.fired = fired
        self.x = x
        self.y = y
    def shootStraight(super):
        super.x -=20
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            super().stopShot(self.x, self.y)
        else:
            self._hide()

class PedraY3(Projectile):
    def __init__(self, x, y, fired = False, y_Direction = 0, clone = False):
        super().__init__("../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.y_Direction = y_Direction
        self.clone = clone
        self.count = 0
        self.x = x
        self.y = y
    def shootStraight(self):
        self.x -= 9
        self.y -= self.y_Direction
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            if self.clone == False and self.count == 0:
                self.count += 1
                PedraY3(self.x, self.y, True, -2, True)
                PedraY3(self.x, self.y, True, 2, True)
            self.stopShot(self.x, self.y)
        else:
            self._hide()

class PedraY5(Projectile):
    def __init__(self, x, y, fired = False, y_Direction = 0, clone = False):
        super().__init__("../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.y_Direction = y_Direction
        self.clone = clone
        self.count = 0
        self.x = x
        self.y = y
    def shootStraight(self):
        self.x -= 9
        self.y -= self.y_Direction
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            if self.clone == False and self.count == 0:
                self.count += 1
                x = PedraY5(self.x, self.y, True, -2, True)
                y = PedraY5(self.x, self.y, True, 2, True)
                x = PedraY5(self.x, self.y, True, -4, True)
                y = PedraY5(self.x, self.y, True, 4, True)
                
            super().stopShot(self.x, self.y)
        else:
            self._hide()

class Trajetorias(Image):
    def __init__(self, imgs, x, y):
        self.file = imgs[0]
        self.imgs = imgs
        self.x = x
        self.y = y
        self.helperSeno = -0.2
        self.aux_y = y
        pass

    def shootSeno(self, img):
        self.file = self.imgs[img]
        self.helper += 0.1
        self.x -= 10
        self.y = ((math.sin(self.helperSeno)*75)+self.aux_y)
    
    def shootStraight(self, xSpeed, ySpeed, img):
        self.file = self.imgs[img]
        self.x -= xSpeed
        self.y -= ySpeed