"""Detect strategies per player."""

import datetime
import logging
import strats.strategies as strategies


_LOGGER = logging.getLogger(__name__)
PROBABILITY_THRESHOLD = 0.5
STRATEGIES = [
    {
        'name': 'drush',
        'function': strategies.detect_drush,
        'overrides': []
    }, {
        'name': 'fast_castle',
        'function': strategies.detect_fast_castle,
        'overrides': []
    }, {
        'name': 'douche',
        'function': strategies.detect_douche,
        'overrides': []
    }, {
        'name': 'scrush',
        'function': strategies.detect_scrush,
        'overrides': ['drush']
    }, {
        'name': 'trush',
        'function': strategies.detect_trush,
        'overrides': ['drush']
    }, {
        'name': 'maa',
        'function': strategies.detect_maa,
        'overrides': ['drush']
    }, {
        'name': 'forward_ranges',
        'function': strategies.detect_forward_ranges,
        'overrides': ['drush']
    }
]


def _find_player(player_index, summary):
    """Find player in summary data."""
    player = [player for player in summary['players'] if player['index'] == player_index]
    if not player:
        raise ValueError('player not found')
    return player[0]


def detect(player_index, summary, threshold=PROBABILITY_THRESHOLD):
    """Detect strategies for a given player."""
    results = []
    player = _find_player(player_index, summary)
    for definition in STRATEGIES:
        strategy = definition['name']
        probability = definition['function'](player, summary)
        _LOGGER.debug('testing %s: %s', strategy, probability)
        if probability <= threshold:
            continue
        results.append(strategy)
        for override in definition['overrides']:
            if override not in results:
                continue
            results.remove(override)
    return results
