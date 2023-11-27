from tupy import keyboard
from Classes.Animacao import *
from Classes.bars_indicators import *
from Classes.Chalice.Ataques.Explosao import Explosao
from Classes.Chalice.Ataques.MiniBomba import MiniBomba
from Classes.Chalice.Ataques.Tiro import Tiro
from Classes.Chalice.listasDeImagens import *
from Classes.Personagem import *
from Classes.Chalice.ShootSpark import *
from Classes.Hitbox import HitBox
from Classes.Contador import Contador
from Classes.You_died_screen import You_Died

class Chalice(Personagem):
    QTD_IMAGENS_NORMAL = 6
    QTD_IMAGENS_TRANSICAO_ESPECIAL = 18
    QTD_IMAGENS_ESPECIAL = 4
    QTD_IMAGENS_GHOST = 24

    def __init__(self, oponente: Personagem, x: int = 240, y: int = 240, vida: int = 3):
        super().__init__(x, y, vida, HitBox(x - 35, y - 25, 70, 50))
        self._oponente = oponente
        self._animacao = Animacao(Chalice.QTD_IMAGENS_NORMAL, ChaliceNormal, 6)
        self._animacaoAtual = self.animacao
        self._animacaoDeTransicao = Animacao(Chalice.QTD_IMAGENS_TRANSICAO_ESPECIAL, ChaliceTransitionToSpecial, 2)
        self._animacaoEspecial = Animacao(Chalice.QTD_IMAGENS_ESPECIAL, ChaliceSpecial, 3)
        self._animacaoGhost = Animacao(Chalice.QTD_IMAGENS_GHOST, ChaliceGhost, 2)
        self._barraDeVida = Chalice_Life_bar(vida)
        self._specialCards: list[Chalice_special_card] = []
        self._barraDeSpecial = Chalice_special_card(0)
        self._contadorSpecial = Contador(24)
        self._contador_decreaseSpecial = Contador(33)
        self._numero_cards_Special = 1
        self._special_full_charged = False
        self._special_decrease = False
        self._special_charged_stop = False


        self._ShootSpark = ShootSpark(x+70, y+5)
        self._contadorAuxiliar = Contador(2)
        self._contadorDeTiroSimples = Contador(4)
        self._atacando = False
        self._estaMorto = False
        self._modoDeAtaque = 0
        self._modoEspecial = False
        #self.possibilidadeDeAtaque = True
        self._velocidade = 20
        self._auto_incremente_special_bar = Contador(2)
        
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
    def animacaoGhost(self) -> Animacao:
        return self._animacaoGhost
    
    @animacaoGhost.setter
    def animacaoGhost(self, animacao: Animacao) -> None:
        self._animacaoGhost = animacao
        pass
    
    @property
    def barraDeVida(self) -> Chalice_Life_bar:
        return self._barraDeVida
    
    @barraDeVida.setter
    def barraDeVida(self, barraDeVida: Chalice_Life_bar) -> None:
        self._barraDeVida = barraDeVida
        pass

    @property
    def barraDeSpecial(self) -> Chalice_special_card:
        return self._barraDeSpecial
    
    @barraDeSpecial.setter
    def barraDeSpecial(self, barraDeSpecial: Chalice_special_card) -> None:
        self._barraDeSpecial = barraDeSpecial
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
    
    @property
    def estaMorto(self) -> bool:
        return self._estaMorto
    
    @estaMorto.setter
    def estaMorto(self, valor: bool) -> None:
        self._estaMorto = valor
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
    
    def decrementa_vida(self) -> None:
        super().decrementa_vida()
        if self.barraDeVida.hp>0 and self.animacaoAtual == self.animacao:
            self.barraDeVida.decrease_hp()
            if self.barraDeVida.hp == 0:
                dead_screen = You_Died()
        pass
    
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
            if keyboard.is_key_down('e') and self._special_full_charged:
                self.atacando = False
                self.animacaoAtual = self.animacaoDeTransicao
                self._special_decrease = True
        self.hitbox.atualiza_posicao(self.posX - 35, self.posY - 25)

    
    def movimenta_fantasma(self) -> None:
        self.posY -= 8
        pass
    
    def troca_modo_de_ataque(self) -> None:
        if keyboard.is_key_down('z'):
            if not self.contadorAuxiliar.esta_zerado():
                self.contadorAuxiliar.zera_contador()
            if self.modoDeAtaque == 0:
                self.modoDeAtaque = 1
            elif self.modoDeAtaque == 1:
                self.modoDeAtaque = 2
            else:
                self.modoDeAtaque = 0
    
    def update(self) -> None:
        self.cria_special_cards()
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
        if self.barraDeVida.hp <= 0:
            self.animacaoAtual = self.animacaoGhost
            self.atacando = False
            self.estaMorto = True
            self.movimenta_fantasma()


        if self.animacaoAtual == self.animacao:
            self._auto_incremente_special_bar.incrementa()

        
        # if keyboard.is_key_just_down('k'):
        #         self.barraDeVida.decrease_hp()
        #         if self.vida > 0:
        #             self.decrementa_vida()


        Tiro.corrige_origem(self.posX, self.posY)
        
        if self.atacando:
            self._ShootSpark._show()
        else:
            self._ShootSpark._hide()
        self._ShootSpark.posX = self.posX + 70
        self._ShootSpark.posY = self.posY + 5

        ####
        ####



        
            
        if ((self._auto_incremente_special_bar.esta_zerado()) and (self._special_full_charged is False) and (self._special_decrease is False)):
            self.altera_special_cards()

        # self.aumenta_especial()
            
        self.special_full()

        # if keyboard.is_key_just_down('o'):
        #     if self._special_full_charged is True:
        #         self._special_decrease = True
        #         self._numero_cards_Special = 1

        if (self._special_charged_stop is True) and (self._special_decrease is True):
            self.special_full_decrease()



        
    def cria_special_cards(self) -> None:
        if len(self._specialCards) == 0:
            for i in range(5):
                self._specialCards.append(Chalice_special_card(i))

    def altera_special_cards(self) -> None:
        if self._numero_cards_Special < 6:
            if self._specialCards[self._numero_cards_Special-1].s_level < 45:
                self._specialCards[self._numero_cards_Special-1].increase_special_bar()
            else:
                self._numero_cards_Special += 1
                if self._numero_cards_Special != 6:
                    self._specialCards[self._numero_cards_Special-1].increase_special_bar()
                else:
                    self._special_full_charged = True
                    self._numero_cards_Special = 1
                    for i in range(5):
                        self._specialCards[i].s_level =0

    def special_full(self) -> None:
        if self._special_full_charged is True:
            self.movimento_special_carregado()

    def movimento_special_carregado(self) -> None:
        if (self._auto_incremente_special_bar.esta_zerado()) and (self._special_charged_stop is False):
            for i in range(5):
                if self._contadorSpecial._contador < 12:
                    self._specialCards[i].atualiza_imagem(44 - (self._contadorSpecial._contador))
                    if (44 - self._contadorSpecial._contador == 33) and (self._special_decrease is True):
                        self._special_charged_stop = True
                else:
                    self._specialCards[i].atualiza_imagem((self._contadorSpecial._contador)+21)
            self._contadorSpecial.incrementa()

    def special_full_decrease(self) -> None:
        if self._auto_incremente_special_bar.esta_zerado():
            k = self._contador_decreaseSpecial._contador
            self._contador_decreaseSpecial.incrementa()
            for i in range(5):
                if (33 - k) >= 10:
                    self._specialCards[i].file = f"../Img/Chalice/SpecialCards/SC{33 -k}.png"
                else:
                    if (33 - k) > 1:
                        self._specialCards[i].file = f"../Img/Chalice/SpecialCards/SC0{33 -k}.png"
                    else:
                        self._specialCards[i].file = f"../Img/Chalice/SpecialCards/SC00.png"
            if (33-k) == 1:
                self._special_charged_stop = False
                self._special_decrease = False
                self._special_full_charged = False
                # self._numero_cards_Special = 1

    def aumenta_especial(self):
        if (self._special_full_charged is False) and (self._special_decrease is False):
            self.altera_special_cards()
        self._auto_incremente_special_bar.incrementa()
    
'''
    def flee(self) -> None:
        if keyboard.is_key_just_down('q'):
            self.posY -= 20
            
    def break_attack(self,status: bool):
        self.possibilidadeDeAtaque = status

    def especial_movement(self) -> None:
        self.posX += self.especial_vel
'''