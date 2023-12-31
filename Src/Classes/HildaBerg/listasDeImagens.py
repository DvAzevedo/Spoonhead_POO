hildaIntro = []
hildaIntroFinal = []
hildaTornado = []
hildaDash = []
hildaDashIntro = []
hildaSummon = []
dashExplo = []
dashSmoke = []
hildaTransition = ["../../Img/HildaNormal/TransitionToMoon/StartT/blimp_morph_0001.png"]
hildaTornadoAtkIntro = []
hildaTornadoAtk = []
imgListHa = []
touroImgList = []
touroAtkImgList = []
touroStarImgList = []
hildaNormal = []
hildaLaugh = []

for i in range(1, 44):
    hildaIntro.append(f"../../Img/HildaNormal/Intro/blimp_intro_{i:04d}.png")

for i in range(34, 44):
    hildaIntroFinal.append(f"../../Img/HildaNormal/Intro/blimp_intro_{i:04d}.png")

for i in range(1, 22):
    hildaNormal.append(f"../../Img/HildaNormal/Idle/blimp_idle_{i:04d}.png")

for i in range(1, 20):
    hildaLaugh.append(f"../../Img/HildaNormal/Laugh/blimp_shoot_{i:04d}.png")

for i in range(1, 39):
    hildaTornado.append(f"../../Img/HildaNormal/HildaTornado/blimp_tornado_{i:04d}.png")

for i in range(19, 25):
    hildaDash.append(f"../../Img/HildaNormal/Dash/blimp_dash_{i:04d}.png")

for i in range(1, 19):
    hildaDashIntro.append(f"../../Img/HildaNormal/Dash/blimp_dash_{i:04d}.png")

for i in range(1, 22):
    hildaSummon.append(f"../../Img/HildaNormal/Summon/blimp_summon_{i:04d}.png")

for i in range(1, 16):
    dashExplo.append(f"../../Img/HildaNormal/Attaks/DashExplo/blimp_dash_fx_explode_{i:04d}.png")
    
for i in range(1, 7):
    dashSmoke.append(f"../../Img/HildaNormal/Attaks/DashSmoke/blimp_dash_fx_smoke_{i:04d}.png")

for i in range(2, 8):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilA/blimp_morph_{i:04d}.png")

for i in range(8, 10):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/Middle/blimp_morph_{i:04d}.png")
for i in range(10, 14):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilB/blimp_morph_{i:04d}.png")
for i in range(14, 49):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/End/blimp_morph_{i:04d}.png")

for i in range(1, 13):
    hildaTornadoAtkIntro.append(f"../../Img/HildaNormal/Attaks/TornadoIntro/tornado_intro_{i:04d}.png")
for i in range(1, 17):
    hildaTornadoAtk.append(f"../../Img/HildaNormal/Attaks/Tornado/tornado_attack_{i:04d}.png")

 # imagens: 2, 3, 4, 6 estão bugadas
for i in range(1, 2):
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
for i in range(5, 6):
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
for i in range(7, 14):
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_{i:04d}.png")
for i in range(46):
    imgListHa.append(f"../../Img/HildaNormal/Attaks/Ha/blimp_ha_0013.png")

for i in range(1, 17):
    touroImgList.append(f"../../Img/Constelacoes/Touro/taurus_idle_{i:04d}.png")

for i in range(1, 22):
    touroAtkImgList.append(f"../../Img/Constelacoes/TouroAtk/taurus_attack_{i:04d}.png")

for i in range(1, 4):
    touroStarImgList.append(f"../../Img/Constelacoes/TouroStar/taurus_stars_{i:04d}.png")


#/////////////// MOON LISTS ///////////////
    
hildaMoon = []
moonAtkIntro = []
moonAtk = []
moonAtkBack = []
moonSmoke = []
moonDeath = []
estrelaList = []
estrelaPinkList = []

for i in range(1, 14):
    estrelaPinkList.append(f"../../Img/HildaMoon/Proje/luaEstrelaPink/pink_blimp_star_c_{i:04d}.png")

for i in range(1, 17):
    estrelaList.append(f"../../Img/HildaMoon/Proje/blimp_star_a_{i:04d}.png")

for i in range(1, 17):
    hildaMoon.append(f"../../Img/HildaMoon/Idle/blimp_moon_idle_{i:04d}.png")

for i in range(1, 13):
    moonAtkIntro.append(f"../../Img/HildaMoon/AttackIdle/blimp_moon_attack_{i:04d}.png")

for i in range(13, 21):
    moonAtk.append(f"../../Img/HildaMoon/AttackIdle/blimp_moon_attack_{i:04d}.png")

for i in range(13, 21):
    moonAtkBack.append(f"../../Img/HildaMoon/AttackBack/back_blimp_moon_attack_{i:04d}.png")

for i in range(1, 16):
    moonSmoke.append(f"../../Img/HildaMoon/AttackSmoke/blimp_moon_smoke_{i:04d}.png")

for i in range(1, 17):
    moonDeath.append(f"../../Img/HildaMoon/Death/blimp_moon_death_{i:04d}.png")