from tupy import*
from Classes.armas import Arma, PedraSeno, FogoReto, PedraTripla
from Classes.personagem import Vilao_test_1


pedra = Arma(20, PedraSeno)
fogo = Arma(1, FogoReto)
pedraTripla = Arma(1, PedraTripla)

vi = Vilao_test_1(800, 300, "../Img/balaoVerde_poo.webp", 200, [pedra, fogo, pedraTripla,])
run(globals())