class Room(object):
    def __init__(self, name, north, south, east, west, up, down, item, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.item = item
        self.description = description


class Player(object):
    def __init__(self, starting_location, health, shield):
        self.current_location = starting_location
        self.health = health
        self.shield = shield
        self.inventory = []

    def move(self, new_location):

        self.current_location = new_location

    def find_next_room(self, direction):

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
knife = Weapon("Knife", 7, 76)
browningHipoint = Weapon("Browning Hi Point", 21, 97)
rustyscissors = Weapon("Rusty Scissors", 3, 32)
p90BShot = Weapon("P90 Burst Shot", 29, 147)
spoon = Weapon("Spoon", 40, 400)
claw = Weapon("Claw", 4, 9999999999)
fist = Weapon("Fist", 1, 9999999999)

# Armor
woodenchestplate = Armor("Wooden Chest Plate", 10, 25)
woodenhelmet = Armor("Wooden Helmet", 5, 20)
woodenleggings = Armor("Wooden Leggings", 10, 25)
steelchestplate = Armor("Steel Chest Plate", 20, 50)
steelhelmet = Armor("Steel Helmet", 15, 40)
steelleggings = Armor("Steel Leggings", 20, 45)

# Potion
healthpotion = Potion("Health potion", 25, 0, 0)
shieldpotion = Potion("Shield potion", 0, 25, 0)
attackpotion = Potion("Attack potion", 0, 0, 25)

# Characters                    # Weap.         # Dam. # Dura.
molded = Character("Molded", 100, Claw, Armor("", None, None))
molded2 = Character("Molded", 100, None, Armor("", None, None))


MAIN_ROOM = Room('Main Room', None, None, 'SECRET_ROOM', 'HALLWAY_2', None, None, 'BrowningHipoint()',
                                                                                  "You wake up in a very filthy room "
                                                                                  "and you do not remember"
                                                                                  " how you got there. There is a "
                                                                                  "couch in the middle of the room"
                                                                                  "and a chimney that has not been"
                                                                                  " used.")
SECRET_ROOM = Room('Secret room', None, 'BASEMENT', None, 'MAIN_ROOM', None, None, 'Rustyscissors()',
                                                                                   "You are in a small room and notice "
                                                                                   "a small table on your left and on "
                                                                                   "your right"
                                                                                   " you see a hole in the floor.")
HALLWAY_2 = Room('Hallway', 'KITCHEN', 'HALLWAY_1', None, 'STORAGE_ROOM_1', None, None, None,
                                                                                        "To the north you see a door, "
                                                                                        "on the south side there is "
                                                                                        "another door, and to the west "
                                                                                        "is a room without a door.")
KITCHEN = Room('Kitchen', None, None, 'HALLWAY_2', 'HALLWAY_3', None, None, 'Knife()',
                                                                            "In the kitchen you see a cabinet with "
                                                                            "two drawers on the south side."
                                                                            "To the north is a very dirty "
                                                                            "refrigerator.")
STORAGE_ROOM_1 = Room('Storage room 1', None, None, 'HALLWAY_2', None, None, None, 'P90BShot()',
                                                                                   "You see a door that is boarded up "
                                                                                   "and cannot be pried open."
                                                                                   "You also notice a self with "
                                                                                   "some items on it")
HALLWAY_1 = Room('Hallway 1', 'STORAGE_ROOM_2', 'BATHROOM', 'STAIRS', None, None, None, None,
                                                                                "There are three doors one to "
                                                                                "the north, one to the south, "
                                                                                "and one on the east.")
STORAGE_ROOM_2 = Room('Storage room 2', None, 'HALLWAY_1', None, None, None, None, 'Healthpotion()',
                                                                                "All around you are shelves with "
                                                                                "items on them.")
BATHROOM = Room('Bathroom', 'HALLWAY_1', None, None, None, None, None, 'Spoon()',
                                                                       "You are in a filthy bathroom and hear water "
                                                                       "running.")
HALLWAY_3 = Room('Hallway 3', None, None, 'KITCHEN', None, None, None, None, "To the south you see a door and you also "
                                                                             "notice a cabinet on the west.")
STAIRS = Room('Stairs', None, None, None, None, 'HALLWAY_1', 'BASEMENT_SUPPLY_ROOM', None,
                                                                                     "You are now in the middle of the"
                                                                                     "stairs, you can go back up to "
                                                                                     "the first floor or go down to "
                                                                                     "the basement.")
BM_SECRET_ROOM = Room('BM Secret Room', None, 'PRISON_ROOM', None, None, 'SECRET_ROOM', None, 'Steelchestplate()',
                                                                                              "The room is slightly"
                                                                                              " flood up to your "
                                                                                              "ankles and there are "
                                                                                              "a few bodies on a table"
                                                                                              "which stink.")
PRISON_ROOM = Room('Prison room', 'SECRET_ROOM', None, None, 'WORK_SHOP', None, None, 'Shieldpotion()',
                                                                                      "It is dark and there are two "
                                                                                      "shelves")
WORK_ROOM = Room('Work room', None, 'DISSECTION_ROOM', 'PRISON_ROOM', None, None, None, 'Woodenhelmet()',
                                                                                        "You have reached the work "
                                                                                        "room and notice a few tools "
                                                                                        "on the bench which you can "
                                                                                        "you.")
DISSECTION_ROOM = Room('Dissection room', 'WORK_SHOP', None, 'HALLWAY_4', None, None, None, 'Attackpotion()',
                                                                                            "You are in a damp room "
                                                                                            "which smells awful.")
HALLWAY_4 = Room('Hallway 4', 'LIVING_ROOM', None, None, 'DISSECTION_ROOM', None, None, None,
                                                                                        "You are in a dark hallway, "
                                                                                        "to the west is the dissection "
                                                                                        "room and at the north side "
                                                                                        "is another door.")
LIVING_ROOM = Room('Living room', 'HALLWAY_5', 'HALLWAY_4', None, None, None, None, 'Woodenchestplate()',
                                                                                    "This room is oddly dry and "
                                                                                    "has furniture.")
HALLWAY_5 = Room('Hallway 5', None, 'LIVING_ROOM', None, 'BASEMENT_SUPPLY_ROOM', None, None, None,
                                                                                             "You can see two doors, "
                                                                                             "on the west side you see"
                                                                                             " a door with a little "
                                                                                             "light coming out, and"
                                                                                             " to the east is another "
                                                                                             "room.")
BASEMENT_SUPPLY_ROOM = Room('Basement supply room', 'BODY_STORAGE_ROOM', 'STAIRS', 'HALLWAY_5', None, None, None,
                            'Woodenleggings()',
                            "The stench in this room is awful and it is extremely dark."
                            " You also hear weird noises on the ceiling.")
BODY_STORAGE_ROOM = Room('Body storage room', None, 'BASEMENT_TOOL_STORAGE', 'BASEMENT_TOOL_STORAGE', None, None, None,
                         'Steelleggings()',
                         "You notice a two body bags on a table on is open and the other is not.")
TOOL_STORAGE_ROOM = Room('Tool room', None, None, None, 'BODY_STORAGE_ROOM', None, None, 'Steelhelmet()',
                                                                                         "There are a whole bunch of"
                                                                                         " tool that you can use but "
                                                                                         "they are in locked tool"
                                                                                         " boxes.")
world_map = {
    'MAIN_ROOM': {
        'NAME': "Main Room",
        'DESCRIPTION': "You wake up in a very filthy room and you do not remember how you got there."
                       "There is a couch in the middle of the room and a chimney that has not been used in a while.",
        'PATHS': {
            'EAST': "SECRET_ROOM",
            'WEST': "HALLWAY_2"
        }
    },
    'SECRET_ROOM': {
        'NAME': "Secret room",
        'DESCRIPTION': "You are in a small room and notice a small table on your left and on your right"
                       " you see a hole in the floor.",
        'PATHS': {
            'WEST': 'MAIN_ROOM',
            'DOWN': 'BM_SECRET_ROOM'
        }
    },
    'HALLWAY_2': {
        'NAME': "Hallway 2",
        'DESCRIPTION': "To the north you see a door, on the south side there is another door, and to the west is "
                       "a room without a door.",
        'PATHS': {
            'NORTH': 'KITCHEN',
            'SOUTH': 'HALLWAY_1',
            'WEST': 'STORAGE_ROOM_1',
            'EAST': 'MAIN_ROOM'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "In the kitchen you see a cabinet with two drawers on the south side."
                       "To the north is a very dirty refrigerator.",
        'PATHS': {
            'WEST': 'HALLWAY_3',
            'EAST': 'HALLWAY_2'
        }
    },
    'STORAGE_ROOM_1': {
        'NAME': 'Storage room 1',
        'DESCRIPTION': "You see a door that is boarded up and cannot be pried open."
                       "You also notice a self with some items on it",
        'PATHS': {
            'EAST': 'HALLWAY_2'
        }
    },
    'HALLWAY_1': {
        'NAME': 'Hallway 1',
        'DESCRIPTION': "There are three doors one to the north, one to the south, and one on the east.",
        'PATHS': {
            'NORTH': 'STORAGE_ROOM_2',
            'SOUTH': 'BATHROOM',
            'EAST': 'STAIRS'
        }
    },
    'STORAGE_ROOM_2': {
        'NAME': 'Storage room 2',
        'DESCRIPTION': "All around you are shelves with items on them.",
        'PATHS': {
            'SOUTH': 'HALLWAY_1',
        }
    },
    'BATHROOM': {
        'NAME': 'Bathroom',
        'DESCRIPTION': "You are in a filthy bathroom and hear water running.",
        'PATHS': {
            'NORTH': 'HALLWAY_1'
        }
    },
    'HALLWAY_3': {
        'NAME': 'Hallway 3',
        'DESCRIPTION': "To the south you see a door and you also notice a cabinet on the west.",
        'PATHS': {
            'EAST': 'KITCHEN',
        }
    },
    'STAIRS': {
        'NAME': 'Stairs',
        'DESCRIPTION': "You are now in the middle of the stairs,"
                       " you can go back up to the first floor"
                       " or go down to the basement.",
        'PATHS': {
            'DOWN': 'BASEMENT_SUPPLY_ROOM',
            'UP': 'HALLWAY_1'
        }
    },
    'BM_SECRET_ROOM': {
        'NAME': 'BM Secret Room',
        'DESCRIPTION': "The room is slightly flood up to your "
                       "ankles and there are a few bodies on a table ",
                       "which stink."
        'PATHS': {
            'UP': 'SECRET_ROOM',
            'SOUTH': 'PRISON_ROOM'
        }
    },
    'PRISON_ROOM': {
        'NAME': 'Prison room',
        'DESCRIPTION': "It is dark and there are two shelves",
        'PATHS': {
            'NORTH': 'SECRET_ROOM',
            'WEST': 'WORK_ROOM'
        }
    },
    'WORK_ROOM': {
        'NAME': 'Work room',
        'DESCRIPTION': "You have reached the work room and"
                       "notice a few tools on the bench "
                       "which you can you.",
        'PATHS': {
            'EAST': 'PRISON_ROOM',
            'SOUTH': 'DISSECTION_ROOM'
        }
    },
    'DISSECTION_ROOM': {
        'NAME': 'Dissection room',
        'DESCRIPTION': "You are in a damp room which smells awful.",
        'PATHS': {
            'NORTH': 'WORK_ROOM',
            'EAST': 'HALLWAY_4'
        }
    },
    'HALLWAY_4': {
        'NAME': 'Hallway 4',
        'DESCRIPTION': "You are in a dark hallway, to the west is the dissection room"
                       " and at the north side is another door.",
        'PATHS': {
            'WEST': 'DISSECTION_ROOM',
            'NORTH': 'LIVING_ROOM'
        }
    },
    'LIVING_ROOM': {
        'NAME': 'Living room',
        'DESCRIPTION': "This room is oddly dry and has furniture.",
        'PATHS': {
            'SOUTH': 'HALLWAY_4',
            'NORTH': 'HALLWAY_5'
        }
    },
    'HALLWAY_5': {
        'NAME': 'Hallway 5',
        'DESCRIPTION': "You can see two doors, on the west side you see"
                       " a door with a little light coming out, and to the"
                       " east is another room.",
        'PATHS': {
            'EAST': 'LIVING_ROOM',  # THIS MAY BE SOUTH
            'WEST': 'BASEMENT_SUPPLY_ROOM'
        }
    },
    'BASEMENT_SUPPLY_ROOM': {
        'NAME': 'Basement supply room',
        'DESCRIPTION': "The stench in this room is awful and it is extremely dark."
                       " You also hear weird noises on the ceiling.",
        'PATHS': {
            'SOUTH': 'STAIRS',
            'NORTH': 'BODY_STORAGE_ROOM',
            'EAST': 'HALLWAY_5'
        }
    },
    'BODY_STORAGE_ROOM': {
        'NAME': 'Body storage room',
        'DESCRIPTION': "You notice a two body bags on a table one is open and the other is not.",
        'PATHS': {
            'SOUTH': 'BASEMENT_SUPPLY_ROOM',
            'EAST': 'BASEMENT_TOOL_STORAGE'
        }
    },
    'TOOL_STORAGE_ROOM': {
        'NAME': 'Tool room',
        'DESCRIPTION': "There are a whole bunch of tool that you can use but they"
                       " are in locked tool boxes.",
        'PATHS': {
            'WEST': 'BODY_STORAGE_ROOM'
        }
    }
}
                           # H # S
player = Player(MAIN_ROOM, 100, 25)

item = True
playing = True
current_node = world_map['MAIN_ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
actions = ['PICK UP', 'ATTACK', 'DROP', 'EAT' ]

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
        except AttributeError:
            pass
    elif command.lower() in ['i', 'inventory']:
        print("Your current inventory is:")
        print(list(player.inventory))
    elif command.lower() in ['pick up']:
        print("You picked the item.")
        player.inventory = []
        player.inventory.append(player.current_location.item.name)
        print(list(player.inventory))
        item = False
    else:
        print("Command Not Found")
