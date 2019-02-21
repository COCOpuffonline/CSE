class Room(object):
    def __init__(self, name, north, south, east, west, up, down):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


MAIN_ROOM = Room('Main Room', None, None, 'SECRET_ROOM', 'HALLWAY_2', None, None)
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
PRISON_ROOM = Room('Prison room', 'SECRET_ROOM', None, None, 'WORK_SHOP')
DISSECTION_ROOM = Room('Dissection room', 'WORK_SHOP', None, 'HALLWAY_4', None, None, None, None)
HALLWAY_4 = Room('Hallway 4', 'LIVING_ROOM', None, None, 'DISSECTION_ROOM', None, None)
LIVING_ROOM = Room('Living room', 'HALLWAY_5', 'HALLWAY_4', None, None, None, None)
HALLWAY_5 = Room('Hallway 5', None, 'LIVING_ROOM', None, 'BASEMENT_SUPPLY_ROOM', None, None)
BASEMENT_SUPPLY_ROOM = Room()
BODY_STORAGE_ROOM = Room()
TOOL_STORAGE_ROOM = Room()
