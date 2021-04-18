import pygame

# (0,0) = Top Left Corner
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size)

GAME_NAME = "TIC TAC TOE"
pygame.display.set_caption(GAME_NAME)

background = pygame.Surface(screen.get_size())
background_image = pygame.image.load("images/Bamboo_bc_1.bmp").convert()
x_mark = pygame.image.load("images/Player_X.png").convert_alpha()
o_mark = pygame.image.load("images/Player_O.png").convert_alpha()

class Tiles(pygame.sprite.DirtySprite):
    def __init__(self, new_image, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = y

    def update(self):
        self.rect.x += 50
        self.rect.x += 50

# Tiles as pieces on the board - if I click on a certain Tile object it will change accordingly
class Board:
    def __init__(self):
        tile_width = 200
        tile_height = 200

        # First Row
        self.tile1 = pygame.Rect(200, 0, tile_width, tile_height)
        self.tile2 = pygame.Rect(400, 0, tile_width, tile_height)
        self.tile3 = pygame.Rect(600, 0, tile_width, tile_height)
        # Second Row
        self.tile4 = pygame.Rect(200, 200, tile_width, tile_height)
        self.tile5 = pygame.Rect(400, 200, tile_width, tile_height)
        self.tile6 = pygame.Rect(600, 200, tile_width, tile_height)
        # Third Row
        self.tile7 = pygame.Rect(200, 400, tile_width, tile_height)
        self.tile8 = pygame.Rect(400, 400, tile_width, tile_height)
        self.tile9 = pygame.Rect(600, 400, tile_width, tile_height)

        self.tiles_on_board = [
            self.tile1, self.tile2, self.tile3,
            self.tile4, self.tile5, self.tile6,
            self.tile7, self.tile8, self.tile9
        ]

        self.tiles = {
            # First Row
            (200, 0): (0, 0),
            (400, 0): (0, 1),
            (600, 0): (0, 2),

            # Second Row
            (200, 200): (1, 0),
            (400, 200): (1, 1),
            (600, 200): (1, 2),

            # Third Row
            (200, 400): (2, 0),
            (400, 400): (2, 1),
            (600, 400): (2, 2),
        }

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.tic_tac_table = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.tiles = {
            # First Row
            (0, 0): (200, 0),
            (0, 1): (400, 0),
            (0, 2): (600, 0),

            # Second Row
            (1, 0): (200, 200),
            (1, 1): (400, 200),
            (1, 2): (600, 200),

            # Third Row
            (2, 0): (200, 400),
            (2, 1): (400, 400),
            (2, 2): (600, 400),
        }

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


    def draw_lines(self):
        # -- update the table
        line_color = pygame.Color(0, 0, 0)
        # Vertical
        pygame.draw.line(background, line_color, (200, 0), (200, 600), 10)
        pygame.draw.line(background, line_color, (400, 0), (400, 600), 10)
        pygame.draw.line(background, line_color, (600, 0), (600, 600), 10)
        pygame.draw.line(background, line_color, (800, 0), (800, 600), 10)

        # Horizontal
        pygame.draw.line(background, line_color, (200, 0), (800, 0), 10)
        pygame.draw.line(background, line_color, (200, 200), (800, 200), 10)
        pygame.draw.line(background, line_color, (200, 400), (800, 400), 10)
        pygame.draw.line(background, line_color, (200, 600), (800, 600), 10)

    def draw_table(self):
        background.blit(background_image, (0, 0))

        self.draw_lines()

        screen.blit(background, (0, 0))
        pygame.display.update()

    def update_screen(self, tile):
        background.blit(background_image, (0, 0))
        self.draw_lines()

        for coord in self.player1["occupied_tiles"]:
            if coord:
                background.blit(self.player1["image"], self.tiles[coord])
        for coord in self.player2["occupied_tiles"]:
            if coord:
                background.blit(self.player2["image"], self.tiles[coord])

        screen.blit(background, (0, 0))
        pygame.display.update()

    def update_player(self, tile):
        #If the cursor is on the Board
        if tile in self.board.tiles:
            board_coord = self.board.tiles[tile]

            #If there is no mark on the Tile
            if not self.tic_tac_table[board_coord[0]][board_coord[1]]:
                player = self.players[0] if self.player1_turn else self.players[1]
                self.tic_tac_table[board_coord[0]][board_coord[1]] = player["mark"]

                #If we start to override the players' marks
                if player["occupied_tiles"][player["turns"]]:
                    fourth_mark = player["occupied_tiles"][player["turns"]]
                    self.tic_tac_table[fourth_mark[0]][fourth_mark[1]] = ""
                    # CHANGE THIS MARK POSITION TO THE NEW ONE

                player["occupied_tiles"][player["turns"]] = board_coord
                player["turns"] = (player["turns"] + 1) % 3

                self.update_screen(tile)
                self.player1_turn = not self.player1_turn

    def check_winner(self):
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
        pygame.time.delay(100)

        # Mouse Action
        mouse_coord = pygame.mouse.get_pos()
        for tile in self.board.tiles_on_board:
            if tile.collidepoint(mouse_coord):
                return tile.topleft


    def start_game(self):
        game.draw_table()

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

'''
# MENU
# Keyboard Action
elif event.type == pygame.KEYDOWN:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this

    elif keys[pygame.K_RIGHT]:

    elif keys[pygame.K_UP]:

    elif keys[pygame.K_DOWN]:
'''