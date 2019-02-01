world_map = {
    'MAIN_ROOM': {
        'NAME': "Main Room",
        'DESCRIPTION': "You are in an old dirty room with one door in front of you."
                       "There is a couch in the middle of the room, a breaker box and chimney.",
        'PATHS': {
            'WEST': 'Main Hallway'
            'EAST': 'Secret Room'
        }
    },
    'SECRET_ROOM': {
        'NAME': "Secret Room",
        'DESCRIPTION': "There is a small table on your left and on your right is a hole on the floor.",
        'PATHS': {
            'WEST': 'MAIN_ROOM'

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