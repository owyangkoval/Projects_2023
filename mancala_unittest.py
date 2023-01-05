import unittest

from mancala import Mancala, Player

class TestMancala(unittest.TestCase):

    def test_play_game(self):
        # Setup
        game = Mancala()
        player1 = game.create_player("Pusheen")
        player2 = game.create_player("Pip")

        # Test
        game.play_game(1, 6)

        # Assert
        self.assertEqual(player1.board, [0, 4, 5, 5, 5, 5, 0])
        self.assertEqual(player2.board, [0, 4, 4, 4, 4, 4, 4])

    def test_get_next_move(self):
        # Setup
        game = Mancala()
        player1 = game.create_player("Pusheen")
        player2 = game.create_player("Pip")

        # Test
        game.get_next_move(1, 0, 1)

        # Assert


if __name__ == '__main__':
    unittest.main()