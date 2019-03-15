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


class BrowningHipoint(Weapon):
    def __init__(self):
        super(BrowningHipoint, self).__init__("Browning_Hi_point", 21, 97)

    def shoot(self):
        self.durability -= 3
        print("You shoot your pistol.")


class Rustyscissors(Weapon):
    def __init__(self):
        super(Rustyscissors, self).__init__("rusty_Scissors", 3, 32)


class P90BShot(Weapon):
    def __init__(self):
        super(P90BShot, self).__init__("P90_B_Shot", 29, 147)

    def shoot(self):
        self.durability -= 4
        print("Your guns durability went down.")


class Spoon(Weapon):
    def __init__(self):
        super(Spoon, self).__init__("spoon", 40, 400)


class Armor(Item):
    def __init__(self, name, defence, durability):
        super(Armor, self).__init__(name)
        self.defence = defence
        self.durability = durability


class Woodenchestplate(Armor):
    def __init__(self):
        super(Woodenchestplate, self).__init__("wooden chest plate", 10, 25)


class Woodenhelmet(Armor):
    def __init__(self):
        super(Woodenhelmet, self).__init__("wooden helmet", 5, 20)


class Woodenleggings(Armor):
    def __init(self):
        super(Woodenleggings, self).__init__("wooden leggings", 10, 25)


class Steelchestplate(Armor):
    def __init__(self):
        super(Steelchestplate, self).__init__("steel chest plate", 20, 50)


class Steelhelmet(Armor):
    def __init__(self):
        super(Steelhelmet, self).__init__("steel helmet", 15, 40)


class Steelleggings(Armor):
    def __init__(self):
        super(Steelleggings, self).__init__("steel leggings", 20, 45)


class Potion(Item):
    def __init__(self, name, health_healed, shield, attack_potion):
        super(Potion, self).__init__(name)
        self.health_healed = health_healed
        self.shield = shield
        self.attack_potion = attack_potion


class Healthpotion(Potion):
    def __init__(self):
        super(Healthpotion, self).__init__("health_potion", 25, 0, 0)


class Shieldpotion(Potion):
    def __init__(self):
        super(Shieldpotion, self).__init__("shield potion", 0, 25, 0)


class Attackpotion(Potion):
    def __init__(self):
        super(Attackpotion, self).__init__("attack potion", 0, 0, 20)


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.defence > damage:
            print("You take no damage just because.")
        else:
            self.health -= damage - self.armor.defence
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %s health left" % (self.name, self.health))

    def attack(self, target):
        if target.health <= 0:
            print("They are already dead.")
            return
        print("%s attacks %s for %s damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
P90_B_Shot = Weapon("P90 burst shot", 40, 600)
spoon = Weapon("Spoon", 400, 400)
steel_chest_plate = Armor("steel_chest_plate", 40, 500)

# Characters
orc = Character("Orc1", 100, P90_B_Shot, Armor("Steel chest plate", 40, 500))
orc2 = Character("Wiebe", 10000, spoon, steel_chest_plate)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
