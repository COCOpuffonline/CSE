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
        except AttributeError:
            print("I can't go that way")
        except KeyError:
            print("There is no path here")
    else:
        print("Command Not Found")
