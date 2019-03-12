class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def use_weapon(self):
        self.durability -= 5
        print("You use your weapon and its durability drops.")


class Knife(Weapon):
    def __init__(self):                   # Dam. Dura.
        super(Knife, self).__init__("Knife", 7, 76)


class Browning_Hi_point(Weapon):
    def __init__(self):
        super(Browning_Hi_point, self).__init__("Browning_Hi_point", 21, 97)

    def shoot(self):
        self.durability -= 3
        print("You shoot your pistol.")


class rusty_Scissors(Weapon):
    def __init__(self):
        super(rusty_Scissors, self).__init__("rusty_Scissors", 3, 32)


class P90_B_Shot(Weapon):
    def __init__(self):
        super(P90_B_Shot, self).__init__("P90_B_Shot", 29, 147)

    def shoot(self):
        self.durability -= 4
        print("Your guns durability went down.")


class spoon(Weapon):
    def __init__(self):
        super(spoon, self).__init__("spoon", 40, 400)


class Armor(Item):
    def __init__(self, name, defence, durability):
        super(Armor, self).__init__(name)
        self.defence = defence
        self.durability = durability


class wooden_chest_plate(Armor):
    def __init__(self):
        super(wooden_chest_plate, self).__init__("wooden chest plate", 10, 25)


class wooden_helmet(Armor):
    def __init__(self):
        super(wooden_helmet, self).__init__("wooden helmet", 5, 20)


class wooden_leggings(Armor):
    def __init(self):
        super(wooden_leggings, self).__init__("wooden leggings", 10, 25)



class steel_chest_plate(Armor):
    def __init__(self):
        super(steel_chest_plate, self).__init__("steel chest plate", 20, 50)

class steel_helmet(Armor):
    def __init__(self):
        super(steel_helmet, self).__init__("steel helmet", 15, 40)


class steel_leggings(Armor):
    def __init__(self):
        super(steel_leggings, self).__init__("steel leggings", 20, 45)


class Potion(Item):
    def __init__(self, name, health_healed, shield, attack_potion):
        super(Potion, self).__init__(name)
        self.health_healed = health_healed
        self.shield = shield
        self.attack_potion = attack_potion


class health_potion(Potion):
    def __init__(self):
        super(health_potion, self).__init__("health_potion", 25, 0, 0)


class shield_potion(Potion):
    def __init__(self):
        super(shield_potion, self).__init__("shield potion", 0, 25, 0)


class attack_potion(Potion):
    def __init__(self):
        super(attack_potion, self).__init__("attack potion", 0, 0, 20)
