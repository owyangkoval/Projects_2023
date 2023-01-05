# Mancala Game - Final Portfolio Project for OSU

class Mancala:
    """ This class represents the gameplay for Mancala. Game moves counterclockwise. """

    def __init__(self):
        self._player_list = []  # list of players objects

    def create_player(self, player_name):
        """ Creates a list of player objects """
        player_object = Player(player_name) # create player object
        self._player_list.append(player_object) # append to lists of player objects
        return player_object

    def play_game(self, player, pit_idx):
        """ Sets up the board for one side of the pit, decrements clockwise"""
        player_object = self._player_list[player-1]  # create a player object
        player_board = player_object.board  # create a player board
        num_stones = player_board[pit_idx]  # num_stones keeps track of number of stones
        player_board[pit_idx] = 0  # set the chosen pit_idx to 0
        pit_idx -= 1 # decrement pit_idx by one after setting pit_idx to 0
        while num_stones > 0:
            num_stones -= 1 # decrement stones
            player_board[pit_idx] += 1  # add to each subsequent pit counterclockwise
            pit_idx -= 1

    def get_next_move(self, player, board_side, pit_idx):
        """ Prepares player to move onto either side of the board """
        player_object = self._player_list[player-1]  # create a player object
        player_board_side_1 = player_object.board  # create a player board
        player_board_side_2 = player_object.other_board  # create the other board side for current player
        num_stones = player_board_side_1[pit_idx]  # num_stones keeps track of number of stones
        player_board_side_1[pit_idx] = 0  # set the chosen pit_idx to 0
        pit_idx -= 1  # decrement pit_idx by one after setting pit_idx to 0

        # if number of stones runs out on player_board_side_1, must move to player_board_side_2


    # def print_board(self):


class Player:
    """ This class represents the player who will play Mancala"""

    def __init__(self, name):
        self._name = name
        self.board = [0, 4, 4, 4, 4, 4, 4]
        self.other_board = [0, 4, 4, 4, 4, 4, 4]
