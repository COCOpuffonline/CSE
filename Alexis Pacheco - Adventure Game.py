world_map = {
    'MAIN_ROOM': {
        'NAME': "Room #1",
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
            'SOUTH': 'BASEMENT'
        }
    },
    'HALLWAY_2': {
        'NAME': "Hallway 1",
        'DESCRIPTION': "To the north you see a door, on the south side there is another door, and to the west is a"
                       "a room without a door.",
        'PATHS': {
            'NORTH': 'KITCHEN',
            'SOUTH': 'HALLWAY_1',
            'WEST': 'STORAGE_ROOM_1'
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
        'NAME':



        }
    }
}

playing = True
current_node = world_map['MAIN_ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

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
    else:
        print("Command Not Found")
