import math
from Classes.Animacao import *
from Classes.Personagem import *
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.HildaBerg.Ataques.Avanco import Avanco, Explosao
from Classes.HildaBerg.Ataques.Risada import Risada
from Classes.HildaBerg.Ataques.Tornado import Tornado
from Classes.HildaBerg.Ataques.estrela import EstrelaLua2
from Classes.HildaBerg.Ataques.estrela import EstrelaLua
from Classes.bars_indicators import *
from Classes.Contador import Contador
from Classes.Hitbox import HitBox
from Classes.Victory_screen import Victory

ORIGEM_X = 700
ORIGEM_Y = 240

QTD_IMGS_ESTADO_NORMAL = 21
QTD_IMGS_ESTADO_RINDO = 19
QTD_IMGS_ESTADO_INTRO = 43
QTD_IMGS_ESTADO_TRANSICAO = 48
QTD_IMGS_ESTADO_TORNADO = 38
QTD_IMGS_ESTADO_SUMMONANDO = 21
QTD_IMGS_ESTADO_TOURO = 16
QTD_IMGS_ATQ_TOURO = 21

QTD_IMG_MOON_STATE_NORMAL = 16
QTD_IMG_MOON_STATE_ATK_INTRO = 12
QTD_IMG_MOON_STATE_ATK = 8
QTD_IMG_MOON_STATE_ATK_BACK = 8
QTD_IMG_MOON_STATE_SMOKE = 15
QTD_IMG_MOON_STATE_DEATH = 16
ANIME_DELAY_MOON = 2

MOON_STATE_LIST = ["idle", "atkIntro", "atk", "death"]

moon_idleAnime = Animacao(QTD_IMG_MOON_STATE_NORMAL, hildaMoon, ANIME_DELAY_MOON)
moon_atkIntroAnime = Animacao(QTD_IMG_MOON_STATE_ATK_INTRO, moonAtkIntro, ANIME_DELAY_MOON)
moon_atkAnime = Animacao(QTD_IMG_MOON_STATE_ATK, moonAtk, ANIME_DELAY_MOON)
moon_atkBackAnime = Animacao(QTD_IMG_MOON_STATE_ATK_BACK, moonAtkBack, ANIME_DELAY_MOON)
moon_smokeAnime = Animacao(QTD_IMG_MOON_STATE_SMOKE, moonSmoke, ANIME_DELAY_MOON)
moon_deathAnime = Animacao(QTD_IMG_MOON_STATE_DEATH, moonDeath, ANIME_DELAY_MOON)


class HildaBerg(Personagem):
    ESTADOS = ["intro", "normal", "rindo", "tornado", "avancoIntro", "avanco", "summonando", "touro", "touroAtq", "transicao", "morte", "lua", "luaAtkIntro", "luaAtk"]
    ATRASO_DE_ANIMACAO = 2
    def __init__(self, x: int = ORIGEM_X, y: int = ORIGEM_Y, alvo=None) -> None:
        super().__init__(x, y, 1000, HitBox(x - 80, y - 55, 160, 110))
        self._alvo = alvo
        self.file = hildaIntro[0]
        self._estado = HildaBerg.ESTADOS[0]
        self._animacaoIntro = Animacao(QTD_IMGS_ESTADO_INTRO, hildaIntro, HildaBerg.ATRASO_DE_ANIMACAO)
        self._animacaoPadrao = Animacao(QTD_IMGS_ESTADO_NORMAL, hildaNormal, HildaBerg.ATRASO_DE_ANIMACAO)
        self._animacaoRindo = Animacao(QTD_IMGS_ESTADO_RINDO, hildaLaugh, 1)
        self._animacaoDeTransicao = Animacao(QTD_IMGS_ESTADO_TRANSICAO, hildaTransition, HildaBerg.ATRASO_DE_ANIMACAO)
        self._animacaoTornado = Animacao(QTD_IMGS_ESTADO_TORNADO, hildaTornado, 1)
        self._animacaoSummonando = Animacao(QTD_IMGS_ESTADO_SUMMONANDO, hildaSummon, HildaBerg.ATRASO_DE_ANIMACAO)
        self._animacaoTouro = Animacao(QTD_IMGS_ESTADO_TOURO, touroImgList, HildaBerg.ATRASO_DE_ANIMACAO)
        self._animacaoAtqTouro = Animacao(QTD_IMGS_ATQ_TOURO, touroAtkImgList, 1)
        self._animacoes = [self.animacaoIntro, self.animacaoPadrao, self.animacaoRindo, self.animacaoTornado, self.animacaoSummonando, self.animacaoTouro,  self.animacaoAtqTouro, self.animacaoDeTransicao, moon_deathAnime, moon_idleAnime, moon_atkIntroAnime, moon_atkAnime]
        self._contadorDeAtraso = Contador(HildaBerg.ATRASO_DE_ANIMACAO)
        self._contadorParaAtaques = Contador(300)
        self._angulacao = 1.5
        self._atacando = True
        self._contador = 0
        self._estrela = False
        pass
    
    #Propriedades
    @property
    def alvo(self) -> Personagem:
        return self._alvo
    
    @alvo.setter
    def alvo(self, alvo: Personagem) -> None:
        self._alvo = alvo
        pass
    
    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado
        pass
    
    @property
    def animacaoIntro(self) -> Animacao:
        return self._animacaoIntro
    
    @animacaoIntro.setter
    def animacaoIntro(self, animacao: Animacao) -> None:
        self._animacaoIntro = animacao
        pass
    
    @property
    def animacaoPadrao(self) -> Animacao:
        return self._animacaoPadrao
    
    @animacaoPadrao.setter
    def animacaoPadrao(self, animacao: Animacao) -> None:
        self._animacaoPadrao = animacao
        pass
    
    @property
    def animacaoRindo(self) -> Animacao:
        return self._animacaoRindo
    
    @animacaoRindo.setter
    def animacaoRindo(self, animacao: Animacao) -> None:
        self._animacaoRindo = animacao
        pass
    
    @property
    def animacaoDeTransicao(self) -> Animacao:
        return self._animacaoDeTransicao
    
    @animacaoDeTransicao.setter
    def animacaoDeTransicao(self, animacao: Animacao) -> None:
        self._animacaoDeTransicao = animacao
        pass
    
    @property
    def animacaoTornado(self) -> Animacao:
        return self._animacaoTornado
    
    @animacaoTornado.setter
    def animacaoTornado(self, animacao: Animacao) -> None:
        self._animacaoTornado = animacao
        pass
    
    @property
    def animacaoSummonando(self) -> Animacao:
        return self._animacaoSummonando
    
    @animacaoSummonando.setter
    def animacaoSummonando(self, animacao: Animacao) -> None:
        self._animacaoSummonando = animacao
        pass
    
    @property
    def animacaoTouro(self) -> Animacao:
        return self._animacaoTouro
    
    @animacaoTouro.setter
    def animacaoTouro(self, animacao: Animacao) -> None:
        self._animacaoTouro = animacao
        pass
    
    @property
    def animacaoAtqTouro(self) -> Animacao:
        return self._animacaoAtqTouro
    
    @animacaoAtqTouro.setter
    def animacaoAtqTouro(self, animacao: Animacao) -> None:
        self._animacaoAtqTouro = animacao
        pass
    
    @property
    def animacoes(self) -> list[Animacao]:
        return self._animacoes
    
    @animacoes.setter
    def animacoes(self, animacoes: list[Animacao]) -> None:
        self._animacoes = animacoes
        pass
    
    @property
    def contadorDeAtraso(self) -> Contador:
        return self._contadorDeAtraso
    
    @contadorDeAtraso.setter
    def contadorDeAtraso(self, contador: Contador) -> None:
        self._contadorDeAtraso = contador
        pass
    
    @property
    def contadorParaAtaques(self) -> Contador:
        return self._contadorParaAtaques
    
    @contadorParaAtaques.setter
    def contadorParaAtaques(self, contador: Contador) -> None:
        self._contadorParaAtaques = contador
        pass
    
    @property
    def angulacao(self) -> float:
        return self._angulacao
    
    @angulacao.setter
    def angulacao(self, angulacao: float) -> None:
        self._angulacao = angulacao
        pass
    
    @property
    def contador(self) -> int:
        return self._contador
    
    @contador.setter
    def contador(self, contador: int) -> None:
        self._contador = contador
        pass
    
    @property
    def estrela(self) -> bool:
        return self._estrela
    
    @estrela.setter
    def estrela(self, estrela: bool) -> None:
        self._estrela = estrela
        pass
    
    @property
    def atacando(self) -> bool:
        return self._atacando
    
    @atacando.setter
    def atacando(self, valor: bool) -> None:
        self._atacando = valor
        pass
    
    #Movimentação
    def movimenta(self) -> None:
        if self.estado == "normal" or self.estado == "rindo" or self.estado == "touro":
            self.movimento_padrao()
            pass   
        if self.estado == "avanco":
            self.movimento_de_avanco()
            pass
        if self.estado == "touroAtq":
            self.movimento_de_ataque_touro()
            pass
        if self.estado == "summonando":
            self.movimento_summonando()
            pass
        if self.estado == "transicao":
            self.movimento_de_transicao()
            pass
        self.hitbox.atualiza_posicao(self.posX - 80, self.posY - 55)
        pass
    
    def movimento_de_ataque_touro(self) -> None:
        resultado = any(self.file == touroAtkImgList[i] for i in range(10, 21))
        if resultado:
            self.posX -= 50
            pass
        self.posX += 3
        pass
    
    def movimento_de_avanco(self) -> None:
        self.posX -= 60
        pass
    
    def movimento_de_transicao(self) -> None:
        if self.animacaoDeTransicao.imgsCont.contador > 37 and self.animacaoDeTransicao.imgsCont.contador < QTD_IMGS_ESTADO_TRANSICAO:
            self.posX += int((ORIGEM_X - self.posX) / (QTD_IMGS_ESTADO_TRANSICAO - self.animacaoDeTransicao.imgsCont.contador))
            self.posY += int((ORIGEM_Y - self.posY) / (QTD_IMGS_ESTADO_TRANSICAO - self.animacaoDeTransicao.imgsCont.contador))
        pass 
    
    def movimento_padrao(self) -> None:
        self.angulacao += 0.1
        self.posX = int(((100 * math.sqrt(2) * math.cos(self.angulacao) * math.sin(self.angulacao) / (1 + math.sin(self.angulacao)**2)) + ORIGEM_X))
        self.posY = int(((-100 * math.sqrt(2) * math.cos(self.angulacao) / (1 + math.sin(self.angulacao)**2)) + ORIGEM_Y))
        pass 
    
    def movimento_summonando(self) -> None:
        self.posX += 16
        pass

    #Animações
    def animacao_finalizada(self, ultimaImg: str) -> bool:
        if self.file == ultimaImg:
            return True
        return False
    
    def animar(self, indice: int) -> None:
        self.animacoes[indice].animar()
        self.file = self.animacoes[indice].imagem
        pass
        
    def volta_ao_normal(self, ultimaImg: str, estado: str) -> None:
        if self.file == ultimaImg:
            self.estado = estado
        pass
        
    def tipo_de_animacao(self) -> None:
        if self.estado == "intro":
            self.animar(0)
            self.volta_ao_normal(self.animacaoIntro.ultimaImg, "normal")
            pass
        elif self.estado == "normal":
            self.animar(1)
            pass
        elif self.estado == "rindo":
            self.animar(2)
            self.volta_ao_normal(self.animacaoRindo.ultimaImg, "normal")
            pass
        elif self.estado == "tornado":
            self.animar(3)
            self.volta_ao_normal(self.animacaoTornado.ultimaImg, "normal")
            pass
        elif self.estado == "summonando":
            self.animar(4)
            if self.file == hildaSummon[19] or self.file == hildaSummon[16]:
                Explosao(self.posX, self.posY, self.alvo)
            self.volta_ao_normal(self.animacaoSummonando.ultimaImg, "touro")
            pass
        elif self.estado == "touro":
            self.animar(5)
            pass
        elif self.estado == "touroAtq":
            self.animar(6)
            if self._collides_with(self.alvo.hitbox):
                self.alvo.decrementa_vida()
            if self.file == self.animacaoAtqTouro.ultimaImg:
                self.posX += 30
                self.estrela = False
            if self.estrela == False:
                self.volta_ao_normal(self.animacaoAtqTouro.ultimaImg, "touro")
            pass
        elif self.estado == "transicao":
            self.animar(7)
            self.volta_ao_normal(self.animacaoDeTransicao.ultimaImg, "lua")
            pass
        elif self.estado == "morte":
            self.animar(8)
        elif self.estado == "lua":
            self.animar(9)
            self.volta_ao_normal(moon_idleAnime.ultimaImg, "luaAtkIntro")
        elif self.estado == "luaAtkIntro":
            self.animar(10)
            if self.file == moon_atkIntroAnime.ultimaImg:
                self.estado = "luaAtk"
            pass
        elif self.estado == "luaAtk":
            self.animar(11)
        else:
            pass

    #Ataques
    def ataca(self) -> None:
        self.avanco()
        self.risada()
        self.tornado()
        self.touro_atq()
        self.lua_atq()
        self.lua_atq2()
        pass

    def avanco(self) -> None:
        if self.vida <= 650:
            if self.estado == "normal":
                self.estado = "avancoIntro"
                Avanco(self.posX, self.posY, self.alvo, self)
        pass
    
    def risada(self) -> None:
        if self.contadorParaAtaques.contador % 100 == 0:
            if self.estado == "normal":
                Risada(self.posX, self.posY, self.alvo)
                self.estado = "rindo" 
        pass
    
    def tornado(self) -> None:
        if self.contadorParaAtaques.contador % 150 == 0:
            if self.estado == "normal":
                Tornado(self.posX, self.posY, self.alvo)
                self.estado = "tornado"
        pass

    def touro_atq(self) -> None:
        if self.contadorParaAtaques.contador % 150 == 0:
            if self.estado == "touro":
                self.estado = "touroAtq"
        pass

    def lua_atq(self) -> None:
        if self.contadorParaAtaques.contador % 100 == 0:
            if self.estado == "luaAtk":
                EstrelaLua(self.posX, self.posY, self.alvo)
        pass

    def lua_atq2(self) -> None:
        if self.contadorParaAtaques.contador % 50 == 0:
            if self.estado == "luaAtk":
                EstrelaLua2(self.posX, self.posY, self.alvo)
        pass
    
    def update(self) -> None:
        self.contador +=1
        if self.atacando:
            self.contadorParaAtaques.incrementa()
        self.ataca()
        self.tipo_de_animacao()
        self.movimenta()
        if self.alvo.estaMorto:
            self.contadorParaAtaques.contador = 1
            self.atacando = False
        if self.vida <= 350 and self.estado == "touro":
            Explosao(self.posX, self.posY, self.alvo)
            self.estado = "transicao"
        if self.vida <= 0:
            self.estado = "morte"
            vitoria = Victory()
        pass