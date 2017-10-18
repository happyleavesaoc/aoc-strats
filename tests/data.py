import datetime


GAME_QUEUE = [
    {'unit': 'Militia', 'timestamp': datetime.time(0, 7, 40)},
    {'unit': 'Militia', 'timestamp': datetime.time(0, 8, 0)},
    {'unit': 'Militia', 'timestamp': datetime.time(0, 8, 0)},
    {'unit': 'Scout', 'timestamp': datetime.time(0, 9, 10)},
    {'unit': 'Scout', 'timestamp': datetime.time(0, 9, 30)},
    {'unit': 'Scout', 'timestamp': datetime.time(0, 10, 0)},
]

DEFAULT_SUMMARY = {
    'map_size': {'x': 100, 'y': 100},
    'teams': [{'player_nums': [1, 6, 2]}, {'player_nums': [3, 5, 4]}],
    'queue': GAME_QUEUE
}

PLAYER_DRUSH = {
    'index': 1,
    'civilization': 'Goths',
    'build': [{'building': 'Barracks', 'timestamp': datetime.time(0, 7, 0), 'coords': {'x': 10, 'y': 10}}],
    'ages': {'feudal': datetime.time(0, 10, 0)},
    'research': [],
    'coords': {'x': 100, 'y': 100}
}

PLAYER_FAST_CASTLE = {
    'index': 2,
    'civilization': 'Franks',
    'research': [],
    'ages': {'feudal': datetime.time(0, 14, 0), 'castle': datetime.time(0, 15, 30)}
}

PLAYER_DOUCHE = {
    'index': 3,
    'civilization': 'Persians',
    'build': [{'building': 'Town Center', 'timestamp': datetime.time(0, 6, 0), 'coords': {'x': 10, 'y': 10}}],
    'ages': {'feudal': datetime.time(0, 14, 0)},
    'research': []
}

PLAYER_SCRUSH = {
    'index': 4,
    'civilization': 'Huns',
    'build': [
        {'building': 'Stable', 'timestamp': datetime.time(0, 9, 0), 'coords': {'x': 10, 'y': 10}},
        {'building': 'Stable', 'timestamp': datetime.time(0, 10, 30), 'coords': {'x': 10, 'y': 10}},
        {'building': 'Stable', 'timestamp': datetime.time(1, 10, 30), 'coords': {'x': 10, 'y': 10}}
    ],
    'ages': {'feudal': datetime.time(0, 10, 0)},
    'research': []
}

PLAYER_TRUSH = {
    'index': 5,
    'civilization': 'Koreans',
    'build': [
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 1), 'coords': {'x': 90, 'y': 90}},
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 20), 'coords': {'x': 90, 'y': 90}},
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 40), 'coords': {'x': 90, 'y': 90}}
    ],
    'ages': {'feudal': datetime.time(0, 8, 0)},
    'research': [{'technology': 'Fletching', 'timestamp': datetime.time(0, 8, 1)}],
    'coords': {'x': 50, 'y': 0}
}

PLAYER_MAA = {
    'index': 6,
    'civilization': 'Japanese',
    'build': [{'building': 'Barracks', 'timestamp': datetime.time(0, 7, 0)}],
    'ages': {'feudal': datetime.time(0, 10, 0),},
    'research': [{'technology': 'Man-at-Arms', 'timestamp': datetime.time(0, 11, 0)}]
}

PLAYER_FORWARD_RANGES = {
    'index': 7,
    'civilization': 'Huns',
    'build': [{'building': 'Archery Range', 'timestamp': datetime.time(0, 8, 1), 'coords': {'x': 90, 'y': 90}}],
    'ages': {'feudal': datetime.time(0, 10, 0)},
    'coords': {'x': 50,'y': 100},
    'research': []
}
