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