# aoc-strats

Prototype for detecting strategies used in Age of Empires 2 recorded games. At present, makes an attempt to detect various popular competitive play openings.


## Install

Prerequisite: Python 3

After cloning repository:

`pip install -e .`

## Usage

`strats.detect` is the only public method. It accepts a player `dict`, and a game summary `dict`. Both of these follow output format of [`aoc-mgz`](https://github.com/happyleavesaoc/aoc-mgz)'s `recorded_game.summarize` method. A minimal example is below.

```python
import datetime
import strats

summary = {
    'map': {'x': 100, 'y': 100},
    'teams': [{'player_numbers': [1, 6, 2]}, {'player_numbers': [3, 5, 4]}],
    'queue': [
        {'unit': 'Militia', 'timestamp': datetime.time(0, 7, 0)},
        {'unit': 'Militia', 'timestamp': datetime.time(0, 7, 30)},
        {'unit': 'Militia', 'timestamp': datetime.time(0, 8, 0)}
    ],
    'players': [
        {
            'index': 1,
            'number': 2,
            'civilization': 'Goths',
            'build': [
                {'building': 'Barracks', 'timestamp': datetime.time(0, 6, 40), 'coordinates': {'x': 10, 'y': 10}}
            ],
            'ages': {'feudal': datetime.time(0, 10, 0)},
            'research': [],
            'coordinates': {'x': 100, 'y': 100}
        }
    ]
}

result = strats.detect(1, summary)  # detect strategy for player 1
print(result)  # ['drush']
```

## TODO

- [ ] Detect more strategies
- [ ] Adjust constants to match current meta
- [ ] Test against more recorded games to discover edge cases

## Development

Contributions are welcome. Please be sure your pull request includes tests and passes `tox`.
