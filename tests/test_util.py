import datetime
import unittest
import strats.util as util


class TestUtil(unittest.TestCase):

    def test_first_building(self):
        player = {
            'build': [{'building': 'Barracks', 'timestamp': datetime.time(0, 5, 5)}]
        }
        self.assertEqual(util.first_building('Barracks', player), datetime.time(0, 5, 5))
        self.assertEqual(util.first_building('University', player), None)

    def test_age_start(self):
        player = {
            'ages': {'feudal': datetime.time(0, 10, 0)}
        }
        self.assertEqual(util.age_start('feudal', player), datetime.time(0, 10, 0))
        self.assertEqual(util.age_start('imperial', player), None)

    def test_queued_before(self):
        game = {
            'queue': [
                {'unit': 'Archer', 'timestamp': datetime.time(0, 12, 0)},
                {'unit': 'Archer', 'timestamp': datetime.time(0, 14, 0)}
            ]
        }
        self.assertEqual(util.queued_before('Archer', datetime.time(0, 13, 0), game), 1)

    def test_built_before(self):
        player = {
            'build': [
                {'building': 'Barracks', 'timestamp': datetime.time(0, 5, 5)},
                {'building': 'Barracks', 'timestamp': datetime.time(0, 12, 5)}
            ]
        }
        self.assertEqual(len(util.built_before('Barracks', datetime.time(0, 10, 0), player)), 1)

    def test_researched_before(self):
        player = {
            'research': [{'technology': 'Loom', 'timestamp': datetime.time(0, 4, 0)}]
        }
        self.assertTrue(util.researched_before('Loom', datetime.time(0, 5, 0), player))

    def test_distance_to_any_enemy(self):
        player = {'index': 1, 'coords': {'x': 0, 'y': 50}}
        game = {
            'teams': [{'player_nums': [1]}, {'player_nums': [2]}],
            'map_size': {'x': 100, 'y': 100},
            'players': [
                player,
                {'index': 2, 'coords': {'x': 0, 'y': 75}}
            ]
        }
        self.assertEqual(util.distance_to_any_enemy({'x': 0, 'y': 0}, player, game), 0.75)

    def test_probability(self):
        evidence = {
            'piece one': 50,
            'piece two': 35
        }
        self.assertEqual(util.probability(evidence), 0.85)

    def test_distance(self):
        self.assertEqual(util._distance({'x': 0, 'y': 100}, {'x': 0, 'y': 0}), 100)

    def test_time_delta(self):
        self.assertEqual(util.time_delta(datetime.time(0, 3, 0), datetime.time(0, 5, 0)), datetime.timedelta(minutes=2))

    def test_time_add(self):
        self.assertEqual(util.time_add(datetime.time(0, 3, 0), datetime.timedelta(minutes=1, seconds=1)), datetime.time(0, 4, 1))
