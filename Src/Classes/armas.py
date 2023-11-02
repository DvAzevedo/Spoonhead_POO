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
    def reloadMuni(self):
        self.ammunitionList.clear()
        for i in range(self.qtd_ammunition):
            x = self.projectile()
            print(x)
            self.ammunitionList.append(x)
    def shoot(self):
        if self.projectilesDisparados < self.qtd_ammunition:
            self.ammunitionList[self.projectilesDisparados].fired = True
            print(self.ammunitionList[self.projectilesDisparados])
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
    def shootSeno(self):
        self.helper += 0.1
        self.x -= 10
        self.y = ((math.sin(self.helper)*250) + 250)
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

class PedraY3(Projectile):
    def __init__(self, fired = False, y_Direction = 0, clone = False):
        super().__init__(800, 250, "../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.y_Direction = y_Direction
        self.clone = clone
        self.count = 0
    def shootStraight(self):
        self.x -= 9
        self.y -= self.y_Direction
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            if self.clone == False and self.count == 0:
                print(self.count)
                self.count += 1
                print(self.count)
                x = PedraY3(True, -2, True)
                y = PedraY3(True, 2, True)
            super().stopShot()
        else:
            self._hide()

class PedraY5(Projectile):
    def __init__(self, fired = False, y_Direction = 0, clone = False):
        super().__init__(800, 250, "../Img/pedra_poo.png", -0.2)
        self.fired = fired
        self.y_Direction = y_Direction
        self.clone = clone
        self.count = 0
    def shootStraight(self):
        self.x -= 9
        self.y -= self.y_Direction
    def update(self):
        if self.fired == True:
            self._show()
            self.shootStraight()
            if self.clone == False and self.count == 0:
                self.count += 1
                x = PedraY5(True, -2, True)
                y = PedraY5(True, 2, True)
                x = PedraY5(True, -4, True)
                y = PedraY5(True, 4, True)
                
            super().stopShot()
        else:
            self._hide()

                
            
        