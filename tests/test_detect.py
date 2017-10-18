import unittest
import strats
import data


class TestStrats(unittest.TestCase):

    def test_detect_without_override(self):
        summary = {'players': [data.PLAYER_DRUSH]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strats.detect(1, summary), ['drush'])

    def test_detect_with_override(self):
        summary = {'players': [data.PLAYER_MAA]}
        summary.update(data.DEFAULT_SUMMARY)
        self.assertEqual(strats.detect(6, summary), ['maa'])

    def test_find_player(self):
        summary = {'players': [{'index': 3}]}
        self.assertEqual(strats._find_player(3, summary), {'index': 3})
        with self.assertRaises(ValueError):
            strats._find_player(1, summary)
