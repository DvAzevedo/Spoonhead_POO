from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto
from Classes.personagem import Vilao_test_1


pedra = Arma(20, PedraSeno)
fogo = Arma(1, FogoReto)

vi = Vilao_test_1(800, 300, "../Img/balaoVerde_poo.webp", 200, [pedra, fogo])
run(globals())