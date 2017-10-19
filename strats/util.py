"""Utility functions for strategy detection."""

import datetime
import logging
import math

_LOGGER = logging.getLogger(__name__)


def first_building(building, player):
    """Find when the first building of a given type was constructed."""
    for item in player['build']:
        if item['building'] == building:
            return item['timestamp']


def age_start(age, player):
    """Find when player clicked up to a given age."""
    if age in player['ages']:
        return player['ages'][age]


def queued_before(unit, timestamp, summary):
    """Find how many units were queued before a given time."""
    count = 0
    for item in summary['queue']:
        if item['unit'] == unit and item['timestamp'] < timestamp:
            count += 1
    return count


def built_before(building, timestamp, player):
    """Get list of buildings constructed before a given time."""
    result = []
    for item in player['build']:
        if item['building'] == building and item['timestamp'] < timestamp:
            result.append(item)
    return result


def researched_before(technology, timestamp, player):
    """Check if a technology was researched before a given time."""
    for item in player['research']:
        if item['technology'] == technology and item['timestamp'] < timestamp:
            return True
    return False


def distance_to_any_enemy(coords, player, summary):
    """Find distance to nearest enemy from any point."""
    min_dist = 1.0
    enemies = []
    for team in summary['diplomacy']['teams']:
        if player['number'] not in team['player_numbers']:
            enemies += team['player_numbers']
    for other in summary['players']:
        if other['number'] not in enemies:
            continue
        dist = _distance(coords, other['coordinates'])
        percent = dist / summary['map']['x']
        if percent < min_dist:
            min_dist = percent
    return min_dist



def probability(evidence):
    """Produce a probability score."""
    total_score = 0
    for factor, weight in evidence.items():
        _LOGGER.debug(' -> %s: %s', factor, weight)
        total_score += weight
    return round(total_score / 100, 2)


# pylint: disable=invalid-name
def time_delta(t1, t2):
    """Get difference between two times."""
    return (datetime.datetime.combine(datetime.date.min, t2)
            - datetime.datetime.combine(datetime.date.min, t1))


def time_add(t, delta):
    """Add two times together."""
    return (datetime.datetime.combine(datetime.date.min, t) + delta).time()


def _distance(p0, p1):
    """Compute linear distance."""
    return math.sqrt((p0['x'] - p1['x'])**2 + (p0['y'] - p1['y'])**2)
