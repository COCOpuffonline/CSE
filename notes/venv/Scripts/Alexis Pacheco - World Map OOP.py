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


MAIN_ROOM = Room('Main Room', None, None, 'SECRET_ROOM', 'HALLWAY_2', None, None,)
SECRET_ROOM = Room('Secret room', None, 'BASEMENT', None, 'MAIN_ROOM', None, None)
HALLWAY_2 = Room('Hallway', 'KITCHEN', 'HALLWAY_1', None, 'STORAGE_ROOM_1', None, None)
KITCHEN = Room('Kitchen', None, None, 'HALLWAY_2', 'HALLWAY_3', None, None)
STORAGE_ROOM = Room('Storage room 1', None, None, 'HALLWAY_2', None, None, None)
HALLWAY_1 = Room('Hallway 1', 'STORAGE_ROOM_2', 'BATHROOM', 'STAIRS', None, None, None)
STORAGE_ROOM_2 = Room('Storage room 2', None, 'HALLWAY_1', None, None, None, None)
BATHROOM = Room('Bathroom', 'HALLWAY_1', None, None, None, None, None)
HALLWAY_3 = Room('Hallway 3', None, None, 'KITCHEN', None, None, None)
STAIRS = Room('Stairs', None, None, None, None, 'HALLWAY_1', 'BASEMENT_SUPPLY_ROOM')
BM_SECRET_ROOM = Room('BM Secret Room', None, 'PRISON_ROOM', None, None, 'SECRET_ROOM', None)
PRISON_ROOM = Room('Prison room', 'SECRET_ROOM', None, None, 'WORK_SHOP', None, None)
DISSECTION_ROOM = Room('Dissection room', 'WORK_SHOP', None, 'HALLWAY_4', None, None, None)
HALLWAY_4 = Room('Hallway 4', 'LIVING_ROOM', None, None, 'DISSECTION_ROOM', None, None)
LIVING_ROOM = Room('Living room', 'HALLWAY_5', 'HALLWAY_4', None, None, None, None)
HALLWAY_5 = Room('Hallway 5', None, 'LIVING_ROOM', None, 'BASEMENT_SUPPLY_ROOM', None, None)
BASEMENT_SUPPLY_ROOM = Room('Basement supply room', 'BODY_STORAGE_ROOM', 'STAIRS', 'HALLWAY_5', None, None, None)
BODY_STORAGE_ROOM = Room('Body storage room', None, 'BASEMENT_TOOL_STORAGE', 'BASEMENT_TOOL_STORAGE', None, None, None)
TOOL_STORAGE_ROOM = Room('Tool room', None, None, None, 'BODY_STORAGE_ROOM', None, None)

player = Player(MAIN_ROOM)

playing = True
directions = ['north', 'south', 'west', 'east', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
        except AttributeError:
            pass
    else:
        print("Command Not Found")
