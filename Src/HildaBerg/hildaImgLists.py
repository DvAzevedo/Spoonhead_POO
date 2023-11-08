
hildaIntro = ["../../Img/HildaNormal/Intro/blimp_intro_0001.png"]
for i in range(2, 44):
    hildaIntro.append(f"../../Img/HildaNormal/Intro/blimp_intro_{i:04d}.png")

hildaNormal = ["../../Img/HildaNormal/Idle/blimp_idle_0001.png"]
for i in range(2, 22):
    hildaNormal.append(f"../../Img/HildaNormal/Idle/blimp_idle_{i:04d}.png")

hildaTransition = ["../../Img/HildaNormal/TransitionToMoon/Start/blimp_morph_0001.png"]
for i in range(2, 8):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilA/blimp_morph_{i:04d}.png")
for i in range(8, 10):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/Middle/blimp_morph_{i:04d}.png")
for i in range(10, 14):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilB/blimp_morph_{i:04d}.png")
for i in range(14, 49):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/End/blimp_morph_{i:04d}.png")

hildaMoon = ["../../Img/HildaMoon/Idle/blimp_moon_idle_0001.png"]
for i in range(2, 17):
    hildaMoon.append(f"../../Img/HildaMoon/Idle/blimp_moon_idle_{i:04d}.png")
