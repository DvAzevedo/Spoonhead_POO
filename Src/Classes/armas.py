from tupy import*
import math

class Arma():
    def __init__(self, qtd_ammunition, projectile):
        self.projectile = projectile
        self.qtd_ammunition = qtd_ammunition
        self.projectilesDisparados = 0
        self.atirou = False
        self.ammunitionList = []
        for i in range(qtd_ammunition):
            x = projectile(False)
            self.ammunitionList.append(x)
        self.currentMuni = [0]
    def reloadMuni(self):
        self.ammunitionList.clear()
        for i in range(self.qtd_ammunition):
            x = self.projectile()
            self.ammunitionList.append(x)
        self.currentMuni = [0]
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

class Projectile(Image):
    def __init__(self, x, y, image, helper):
        self.file = image
        self.x = x 
        self.y = y
        self.helper = helper
        self.fired = False
    def isOutScreen(self):
        if self.x < 0:
            return True
        if self.x > 800:
            return True
        if self.y > 500:
            return True
        if self.y < 0:
            return True
        else:
            return False
    def stopShot(self):
        if self.isOutScreen():
            self.destroy()

class PedraSeno(Projectile):
    def __init__(self, fired = False):
        super().__init__(800, 250, "../Img/pedra_poo.png", -0.2)
        self.fired = fired
    def shootSeno(super):
        super.helper += 0.1
        super.x -= 10
        super.y = ((math.sin(super.helper)*250) + 250)
    def update(self):
        if self.fired == True:
            self._show()
            self.shootSeno()
            super().stopShot()
        else:
            self._hide()

class FogoReto(Projectile):
    def __init__(self, fired = False):
        super().__init__(800, 250, "../Img/fogo_poo.png", 0)
        self.fired = fired
    def shootStraight(super):
        super.x -=20
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            super().stopShot()
        else:
            self._hide()

class PedraY(Projectile):
    def __init__(self, fired = False, y_Direction = 0):
        super().__init__(800, 250, "../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.y_Direction = y_Direction
    def shootStraight(super, self):
        super.x -= 20
        super.y -= self.y_Direction
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            super().stopShot()
        else:
            self._hide()

class PedraTripla:
    def __init__(self, fired = False):
        self.pedras = []
        self.pedras.append(PedraY(False, 0))
        self.pedras.append(PedraY(False, 20))
        self.pedras.append(PedraY(False, -20))
        self.fired = fired
    def update(self):
        if self.fired == True:
            for i in range(3):
                self.pedras[i].fired = True
                
            
        