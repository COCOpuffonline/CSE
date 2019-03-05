class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = 100

    def swing_weapon(self):
        self.durability -= 5
        print("You swing your weapon with great force and damage it in return.")


class Knife(Weapon):
    def __init__(self):                   # Dam. Dura.
        super(Knife, self).__init__("Knife", 4, 76)

class Browning_Hi_point(Weapon):
    def __init__(self):
        super(Browning_Hi_point, self).__init__("Browning_Hi_point", 13, 100)
