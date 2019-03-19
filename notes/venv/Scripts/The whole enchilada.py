class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room object id it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


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


class Fist(Weapon):
    def __init__(self):
        super(Fist, self).__init__("fist", 1, 999999999999)


class Claw(Weapon):
    def __init__(self):
        super(Claw, self).__init__("claw", 4, 999999999999)


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


# Weapons
Knife = Weapon("Knife", 7, 76)
BrowningHipoint = Weapon("Browning Hi Point", 21, 97)
Rustyscissors = Weapon("Rusty Scissors", 3, 32)
P90BShot = Weapon("P90 Burst Shot", 29, 147)
Spoon = Weapon("Spoon", 40, 400)
Claw = Weapon("Claw", 4, 9999999999)
Fist = Weapon("Fist", 1, 9999999999)

# Armor
Woodenchestplate = Armor("Wooden Chest Plate", 10, 25)
Woodenhelmet = Armor("Wooden Helmet", 5, 20)
Woodenleggings = Armor("Wooden Leggings", 10, 25)
Steelchestplate = Armor("Steel Chest Plate", 20, 50)
Steelhelmet = Armor("Steel Helmet", 15, 40)
Steelleggings = Armor("Steel Leggings", 20, 45)

# Potion
Healthpotion = Potion("Health potion", 25, 0, 0)
Shieldpotion = Potion("Shield potion", 0, 25, 0)
Attackpotion = Potion("Attack potion", 0, 0, 25)

# Characters
molded = Character("Molded", 100, None, Armor("", None, None))
molded2 = Character("Molded", 100, None, Armor("", None, None))

orc = Character("Orc1", 100, P90BShot, Armor("Steel chest plate", 40, 500))
orc2 = Character("Wiebe", 10000, Spoon, Steelchestplate)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)


MAIN_ROOM = Room('Main Room', None, None, 'SECRET_ROOM', 'HALLWAY_2', None, None, "You wake up in a very filthy room "
                                                                                  "and you do not remember"
                                                                                  " how you got there. There is a "
                                                                                  "couch in the middle of the room"
                                                                                  "and a chimney that has not been"
                                                                                  "")
SECRET_ROOM = Room('Secret room', None, 'BASEMENT', None, 'MAIN_ROOM', None, None, "You are in a small room and notice "
                                                                                   "a small table on your left and on "
                                                                                   "your right"
                                                                                   " you see a hole in the floor.")
HALLWAY_2 = Room('Hallway', 'KITCHEN', 'HALLWAY_1', None, 'STORAGE_ROOM_1', None, None, "To the north you see a door, "
                                                                                        "on the south side there is "
                                                                                        "another door, and to the west "
                                                                                        "is a room without a door.")
KITCHEN = Room('Kitchen', None, None, 'HALLWAY_2', 'HALLWAY_3', None, None,  "In the kitchen you see a cabinet with "
                                                                             "two drawers on the south side."
                                                                             "To the north is a very dirty "
                                                                             "refrigerator.")
STORAGE_ROOM_1 = Room('Storage room 1', None, None, 'HALLWAY_2', None, None, None, "You see a door that is boarded up "
                                                                                   "and cannot be pried open."
                                                                                   "You also notice a self with "
                                                                                   "some items on it")
HALLWAY_1 = Room('Hallway 1', 'STORAGE_ROOM_2', 'BATHROOM', 'STAIRS', None, None, None, "There are three doors one to "
                                                                                        "the north, one to the south, "
                                                                                        "and one on the east.")
STORAGE_ROOM_2 = Room('Storage room 2', None, 'HALLWAY_1', None, None, None, None, "All around you are shelves with "
                                                                                   "items on them.")
BATHROOM = Room('Bathroom', 'HALLWAY_1', None, None, None, None, None, "You are in a filthy bathroom and hear water "
                                                                       "running.")
HALLWAY_3 = Room('Hallway 3', None, None, 'KITCHEN', None, None, None, "To the south you see a door and you also "
                                                                       "notice a cabinet on the west.")
STAIRS = Room('Stairs', None, None, None, None, 'HALLWAY_1', 'BASEMENT_SUPPLY_ROOM', "You are now in the middle of the"
                                                                                     "stairs, you can go back up to "
                                                                                     "the first floor or go down to "
                                                                                     "the basement.")
BM_SECRET_ROOM = Room('BM Secret Room', None, 'PRISON_ROOM', None, None, 'SECRET_ROOM', None, "The room is slightly"
                                                                                              " flood up to your "
                                                                                              "ankles and there are "
                                                                                              "a few bodies on a table"
                                                                                              "which stink.")
PRISON_ROOM = Room('Prison room', 'SECRET_ROOM', None, None, 'WORK_SHOP', None, None, "It is dark and there are two "
                                                                                      "shelves")
WORK_ROOM = Room('Work room', None, 'DISSECTION_ROOM', 'PRISON_ROOM', None, None, None, "You have reached the work "
                                                                                        "room and notice a few tools "
                                                                                        "on the bench which you can "
                                                                                        "you.")
DISSECTION_ROOM = Room('Dissection room', 'WORK_SHOP', None, 'HALLWAY_4', None, None, None, "You are in a damp room "
                                                                                            "which smells awful.")
HALLWAY_4 = Room('Hallway 4', 'LIVING_ROOM', None, None, 'DISSECTION_ROOM', None, None, "You are in a dark hallway, "
                                                                                        "to the west is the dissection "
                                                                                        "room and at the north side "
                                                                                        "is another door.")
LIVING_ROOM = Room('Living room', 'HALLWAY_5', 'HALLWAY_4', None, None, None, None, "This room is oddly dry and "
                                                                                    "has furniture.")
HALLWAY_5 = Room('Hallway 5', None, 'LIVING_ROOM', None, 'BASEMENT_SUPPLY_ROOM', None, None, "You can see two doors, "
                                                                                             "on the west side you see"
                                                                                             " a door with a little "
                                                                                             "light coming out, and"
                                                                                             " to the east is another "
                                                                                             "room.")
BASEMENT_SUPPLY_ROOM = Room('Basement supply room', 'BODY_STORAGE_ROOM', 'STAIRS', 'HALLWAY_5', None, None, None,
                            "The stench in this room is awful and it is extremely dark."
                            " You also hear weird noises on the ceiling.")
BODY_STORAGE_ROOM = Room('Body storage room', None, 'BASEMENT_TOOL_STORAGE', 'BASEMENT_TOOL_STORAGE', None, None, None,
                         "You notice a two body bags on a table on is open and the other is not.")
TOOL_STORAGE_ROOM = Room('Tool room', None, None, None, 'BODY_STORAGE_ROOM', None, None, "There are a whole bunch of"
                                                                                         " tool that you can use but "
                                                                                         "they are in locked tool"
                                                                                         " boxes.")

