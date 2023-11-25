from tupy import*
import pygame
from pygame.locals import *
from Classes.Cenario import *
from Classes.MenuInicial import *
from Classes.InicioDeJogo import *
from Classes.Chalice.Chalice import Chalice
from Classes.cena import Cena
from Classes.HildaBerg.HildaBerg import *

''' 
MENSAGEM IMPORTANTE QUANTO A MÚSICA
-A música da gameplay foi movida para o arquivo "InicioDeJogo" dentro da pasta "Classes"
ninguém merece ficar codando ouvindo a música repetidas vezes, por isso se quiser retirar 
 ou alterar a música vá em "InicioDeJogo" que haverá comentários de onde exatamente mexer no código
'''
pygame.init()
#comentar/descomentar as duas linhas abaixo para retirar/colocar a música do menu
pygame.mixer.music.load('Sound/Music/MusicaDoMenu.mp3')
pygame.mixer.music.play(-1)


'''
MENSAGEM IMPORTANTE QUANTOS AOS TRAVAMENTOS
-Eu(tuão) acredito que o tupy não suporta a criação de múltiplas imagens ao mesmo tempo por isso que tanto nos tiros
quanto no menu ocorrem travamentos, afinal são periodos carregados de muitas imagens. 
-Tentei bastante otimizar o menu mas não encontrei nenhuma solução, mas caso vc queira tentar resolver essa ""issue"" vou
deixar um textinho no final do código.
'''
Cenario.criar_cenario()
vilao = HildaBerg(700, 220)
jogador = Chalice(vilao)
cena = Cena(jogador, vilao)

MensagemDeReady = Ready()
TransicaoParaAGameplay = Transicao()
FundoDoMenuInicial = FundoDoMenu()
CupAndMugMenu = CupAndMug()
MensagemDoMenu = PressioneTab()

run(globals())

'''
CONTINUAÇÃO DE (MENSAGEM IMPORTANTE QUANTOS AOS TRAVAMENTOS)
-Basicamente a solução é criar os elementos aos poucos para evitar o travamento do tupy, ou seja, primeiro criar o menu
depois criar os elementos de InicioDeJogo junto com uma parte do cenário, depois criar o resto do cenário e os personagens
todas essas criações devem ser seguidas de "_hide" e depois "_destroy" assim somente os elementos essenciais para a tela 
continuarão no jogo.
-Da forma com está agora todos os elementos são criados atrás do menu, e eles somente são inicializados depois que o menu 
some, da a impressão que cada coisa está sendo criada uma de cada vez, mas tá tudo rodando ao mesmo tempo.
-Não recomendo usar update() na main e coisas que mexem com o tempo como time.sleep() tetentei algumas soluções nesses caminhos mas,
não deu muito certo 
'''