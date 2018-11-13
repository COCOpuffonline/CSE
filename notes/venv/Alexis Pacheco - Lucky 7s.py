import random
money = 15
rounds = 0
playing = True

while money > 0 and playing:
    money -= 1
    rounds += 1

    if random.randint (1, 6) + random.randint (1, 6) == 7:
        money += 1
        money += 4
    else:
        playing = True
        if money == 0:
            print("Rounds played")
            print(rounds)
            
