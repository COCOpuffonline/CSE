class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Knife(Weapon):
    def __init__(self):                   # Dam. Dura.
        super(Knife, self).__init__("Knife", 7)


class BrowningHipoint(Weapon):
    def __init__(self):
        super(BrowningHipoint, self).__init__("BrowningHipoint", 21)


class Rustyscissors(Weapon):
    def __init__(self):
        super(Rustyscissors, self).__init__("Rustyscissors", 5)


class P90BShot(Weapon):
    def __init__(self):
        super(P90BShot, self).__init__("P90BShot", 29)


class Spoon(Weapon):
    def __init__(self):
        super(Spoon, self).__init__("Spoon", 40)


class Claw(Weapon):
    def __init__(self):
        super(Claw, self).__init__("Claw", 5)


class Fist(Weapon):
    def __init__(self):
        super(Fist, self).__init__("Fist", 3)


class Armor(Item):
    def __init__(self, name, defence):
        super(Armor, self).__init__(name)
        self.defence = defence


class Woodenchestplate(Armor):
    def __init__(self):
        super(Woodenchestplate, self).__init__("Woodenchestplate", 10)


class Woodenhelmet(Armor):
    def __init__(self):
        super(Woodenhelmet, self).__init__("Woodenhelmet", 5)


class Woodenleggings(Armor):
    def __init(self):
        super(Woodenleggings, self).__init__("Woodenleggings", 10)


class Steelchestplate(Armor):
    def __init__(self):
        super(Steelchestplate, self).__init__("Steelchestplate", 20)


class Steelhelmet(Armor):
    def __init__(self):
        super(Steelhelmet, self).__init__("Steelhelmet", 15)


class Steelleggings(Armor):
    def __init__(self):
        super(Steelleggings, self).__init__("Steelleggings", 20)


class Potion(Item):
    def __init__(self, name, health_healed, shield, attack_boost):
        super(Potion, self).__init__(name)
        self.health_healed = health_healed
        self.shield = shield
        self.attack_boost = attack_boost


class Healthpotion(Potion):
    def __init__(self):
        super(Healthpotion, self).__init__("Healthpotion", 25, 0, 0)


class Shieldpotion(Potion):
    def __init__(self):
        super(Shieldpotion, self).__init__("Shieldpotion", 0, 25, 0)


class Attackpotion(Potion):
    def __init__(self):
        super(Attackpotion, self).__init__("Attackpotion", 0, 0, 25)


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


class Room(object):

    def __init__(self, name, north, south, east, west, up, down, description, item):
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


# Items
Knife = Weapon(7, Knife)
browningHipoint = Weapon(21, BrowningHipoint)
rustyscissors = Weapon(5, Rustyscissors)
p90BShot = Weapon(29, P90BShot)
spoon = Weapon(40, Spoon)
claw = Weapon(5, Claw)
fist = Weapon(3, Fist)

# Armor
woodenchestplate = Armor(10, Woodenchestplate)
woodenhelmet = Armor(5, Woodenhelmet)
woodenleggings = Armor(10, Woodenleggings)
steelchestplate = Armor(20, Steelchestplate)
steelhelmet = Armor(15, Steelhelmet)
steelleggings = Armor(20, Steelleggings)

# Potion
healthpotion = Potion(0, 25, Healthpotion, 0)
shieldpotion = Potion(0, 0, Shieldpotion, 25)
attackpotion = Potion(25, 0, Attackpotion, 0)

# Characters                    # Weap.         # Dam. # Dura.
molded = Character("Molded", 100, "claw", Armor("", 4))
molded2 = Character("Molded", 100, "claw", Armor("", None))


MAIN_ROOM = Room('Main Room', None, None, 'SECRET_ROOM', 'HALLWAY_2', None, None, "You wake up in a very filthy room "
                                                                                  "and you do not remember how you "
                                                                                  "got there. There is a "
                                                                                  "couch in the middle of the room"
                                                                                  "and a chimney that has not been"
                                                                                  " used.", 'BrowningHipoint')
SECRET_ROOM = Room('Secret room', None, 'BASEMENT', None, 'MAIN_ROOM', None, None, "You are in a small room and notice "
                                                                                   "a small table on your left and on "
                                                                                   "your right"
                                                                                   " you see a hole in the floor.",
                                                                                   'Rusty scissors')
HALLWAY_2 = Room('Hallway', 'KITCHEN', 'HALLWAY_1', None, 'STORAGE_ROOM_1', None, None, None, "To the north you see a "
                                                                                              "door, on the south side"
                                                                                              " there is another door,"
                                                                                              " and to the west is a"
                                                                                              " room without a door.")
KITCHEN = Room('Kitchen', None, None, 'HALLWAY_2', 'HALLWAY_3', None, None, "In the kitchen you see a cabinet with "
                                                                            "two drawers on the south side."
                                                                            "To the north is a very dirty "
                                                                            "refrigerator.", 'Knife')
STORAGE_ROOM_1 = Room('Storage room 1', None, None, 'HALLWAY_2', None, None, None, "You see a door that is boarded up "
                                                                                   "and cannot be pried open."
                                                                                   "You also notice a self with "
                                                                                   "some items on it", 'P90BShot')
HALLWAY_1 = Room('Hallway 1', 'STORAGE_ROOM_2', 'BATHROOM', 'STAIRS', None, None, None, None, "There are three doors "
                                                                                              "one to the north, one"
                                                                                              " to the south, and one"
                                                                                              " on the east.")
STORAGE_ROOM_2 = Room('Storage room 2', None, 'HALLWAY_1', None, None, None, None, "All around you are"
                                                                                   " shelves with items"
                                                                                   " on them.", 'Healthpotion')
BATHROOM = Room('Bathroom', 'HALLWAY_1', None, None, None, None, None, "You are in a filthy bathroom and hear water "
                                                                       "running.", 'Spoon')
HALLWAY_3 = Room('Hallway 3', None, None, 'KITCHEN', None, None, None, None, "To the south you see a door and you also "
                                                                             "notice a cabinet on the west.")
STAIRS = Room('Stairs', None, None, None, None, 'HALLWAY_1', 'BASEMENT_SUPPLY_ROOM', None, "You are now in the middle"
                                                                                           " of the stairs, you can"
                                                                                           " go back up to the first"
                                                                                           " floor or go down to"
                                                                                           " the basement.")
BM_SECRET_ROOM = Room('BM Secret Room', None, 'PRISON_ROOM', None, None, 'SECRET_ROOM', None, "The room is slightly"
                                                                                              " flood up to your "
                                                                                              "ankles and there are "
                                                                                              "a few bodies on a table"
                                                                                              "which stink.",
                      'Steelchestplate')
PRISON_ROOM = Room('Prison room', 'SECRET_ROOM', None, None, 'WORK_SHOP', None, None, "It is dark and there are two "
                                                                                      "shelves", 'Shieldpotion')
WORK_ROOM = Room('Work room', None, 'DISSECTION_ROOM', 'PRISON_ROOM', None, None, None, "You have reached the work "
                                                                                        "room and notice a few tools "
                                                                                        "on the bench which you can "
                                                                                        "you.", 'Woodenhelmet')
DISSECTION_ROOM = Room('Dissection room', 'WORK_SHOP', None, 'HALLWAY_4', None, None, None, "You are in a damp room "
                                                                                            "which smells awful.",
                                                                                            'Attackpotio')
HALLWAY_4 = Room('Hallway 4', 'LIVING_ROOM', None, None, 'DISSECTION_ROOM', None, None, None, "You are in a dark "
                                                                                              "hallway, to the west "
                                                                                              "is the dissection room"
                                                                                              " and at the north side "
                                                                                              "is another door.")
LIVING_ROOM = Room('Living room', 'HALLWAY_5', 'HALLWAY_4', None, None, None, None, "This room is oddly dry and "
                                                                                    "has furniture.",
                                                                                    'Woodenchestplate')
HALLWAY_5 = Room('Hallway 5', None, 'LIVING_ROOM', None, 'BASEMENT_SUPPLY_ROOM', None, None, None, "You can see two "
                                                                                                   "doors, on the west"
                                                                                                   " side you see a "
                                                                                                   "door with a little"
                                                                                                   " light coming out,"
                                                                                                   " and to the east"
                                                                                                   " is another room.")
BASEMENT_SUPPLY_ROOM = Room('Basement supply room', 'BODY_STORAGE_ROOM', 'STAIRS', 'HALLWAY_5', None, None, None,
                            "The stench in this room is awful and it is extremely dark."
                            " You also hear weird noises on the ceiling.", 'Woodenleggings')
BODY_STORAGE_ROOM = Room('Body storage room', None, 'BASEMENT_TOOL_STORAGE', 'BASEMENT_TOOL_STORAGE', None, None, None,
                         "You notice a two body bags on a table on is open and the other is not.", 'Steelleggings')
TOOL_STORAGE_ROOM = Room('Tool room', None, None, None, 'BODY_STORAGE_ROOM', None, None, "There are a whole bunch of"
                                                                                         " tool that you can use but "
                                                                                         "they are in locked tool"
                                                                                         " boxes.", 'Steelhelmet')
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

player = Player(MAIN_ROOM, 100, 25)

playing = True
current_node = world_map['MAIN_ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
actions = ['PICK UP', 'ATTACK', 'DRINK']
player.inventory = []

while playing:
    print("Health = %s" % player.health)
    print("Shield = %s" % player.shield)
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print(player.current_location.item)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())  # <--- This is for shortcuts like W for west
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:  # <--- This is to exit the game
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
        print("Your current inventory is:")  # <--- This is for inventory
        print(list(player.inventory))

    elif player.current_location.item is not None and ('pick up' in command.lower() or 'grab' in command.lower()):
        try:
            print("You picked up the item.")
            player.inventory.append(player.current_location.item)
            player.current_location.item = None
        except AttributeError:
            print("You cannot pick this up")
            pass

    elif player.current_location.item is None:
        try:
            print()
        except AttributeError:
            pass

    else:
        print("Command Not Found")
