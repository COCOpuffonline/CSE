world_map = {
    'R19A': {
        'NAME': "Mr.Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the the north wall",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "This North Parking Lot",
        'DESCRIPTION': "There are a couple cars picked here",
        'PATHS': {
            'SOUTH': 'R19A'

        }
    }
}

# Controller
# Nodes are the rooms
# Nodes have name, description, and path
playing = True
current_node = world_map['R19A']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
