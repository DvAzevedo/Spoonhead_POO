from tupy import*
lista_de_viloes = []

class Vilao(Image):
    def __init__(self, file, life, cena):
        self._file = file
        self.life = life
        self.defeated = False
        self.cena = cena
        self.cena.viloes.append(self)
                
    def recebe_dano(self, dano):
        self.life -= dano
        self.defeated = self.hasBeendefeated()
    
    def hasBeendefeated(self):
        if self.life <= 0:
            return True
        self.cena.viloes.remove(self)