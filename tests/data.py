import datetime


GAME_QUEUE = [
    {'unit': 'Militia', 'timestamp': datetime.time(0, 6, 40)},
    {'unit': 'Militia', 'timestamp': datetime.time(0, 7, 0)},
    {'unit': 'Militia', 'timestamp': datetime.time(0, 7, 0)},
    {'unit': 'Scout Cavalry', 'timestamp': datetime.time(0, 9, 30)},
    {'unit': 'Scout Cavalry', 'timestamp': datetime.time(0, 9, 50)},
    {'unit': 'Scout Cavalry', 'timestamp': datetime.time(0, 10, 0)},
]

DEFAULT_SUMMARY = {
    'map': {'x': 100, 'y': 100},
    'diplomacy': {'teams': [{'player_numbers': [1, 6, 2]}, {'player_numbers': [3, 5, 4]}]},
    'queue': GAME_QUEUE
}

PLAYER_DRUSH = {
    'index': 1,
    'number': 1,
    'civilization': 'Goths',
    'build': [{'building': 'Barracks', 'timestamp': datetime.time(0, 6, 30), 'coordinates': {'x': 10, 'y': 10}}],
    'ages': {'feudal': datetime.time(0, 10, 0)},
    'research': [],
    'coordinates': {'x': 100, 'y': 100}
}

PLAYER_FAST_CASTLE = {
    'index': 2,
    'number': 2,
    'civilization': 'Franks',
    'research': [],
    'ages': {'feudal': datetime.time(0, 14, 0), 'castle': datetime.time(0, 15, 30)}
}

PLAYER_DOUCHE = {
    'index': 3,
    'number': 3,
    'civilization': 'Persians',
    'build': [{'building': 'Town Center', 'timestamp': datetime.time(0, 6, 0), 'coordinates': {'x': 10, 'y': 10}}],
    'ages': {'feudal': datetime.time(0, 14, 0)},
    'research': []
}

PLAYER_SCRUSH = {
    'index': 4,
    'number': 4,
    'civilization': 'Huns',
    'build': [
        {'building': 'Stable', 'timestamp': datetime.time(0, 9, 10), 'coordinates': {'x': 10, 'y': 10}},
        {'building': 'Stable', 'timestamp': datetime.time(0, 10, 30), 'coordinates': {'x': 10, 'y': 10}},
        {'building': 'Stable', 'timestamp': datetime.time(1, 10, 30), 'coordinates': {'x': 10, 'y': 10}}
    ],
    'ages': {'feudal': datetime.time(0, 9, 0)},
    'research': []
}

PLAYER_TRUSH = {
    'index': 5,
    'number': 5,
    'civilization': 'Koreans',
    'build': [
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 1), 'coordinates': {'x': 90, 'y': 90}},
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 20), 'coordinates': {'x': 90, 'y': 90}},
        {'building': 'Watch Tower', 'timestamp': datetime.time(0, 8, 40), 'coordinates': {'x': 90, 'y': 90}}
    ],
    'ages': {'feudal': datetime.time(0, 8, 0)},
    'research': [{'technology': 'Fletching', 'timestamp': datetime.time(0, 8, 1)}],
    'coordinates': {'x': 50, 'y': 0}
}

PLAYER_MAA = {
    'index': 6,
    'number': 6,
    'civilization': 'Japanese',
    'build': [{'building': 'Barracks', 'timestamp': datetime.time(0, 7, 0)}],
    'ages': {'feudal': datetime.time(0, 10, 0),},
    'research': [{'technology': 'Man-at-Arms', 'timestamp': datetime.time(0, 11, 0)}]
}

PLAYER_FORWARD_RANGES = {
    'index': 7,
    'number': 7,
    'civilization': 'Huns',
    'build': [{'building': 'Archery Range', 'timestamp': datetime.time(0, 8, 1), 'coordinates': {'x': 90, 'y': 90}}],
    'ages': {'feudal': datetime.time(0, 10, 0)},
    'coordinates': {'x': 50,'y': 100},
    'research': []
}
