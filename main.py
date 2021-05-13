'''
Contains all the information related to the TicTacToe class
The game starts here
'''

from Table import *
from Macros import *


class TicTacToe:
    def __init__(self):
        """
        Initializes the table, players
        """

        self.board = Board()
        self.tic_tac_table = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.player1 = {
            "name": "Player X",
            "occupied_tiles": [(), (), ()],
            "turns": 0,
            "mark": "X",
            "image": x_mark,
        }
        self.player2 = {
            "name": "Player O",
            "occupied_tiles": [(), (), ()],
            "turns": 0,
            "mark": "O",
            "image": o_mark,
        }
        self.players = [self.player1, self.player2]
        self.turns = 0
        self.player1_turn = True
        self.running = True

    def __str__(self):

        return f"{self.tic_tac_table[0][:]}\n" \
               f"{self.tic_tac_table[1][:]}\n" \
               f"{self.tic_tac_table[2][:]}\n" \
               f"\n\n\n\n"

    def update_screen(self):
        """
        Redraws the screen after every turn
        """

        background.blit(background_image, (0, 0))
        self.board.draw_lines()

        for coord in self.player1["occupied_tiles"]:
            if coord:
                background.blit(self.player1["image"], self.board.tiles[coord])
        for coord in self.player2["occupied_tiles"]:
            if coord:
                background.blit(self.player2["image"], self.board.tiles[coord])

        screen.blit(background, (0, 0))
        pygame.display.update()

    def update_player(self, tile):
        """
        Updates the data of a player if the player did a regular move
        :param tile: one of the table's tile top left coordinates
        """

        # If the cursor is on the Board
        if tile in self.board.tiles:
            board_coord = self.board.tiles[tile]

            # If there is no mark on the Tile
            if not self.tic_tac_table[board_coord[0]][board_coord[1]]:
                player = self.players[0] if self.player1_turn else self.players[1]
                self.tic_tac_table[board_coord[0]][board_coord[1]] = player["mark"]

                # If we start to override the players' marks
                if player["occupied_tiles"][player["turns"]]:
                    fourth_mark = player["occupied_tiles"][player["turns"]]
                    self.tic_tac_table[fourth_mark[0]][fourth_mark[1]] = ""

                player["occupied_tiles"][player["turns"]] = board_coord
                player["turns"] = (player["turns"] + 1) % 3

                self.update_screen()
                self.player1_turn = not self.player1_turn

    def check_winner(self):
        """
        The game checks if one of the player wins by checking if the rows or columns have the same character
        """

        # First Row
        if self.tic_tac_table[0][0] == self.tic_tac_table[0][1] == self.tic_tac_table[0][2] != "":
            print("The winner is:", self.tic_tac_table[0][0])
        # Second Row
        elif self.tic_tac_table[1][0] == self.tic_tac_table[1][1] == self.tic_tac_table[1][2] != "":
            print("The winner is:", self.tic_tac_table[1][0])
        # Third Row
        elif self.tic_tac_table[2][0] == self.tic_tac_table[2][1] == self.tic_tac_table[2][2] != "":
            print("The winner is:", self.tic_tac_table[2][0])

        # First Column
        elif self.tic_tac_table[0][0] == self.tic_tac_table[1][0] == self.tic_tac_table[2][0] != "":
            print("The winner is:", self.tic_tac_table[0][0])
        # Second Column
        elif self.tic_tac_table[0][1] == self.tic_tac_table[1][1] == self.tic_tac_table[2][1] != "":
            print("The winner is:", self.tic_tac_table[0][1])
        # Third Column
        elif self.tic_tac_table[2][0] == self.tic_tac_table[2][1] == self.tic_tac_table[2][2] != "":
            print("The winner is:", self.tic_tac_table[2][0])

        # Diagonal 1
        elif self.tic_tac_table[0][0] == self.tic_tac_table[1][1] == self.tic_tac_table[2][2] != "":
            print("The winner is:", self.tic_tac_table[0][0])
        # Diagonal 2
        elif self.tic_tac_table[0][2] == self.tic_tac_table[1][1] == self.tic_tac_table[2][0] != "":
            print("The winner is:", self.tic_tac_table[0][2])

    def check_mouse_coords(self):
        """
        Checks if the player clicked on a tile on the table
        :return: the tile's top left coordinate
        """

        pygame.time.delay(100)

        # Mouse Action
        mouse_coord = pygame.mouse.get_pos()
        for tile in self.board.tiles_on_board:
            if tile.collidepoint(mouse_coord):
                return tile.topleft

    def start_game(self):
        """
        The game loop starts here and stops when the player quits the game
        """
        self.board.draw_table()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    tile = self.check_mouse_coords()
                    self.update_player(tile)
                    self.check_winner()
                    print(self)

        else:
            pygame.quit()


if __name__ == '__main__':
    pygame.init()

    game = TicTacToe()
    game.start_game()

"""
# MENU
# Keyboard Action
elif event.type == pygame.KEYDOWN:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this

    elif keys[pygame.K_RIGHT]:

    elif keys[pygame.K_UP]:

    elif keys[pygame.K_DOWN]:
"""
