world_map = {
    'MAIN_ROOM': {
        'NAME': "Room #1",
        'DESCRIPTION': "You wake up in a very filthy room and you do not remember how you got there."
                       "There is a couch in the middle of the room and a chimney that has not been used in a while.",
        'PATHS': {
            'EAST': "SECRET_ROOM"
        }
    },
    'SECRET_ROOM': {
        'NAME': "Secret room",
        'DESCRIPTION': "You are in a small room and notice a small table on your left and on your right"
                       "you see a hole in the floor.",
        'PATHS': {
            'WEST': 'MAIN_ROOM'
        }
    },
    'HALLWAY_1': {
        'NAME': "Hallway 2",
        'DESCRIPTION': "To the north you see a door, on the south side there is another door, and to the west is a"
                       "a room without a door.",
        'PATHS': {
            'NORTH': 'KITCHEN',
            'SOUTH': 'HALLWAY_2',
            'WEST': 'STORAGE_ROOM_1'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "In the kitchen you see a cabinet with two drawers on the south side."
                       "To the north is a very dirty refrigerator."


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
