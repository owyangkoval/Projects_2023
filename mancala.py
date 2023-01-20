# Mancala Game - Angela Koval Final Portfolio Project for OSU
# Format of the final output of boardgame is as follows:
#         [player1 pit1, player1 pit2, player1 pit3, player1 pit4, player1 pit5, player1 pit6, player1 store,
#         player2 pit1, player2 pit2, player2 pit3, player2 pit4, player2 pit5, player2 pit6, player2 store,]

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
        player_idx = player - 1  # adjusting for index purposes
        player_object = self._player_list[player_idx]  # getting a player object
        player_board = player_object.board  # getting a player board
        num_stones = player_board[pit_idx]  # num_stones keeps track of number of stones
        player_board[pit_idx] = 0  # set the chosen pit_idx to 0
        active_player_idx = player_idx # keeps track of the player that is currently active
        while num_stones > 0:  # loop for placement of stones from initial pit_idx
            if pit_idx == 0 or (pit_idx == 1 and player_idx != active_player_idx):  # condition for when player side
                # runs out of indices, move to other side
                player_idx = (player_idx + 1) % 2  # switch to the board of the other player
                pit_idx = 6  # begin at pit6 of opposing player's board
            else:
                pit_idx -= 1  # decrement pit_idx number to place one stone from num_stones
            num_stones -= 1  # decrement stones as loop progresses
            player_object = self._player_list[player_idx]  # getting a player object
            player_board = player_object.board  # getting a player board
            player_board[pit_idx] += 1  # add to each subsequent pit counterclockwise


    def print_board(self):
        """ Prints board in final format """
        player_object_1 = self._player_list[0]  # get player object 1
        player_object_2 = self._player_list[1]  # get player object 2
        player_board_1 = player_object_1.board  # get player board 1
        player_board_2 = player_object_2.board  # get player board 2

        # print player_board 1
        player_board_1_final = player_board_1[1:] + player_board_1[0:1]  # pit1 to pit6 concatenated with store at end
        player_board_2_final = player_board_2[1:] + player_board_2[0:1]  # pit1 to pit6 concatenated with store at end
        print(player_board_1_final + player_board_2_final)  # final board arrangement in list
        return player_board_1_final + player_board_2_final

    def return_winner(self):
        """ Returns the winner in printed form """
        player_object_1 = self._player_list[0]  # get player object 1
        player_object_2 = self._player_list[1]  # get player object 2
        player_board_1 = player_object_1.board  # get player board 1
        player_board_2 = player_object_2.board  # get player board 2

        if player_board_1[0] > player_board_2[0]:
            print(f"Winner is player 1: {player_object_1.get_name()}")
            return player_object_1.get_name()
        else:
            print(f"Winner is player 2: {player_object_2.get_name()}")
            return player_object_2.get_name()

class Player:
    """ This class represents all relevant information on the player object in the game Mancala"""

    def __init__(self, name):
        self._name = name  # name of player
        self.board = [0, 4, 4, 4, 4, 4, 4]  # beginning setup [store, pit1, pit2, pit3, pit4, pit5, pit6]
        self.board_side = []  # list of two board sides

    def get_name(self):
        return self._name
