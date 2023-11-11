from tupy import *

class Terreno(Image):
    def __init__(self, x, y, v, r, p, f):
        #pidse = posição inicial "x" do segundo elemento
        self.x = x 
        self.y = y 
        self.velocidade = v
        self.reinicia = r
        self.pidse = p
        self._file = f

    def update(self) -> None:
        if (self.x - self.velocidade) < self.reinicia:
            self.x = self.pidse
        else:
            self.x -= self.velocidade

'''
-cada "pedaço" de cenário representa um objeto onde todos os cenários possuem a parte da esquerda e a parte da direita"
-logo eles serão nomeados de acordo com a sua ordem no parallax sendo os elementos na parte de baixo do jogo os primeiros a serem criados
-eles seguirão o padrão [nome][esquerda ou direita]
-em casos especias em que existem outras partes de cenário além da "esquerda" e "direita" o nome terá mudanças
'''
def criar_cenario():
    
    
    chaoE = Terreno(630, 435, 15, -630, 1900, "../Img/Cenarios/chao1.png")
    chaoD = Terreno(1900, 435, 15, -630, 1900, "../Img/Cenarios/chao1.png")

    ceuE = Terreno(500, 90, 2, -485, 1495, "../Img/Cenarios/sky_loop.png")
    ceuD = Terreno(1495, 90, 2, -485, 1495, "../Img/Cenarios/sky_loop.png")

    montanha_mlongeE = Terreno(630, 155, 3, -630, 1900, "../Img/Cenarios/MontanhasMLonge.png")
    montanha_mlongeD = Terreno(1900, 155, 3, -630, 1900, "../Img/Cenarios/MontanhasMLonge.png")

    montanha_longeE = Terreno(630, 190, 4, -630, 1900, "../Img/Cenarios/MontanhasLonge.png")
    montanha_longeD = Terreno(1900, 190, 4, -630, 1900, "../Img/Cenarios/MontanhasLonge.png")

    montanha_meioE = Terreno(630, 210, 5, -630, 1900, "../Img/Cenarios/MontanhasMeio.png")
    montanha_meioD = Terreno(1900, 210, 5, -630, 1900, "../Img/Cenarios/MontanhasMeio.png")

    montanhaE = Terreno(630, 230, 6, -630, 1900, "../Img/Cenarios/MontanhasE.png")
    montanhaD = Terreno(1900, 230, 6, -630, 1900, "../Img/Cenarios/MontanhasD.png")

    desertoE = Terreno(630, 290, 6, -630, 1900, "../Img/Cenarios/deserto.png")
    desertoD = Terreno(1900, 290, 6, -630, 1900, "../Img/Cenarios/deserto.png")

    arbustoE = Terreno(630, 315, 8, -630, 1900, "../Img/Cenarios/arbustos.png")
    arbustoD = Terreno(1900, 315, 8, -630, 1900, "../Img/Cenarios/arbustos.png")
   
    matoE = Terreno(630, 320, 15, -630, 1900, "../Img/Cenarios/matoE.png")
    matoD = Terreno(1900, 320, 15, -630, 1900, "../Img/Cenarios/matoD.png")