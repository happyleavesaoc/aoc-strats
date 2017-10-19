import datetime
import unittest
import strats.strategies as strategies
import data


class TestStrategies(unittest.TestCase):

    def test_detect_drush(self):
        summary = {'players': [data.PLAYER_DRUSH]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_drush(data.PLAYER_DRUSH, summary), 1.0)

    def test_detect_fast_castle(self):
        summary = {'players': [data.PLAYER_FAST_CASTLE]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_fast_castle(data.PLAYER_FAST_CASTLE, summary), 1.0)

    def test_detect_douche(self):
        summary = {'players': [data.PLAYER_DOUCHE]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_douche(data.PLAYER_DOUCHE, summary), 1.0)

    def test_detect_scrush(self):
        summary = {'players': [data.PLAYER_SCRUSH]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_scrush(data.PLAYER_SCRUSH, summary), 0.9)

    def test_detect_trush(self):
        summary = {'players': [data.PLAYER_TRUSH, data.PLAYER_DRUSH]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_trush(data.PLAYER_TRUSH, summary), 1.0)

    def test_detect_maa(self):
        summary = {'players': [data.PLAYER_MAA]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_maa(data.PLAYER_MAA, summary), 1.0)

    def test_detect_forward_ranges(self):
        summary = {'players': [data.PLAYER_FORWARD_RANGES, data.PLAYER_DRUSH]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strategies.detect_forward_ranges(data.PLAYER_FORWARD_RANGES, summary), 1.0)
