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


class rusty_Scissors(Weapon):
    def __init__(self):
        super(rusty_Scissors, self).__init__("rusty_Scissors", 3, 32)

class P90(Weapon):
    def __init__(self):
        super(P90, self).__init__("P90", 29, 147)

# Work on this later
class Potion(Item):
    def __init__(self, name, health_healed):
        super(Potion, self).__init__(name)
        self.health_healed = health_healed

    def drink_potion(self):
        self.health_healed = h

