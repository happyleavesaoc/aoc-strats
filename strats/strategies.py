"""How to detect various strategies.

Each function is a heuristic that attempts to
detect a competitive meta-game opening.
"""

import datetime

import strats.util as util


def detect_drush(player, summary):
    """Detect a drush.

    - Barracks created
    - Feudal time between boundary
    - Militia queued

    Caveat: We don't know which player queued the militia.
    """
    rax_time = util.first_building('Barracks', player)
    evidence = {}
    if not rax_time:
        return 0.0
    min_rax_time = datetime.time(0, 6, 0)
    max_rax_time = datetime.time(0, 7, 0)
    feudal_time = util.age_start('feudal', player)
    if not feudal_time:
        return 0.0
    if rax_time >= min_rax_time and rax_time <= max_rax_time:
        evidence['in_boundary'] = 30
    if rax_time < feudal_time:
        evidence['before_feudal'] = 30
    queued = util.queued_before('Militia', datetime.time(0, 12, 0), summary)
    if queued == 0:
        return 0.0
    evidence['queued_militia'] = min(queued * 10, 40)
    return util.probability(evidence)


def detect_fast_castle(player, _):
    """Detect a fast castle.

    - Feudal and castle time in short succession.
    """
    evidence = {}
    castle_time = util.age_start('castle', player)
    feudal_time = util.age_start('feudal', player)
    if not feudal_time or not castle_time:
        return 0.0
    if util.time_delta(castle_time, feudal_time) < datetime.timedelta(minutes=2):
        evidence['age_proximity'] = 100
    return util.probability(evidence)


def detect_douche(player, _):
    """Detect a douche.

    - Town center built prior to Feudal age.
    - Possibly player is Persians
    """
    evidence = {}
    first_tc = util.first_building('Town Center', player)
    if not first_tc:
        return 0.0
    if first_tc < util.age_start('feudal', player):
        evidence['tc_before_feudal'] = 80
    if player['civilization'] == 'Persians':
        evidence['is_persian'] = 20
    return util.probability(evidence)


def detect_scrush(player, summary):
    """Detect a scrush.

    - One or more stables built.
    - Scouts trained.

    Caveat: We don't know which player queued the scouts.
    """
    evidence = {}
    feudal_time = util.age_start('feudal', player)
    if not feudal_time:
        return 0.0
    early_feudal = util.time_add(feudal_time, datetime.timedelta(minutes=3))
    stables = util.built_before('Stable', early_feudal, player)
    evidence['in_boundary'] = min(len(stables) * 30, 70)
    queued = util.queued_before('Scout', early_feudal, summary)
    if queued == 0:
        return 0.0
    evidence['queued_scouts'] = min(queued * 10, 30)
    return util.probability(evidence)


def detect_trush(player, summary):
    """Detect a trush.

    - Towers built near enemy in early Feudal
    - Possibly fletching researched
    - POssibly player is Koreans
    """
    evidence = {}
    feudal_time = util.age_start('feudal', player)
    if not feudal_time:
        return 0.0
    early_feudal = util.time_add(feudal_time, datetime.timedelta(minutes=15))
    towers = util.built_before('Watch Tower', early_feudal, player)
    fletching = util.researched_before('Fletching', early_feudal, player)
    if fletching:
        evidence['has_fletching'] = 10
    if player['civilization'] == 'Koreans':
        evidence['is_korean'] = 10
    trush_towers = 0
    for tower in towers:
        if util.distance_to_any_enemy(tower['coords'], player, summary) < 0.2:
            trush_towers += 1
    evidence['near_enemy'] = min(trush_towers * 30, 80)
    return util.probability(evidence)


def detect_maa(player, summary):
    """Detect man-at-arms rush.

    - Drush occurred
    - Man-at-arms researched in early Feudal
    """
    evidence = {
        'drush': detect_drush(player, summary) * 50
    }
    feudal_time = util.age_start('feudal', player)
    if not feudal_time:
        return 0.0
    early_feudal = util.time_add(feudal_time, datetime.timedelta(minutes=3))
    early_maa = util.researched_before('Man-at-Arms', early_feudal, player)
    if early_maa:
        evidence['early_maa'] = 50
    return util.probability(evidence)


def detect_forward_ranges(player, summary):
    """Detect forward.

    - Archery ranges near enemy in early Feudal
    """
    evidence = {}
    feudal_time = util.age_start('feudal', player)
    if not feudal_time:
        return 0.0
    early_feudal = util.time_add(feudal_time, datetime.timedelta(minutes=15))
    ranges = util.built_before('Archery Range', early_feudal, player)
    fwd_ranges = 0
    for building in ranges:
        if util.distance_to_any_enemy(building['coords'], player, summary) < 0.5:
            fwd_ranges += 1
    if fwd_ranges:
        evidence['near_enemy'] = 100
    return util.probability(evidence)
