from tupy import keyboard
from Classes.Animacao import *
from Classes.bars_indicators import *
from Classes.Chalice.Ataques.Explosao import Explosao
from Classes.Chalice.Ataques.MiniBomba import MiniBomba
from Classes.Chalice.Ataques.Tiro import Tiro
from Classes.Chalice.listasDeImagens import *
from Classes.Personagem import *
from Classes.Chalice.ShootSpark import *

class Chalice(Personagem):
    QTD_IMAGENS_NORMAL = 6
    QTD_IMAGENS_TRANSICAO_ESPECIAL = 18
    QTD_IMAGENS_ESPECIAL = 4

    def __init__(self, oponente: Personagem, x=240, y=240, vida = 3):
        super().__init__(x, y, vida, HitBox(x - 54, y - 40, 108, 80))
        self._oponente = oponente
        self._animacao = Animacao(Chalice.QTD_IMAGENS_NORMAL, ChaliceNormal, 6)
        self._animacaoAtual = self.animacao
        self._animacaoDeTransicao = Animacao(Chalice.QTD_IMAGENS_TRANSICAO_ESPECIAL, ChaliceTransitionToSpecial, 2)
        self._animacaoEspecial = Animacao(Chalice.QTD_IMAGENS_ESPECIAL, ChaliceSpecial, 3)
        self._barraDeVida = Chalice_Life_bar(vida)
        self._ShootSpark = ShootSpark(x+70, y+5)
        self._contadorAuxiliar = Contador(2)
        self._contadorDeTiroSimples = Contador(4)
        self._atacando = False
        self._modoDeAtaque = 0
        self._modoEspecial = False
        #self.possibilidadeDeAtaque = True
        self._velocidade = 20
        
    @property
    def oponente(self) -> Personagem:
        return self._oponente
    
    @oponente.setter
    def oponente(self, oponente: Personagem) -> None:
        self._oponente = oponente
        pass
    
    @property
    def animacao(self) -> Animacao:
        return self._animacao
    
    @animacao.setter
    def animacao(self, animacao: Animacao) -> None:
        self._animacao = animacao
        pass
    
    @property
    def animacaoAtual(self) -> Animacao:
        return self._animacaoAtual
    
    @animacaoAtual.setter
    def animacaoAtual(self, animacao: Animacao) -> None:
        self._animacaoAtual = animacao
        pass
    
    @property
    def animacaoDeTransicao(self) -> Animacao:
        return self._animacaoDeTransicao
    
    @animacaoDeTransicao.setter
    def animacaoDeTransicao(self, animacao: Animacao) -> None:
        self._animacaoDeTransicao = animacao
        pass
    
    @property
    def animacaoEspecial(self) -> Animacao:
        return self._animacaoEspecial
    
    @animacaoEspecial.setter
    def animacaoEspecial(self, animacao: Animacao) -> None:
        self._animacaoEspecial = animacao
        pass
    
    @property
    def barraDeVida(self) -> Chalice_Life_bar:
        return self._barraDeVida
    
    @barraDeVida.setter
    def barraDeVida(self, barraDeVida: Chalice_Life_bar) -> None:
        self._barraDeVida = barraDeVida
        pass
    
    @property
    def contadorAuxiliar(self) -> Contador:
        return self._contadorAuxiliar
    
    @contadorAuxiliar.setter
    def contadorAuxiliar(self, contador: Contador) -> None:
        self._contadorAuxiliar = contador
        pass
    
    @property
    def contadorDeTiroSimples(self) -> Contador:
        return self._contadorDeTiroSimples
    
    @contadorDeTiroSimples.setter
    def contadorDeTiroSimples(self, contador: Contador) -> None:
        self._contadorDeTiroSimples = contador
        pass
    
    @property
    def atacando(self) -> bool:
        return self._atacando
    
    @atacando.setter
    def atacando(self, atacando: bool) -> None:
        self._atacando = atacando
        pass
    
    @property
    def modoDeAtaque(self) -> int:
        return self._modoDeAtaque
    
    @modoDeAtaque.setter
    def modoDeAtaque(self, modoDeAtaque: int) -> None:
        self._modoDeAtaque = modoDeAtaque
        pass
    
    @property
    def modoEspecial(self) -> bool:
        return self._modoEspecial
    
    @modoEspecial.setter
    def modoEspecial(self, modoEspecial: bool) -> None:
        self._modoEspecial = modoEspecial
        pass
    
    @property
    def velocidade(self) -> int:
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade: int) -> None:
        self._velocidade = velocidade
        pass
    
    def ataca(self) -> None:
        if keyboard.is_key_just_down('space'):
            if self.animacaoAtual == self.animacao:
                self.atacando = not self.atacando
            
        if self.atacando == True:
            if self.modoDeAtaque == 0:
                Tiro.tiro_simples(self.contadorDeTiroSimples, self.posX, self.posY, self.oponente)
            if self.modoDeAtaque == 1:
                Tiro.tiro_triplo(self.posX, self.posY, self.oponente)
            if self.modoDeAtaque == 2:
                MiniBomba.bombardeio(self.contadorAuxiliar, self.posX, self.posY, self.oponente)
                self.contadorAuxiliar.zera_contador()
    
    def movimenta(self) -> None:
        if self.animacaoAtual == self.animacao or self.animacaoAtual == self.animacaoEspecial:
            if keyboard.is_key_down('Left') and self.posX >= 20:
                self.posX -= self.velocidade
            if keyboard.is_key_down('Right') and self.posX <= 780:
                self.posX += self.velocidade
            if keyboard.is_key_down('Up') and self.posY >= 20:
                if self.modoEspecial is False:
                    self.posY -= self.velocidade
            if keyboard.is_key_down('Down') and self.posY <= 480:
                if self.modoEspecial is False:
                    self.posY += self.velocidade
        if self.animacaoAtual == self.animacao:
            if keyboard.is_key_down('e'):
                self.atacando = False
                self.animacaoAtual = self.animacaoDeTransicao
        self.hitbox.atualiza_posicao(self.posX - 54, self.posY - 40)
    
    def troca_modo_de_ataque(self):
        if keyboard.is_key_just_down('z'):
            if not self.contadorAuxiliar.esta_zerado():
                self.contadorAuxiliar.zera_contador()
            if self.modoDeAtaque == 0:
                self.modoDeAtaque = 1
            elif self.modoDeAtaque == 1:
                self.modoDeAtaque = 2
            else:
                self.modoDeAtaque = 0
    
    def update(self) -> None:
        self.troca_modo_de_ataque()
        self.ataca()
        self.movimenta()
        self.file = self.animacaoAtual.anima()
        if self.file == self.animacaoDeTransicao.ultimaImg:
            self.animacaoAtual = self.animacaoEspecial
        if self.animacaoAtual == self.animacaoEspecial and self._collides_with(self.oponente):
            self._hide()
            explosao = Explosao(self.posX, self.posY, self.oponente, 100)
            explosao.causa_dano()
            self.animacaoAtual = self.animacao
            self.posX -= 10
            self._show()
        if keyboard.is_key_just_down('k'):
                self.barraDeVida.decrease_hp()
        Tiro.corrige_origem(self.posX, self.posY)
        if self.atacando:
            self._ShootSpark._show()
        else:
            self._ShootSpark._hide()
        self._ShootSpark.x = self.posX + 70
        self._ShootSpark.y = self.posY + 5
        pass
    
'''
    def flee(self) -> None:
        if keyboard.is_key_just_down('q'):
            self.posY -= 20
            
    def break_attack(self,status: bool):
        self.possibilidadeDeAtaque = status

    def especial_movement(self) -> None:
        self.posX += self.especial_vel
'''