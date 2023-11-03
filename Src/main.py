from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto, PedraY3, PedraY5
from Classes.personagem import Vilao_test_1


pedra = Arma(20, PedraSeno)
fogo = Arma(3, FogoReto)
pedray3 = Arma(1, PedraY3)
pedray5 = Arma(1, PedraY5)
vi = Vilao_test_1(800, 300, "../Img/vilaoRedSmile100_poo.png", 200, [pedra, fogo, pedray3, pedray5])
run(globals())

