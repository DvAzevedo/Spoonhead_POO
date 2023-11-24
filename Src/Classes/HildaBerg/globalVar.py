from Classes.Animacao import *
from Classes.HildaBerg.listasDeImagens import *

Y_POSITION_ORIGIN = 240
X_POSITION_ORIGIN = 700

QTD_IMGS_STATE_NORMAL = 21
QTD_IMGS_STATE_LAUGH = 19
QTD_IMGS_STATE_INTRO = 43
QTD_IMGS_STATE_INTRO_FINAL = 9
QTD_IMGS_STATE_TRANSITION = 48
QTD_IMGS_STATE_TORNADO = 38
QTD_IMGS_STATE_DASH_INTRO = 18
QTD_IMGS_STATE_DASH = 6
QTD_IMGS_STATE_SUMMON = 21

QTD_IMGS_STATE_TOURO = 16
QTD_IMGS_STAR_TOURO = 3
QTD_IMGS_ATK_TOURO = 21

QTD_IMGS_ATK_HA = 46
QTD_IMGS_ATK_TORNADO = 16
QTD_IMGS_ATK_TORNADO_INTRO = 12
QTD_IMGS_ATK_DASH_EXPLO = 15
QTD_IMGS_ATK_DASH_SMOKE = 6
ANIME_DELAY = 2

STATE_LIST = ["intro", "normal", "laugh", "tornado", "dashIntro", "dash", "summon", "touro", "touroAtk", "transition"]

introAnime = Animacao(QTD_IMGS_STATE_INTRO, hildaIntro, ANIME_DELAY, True, "normal")
introFinalAnime = Animacao(QTD_IMGS_STATE_INTRO_FINAL, hildaIntroFinal, ANIME_DELAY, True, "normal")
normalAnime = Animacao(QTD_IMGS_STATE_NORMAL, hildaNormal, ANIME_DELAY)
laughAnime = Animacao(QTD_IMGS_STATE_LAUGH, hildaLaugh, 1, True, "normal")
transitionAnime = Animacao(QTD_IMGS_STATE_TRANSITION, hildaTransition, ANIME_DELAY)
tornadoAnime = Animacao(QTD_IMGS_STATE_TORNADO, hildaTornado, 1, True, "normal")
dashIntroAnime = Animacao(QTD_IMGS_STATE_DASH_INTRO, hildaDashIntro, 1, True, "dash")
dashAnime = Animacao(QTD_IMGS_STATE_DASH, hildaDash, ANIME_DELAY)
summonAnime = Animacao(QTD_IMGS_STATE_SUMMON, hildaSummon, ANIME_DELAY)
touroAnime = Animacao(QTD_IMGS_STATE_TOURO, touroImgList, ANIME_DELAY)
touroAtkAnime = Animacao(QTD_IMGS_ATK_TOURO, touroAtkImgList, 1, True, "touro")

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


STATE_LIST = ["intro", "normal", "laugh", "tornado", "dashIntro", "dash", "summon", "touro", "touroAtk", "transition"]

STATE_DIC = {
    "intro": introAnime,
    "introFinal": introFinalAnime,
    "normal": normalAnime,
    "laugh": laughAnime,
    "tornado": tornadoAnime,
    "dashIntro": dashIntroAnime,
    "dash": dashAnime,
    "summon": summonAnime,
    "touro": touroAnime,
    "touroAtk": touroAtkAnime,
    "transition": transitionAnime,
    "moon_idle": moon_idleAnime,
    "moon_atkIntro": moon_atkIntroAnime,
    "moon_atk": moon_atkAnime,
    "moon_atkBack": moon_atkBackAnime,  
    "moon_smoke": moon_smokeAnime,
    "moon_death": moon_deathAnime
} 
