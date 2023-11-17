from tupy import *

class Cenario(Image):
    def __init__(self, x, y, v, f, r = -630, p = 1900) -> None:
        self._x = x 
        self._y = y 
        self._velocidade = v
        self._file = f
        self._reinicia = r
        self._pidse = p      #pidse = posição inicial "x" do segundo elemento
        pass
    
    @property
    def posX(self) -> int:
        return self._x
    
    @posX.setter
    def posX(self, x) -> None:
        self._x = x
        pass
    
    @property
    def posY(self) -> int:
        return self._y
    
    @posY.setter
    def posy(self, y) -> None:
        self._y = y
        pass
    
    @property
    def velocidade(self) -> int:
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, v) -> None:
        self._velocidade = v
        pass
    
    @property
    def file(self) -> int:
        return self._file
    
    @file.setter
    def file(self, f) -> None:
        self._file = f
        pass
    
    @property
    def reinicia(self) -> int:
        return self._reinicia
    
    @reinicia.setter
    def reinicia(self, r) -> None:
        self._reinicia = r
        pass
    
    @property
    def pidse(self) -> int:
        return self._pidse
    
    @pidse.setter
    def pidse(self, p) -> None:
        self._pidse = p
        pass
    
    @classmethod
    def criar_cenario(cls) -> None:
        chaoE = cls(630, 435, 15, "../Img/Cenario/chao1.png")
        chaoD = cls(1900, 435, 15, "../Img/Cenario/chao1.png")

        ceuE = cls(500, 90, 2, "../Img/Cenario/sky_loop.png", -485, 1495)
        ceuD = cls(1495, 90, 2, "../Img/Cenario/sky_loop.png", -485, 1495)

        montanha_mlongeE = cls(630, 155, 3, "../Img/Cenario/MontanhasMLonge.png")
        montanha_mlongeD = cls(1900, 155, 3, "../Img/Cenario/MontanhasMLonge.png")

        montanha_longeE = cls(630, 190, 4, "../Img/Cenario/MontanhasLonge.png")
        montanha_longeD = cls(1900, 190, 4, "../Img/Cenario/MontanhasLonge.png")

        montanha_meioE = cls(630, 210, 5, "../Img/Cenario/MontanhasMeio.png")
        montanha_meioD = cls(1900, 210, 5, "../Img/Cenario/MontanhasMeio.png")

        montanhaE = cls(630, 230, 6, "../Img/Cenario/MontanhasE.png")
        montanhaD = cls(1900, 230, 6, "../Img/Cenario/MontanhasD.png")

        desertoE = cls(630, 290, 6, "../Img/Cenario/deserto.png")
        desertoD = cls(1900, 290, 6, "../Img/Cenario/deserto.png")

        arbustoE = cls(630, 315, 8, "../Img/Cenario/arbustos.png")
        arbustoD = cls(1900, 315, 8, "../Img/Cenario/arbustos.png")
    
        matoE = cls(630, 320, 15, "../Img/Cenario/matoE.png")
        matoD = cls(1900, 320, 15, "../Img/Cenario/matoD.png")
        
        pass
    
    def update(self) -> None:
        if (self.x - self.velocidade) < self.reinicia:
            self.x = self.pidse
            pass
        else:
            self.x -= self.velocidade
            pass

# Cada "pedaço" de cenário representa um objeto onde todos os cenários possuem a parte da esquerda e a parte da direita".
# Logo eles serão nomeados de acordo com a sua ordem no parallax sendo os elementos na parte de baixo do jogo os primeiros a serem criados.
# Eles seguirão o padrão [nome][esquerda ou direita].
# Em casos especias em que existem outras partes de cenário além da "esquerda" e "direita" o nome terá mudanças.
