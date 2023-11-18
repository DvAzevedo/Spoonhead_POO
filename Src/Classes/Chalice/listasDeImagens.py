
ChaliceNormal = []
for i in range(1, 7):
    ChaliceNormal.append(f"../Img/Chalice/Test{i:0d}.png")
    
ChaliceTransitionToSpecial = []
for i in range(1, 19):
    ChaliceTransitionToSpecial.append(f"../Img/Chalice/Special/chalice_shmup_super_intro_{i:04d}.png")

ChaliceSpecial = []
for i in range(1, 5):
    ChaliceSpecial.append(f"../Img/Chalice/Special/chalice_shmup_super_idle_straight_{i:04d}.png")

ChaliceExplosion = []
for i in range(1, 28):
    ChaliceExplosion.append(f"../Img/Chalice/Special/Explosion/shmup_super_explode_{i:04d}.png")

BulletMove = []
for i in range(1,5):
    BulletMove.append(f"../Img/Chalice/Bullet/chalice_shmup_3way_bullet_a_{i:04d}.png")

BulletMove_typeA = []
for i in range(1,5):
    BulletMove_typeA.append(f"../Img/Chalice/Bullet/TripleShoot/TypeA/chalice_shmup_3way_bullet_a_{i:04d}.png")

BulletMove_typeB = []
for i in range(1,5):
    BulletMove_typeB.append(f"../Img/Chalice/Bullet/TripleShoot/TypeB/chalice_shmup_3way_bullet_b_{i:04d}.png")

BulletMove_typeC = []
for i in range(1,5):
    BulletMove_typeC.append(f"../Img/Chalice/Bullet/TripleShoot/TypeC/chalice_shmup_3way_bullet_c_{i:04d}.png")

BulletDict = [BulletMove_typeA,BulletMove_typeB,BulletMove_typeC]

MiniBombMove = []
for i in range(1,9):
    MiniBombMove.append(f"../Img/Chalice/Mini_Bomb/TypeA/weapon_minibomb_bullets_a_{i:04d}.png")

HP_bar = []
for i in range(1,5):
    HP_bar.append(f"../Img/Chalice/Life/hp_{i:02d}.png")
    if i == 1:
        alter = ["critical","lowlevel","dead"]
        for word in alter:
            HP_bar.append(f"../Img/Chalice/Life/hp_{i:02d}_{word}.png")