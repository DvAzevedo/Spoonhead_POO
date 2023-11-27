from Classes.Ataque import *
from Classes.Chalice.listasDeImagens import ChaliceExplosion

class Explosao(Ataque):
    QTD_IMAGENS_EXPLOSAO = 27
    
    def __init__(self, x: int, y: int, alvo: Personagem, dano: int) -> None:
        super().__init__(x, y, alvo, Animacao(Explosao.QTD_IMAGENS_EXPLOSAO, ChaliceExplosion, 1), dano)
        pass
    
    def atualiza_coordenadas(self) -> None:
        return super().atualiza_coordenadas()
        
    def causa_dano(self) -> None:
        self.alvo.sofre_dano(self.dano)
        pass
    
    def update(self) -> None:
        self.file = self.animacao.anima()
        if self.animacao.fim:
            self.destroy()
        pass
        