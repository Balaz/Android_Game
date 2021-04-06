# TODO: Write the GAME

import pygame

# (0,0) = Top Left Corner
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

GAME_NAME = "TIC TAC TOE MotherFucker"
pygame.display.set_caption(GAME_NAME)

RED = (50, 0, 0)
BLUE = (0, 0, 50)


class Tile(pygame.sprite.Sprite):
    def __init__(self, i, j, color):
        # self.x_image = pygame.image.load("images/Player_X.png")
        # screen.blit(self.x_image, (i, j))
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((50, 50))
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.center = (i, j)

all_tiles = pygame.sprite.Group()

class TicTacToe:
    def __init__(self):

        self.tic_tac_table = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
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
            "image": "images/Player_X.png",
            "color" : RED
        }
        self.player2 = {
            "name": "Player O",
            "occupied_tiles": [(), (), ()],
            "turns": 0,
            "image": "images/Player_O.png",
            "color": BLUE
        }
        self.players = [self.player1, self.player2]
        self.turns = 0
        self.player1_turn = True
        self.running = True

    def __str__(self):
        return f"{self.tic_tac_table[0][:]}\n" \
               f"{self.tic_tac_table[1][:]}\n" \
               f"{self.tic_tac_table[2][:]}\n"

    def get_tiles(self, table_coord):
        return self.tiles[table_coord]

    def draw_x(self):
        pass

    @staticmethod
    def draw_table():
        background = pygame.image.load("images/Bamboo_bc_1.bmp")
        screen.blit(background, [0, 0])

        # -- update the table
        line_color = pygame.Color(0, 0, 0)
        # Vertical
        pygame.draw.line(screen, line_color, (200, 0), (200, 600), 10)
        pygame.draw.line(screen, line_color, (400, 0), (400, 600), 10)
        pygame.draw.line(screen, line_color, (600, 0), (600, 600), 10)
        pygame.draw.line(screen, line_color, (800, 0), (800, 600), 10)

        # Horizontal
        pygame.draw.line(screen, line_color, (200, 0), (800, 0), 10)
        pygame.draw.line(screen, line_color, (200, 200), (800, 200), 10)
        pygame.draw.line(screen, line_color, (200, 400), (800, 400), 10)
        pygame.draw.line(screen, line_color, (200, 600), (800, 600), 10)

    def update_player(self, tile):
        if not self.tic_tac_table[tile[0]][tile[1]]:
            player = self.players[0] if self.player1_turn else self.players[1]

            player["occupied_tiles"][player["turns"]] = (tile[0], tile[1])

            #TODO   Wrong IMAGE
            #       No more than 3 X and O
            tiles = self.get_tiles((tile[0], tile[1]))
            all_tiles.add(Tile(tiles[0], tiles[1], player["color"]))

            player["turns"] = (player["turns"] + 1) % 3
            self.player1_turn = not self.player1_turn

    def update_table(self, tile):
        # Clear the Table
        for i in range(3):
            for j in range(3):
                self.tic_tac_table[i][j] = ""
                if (i, j) in self.player1["occupied_tiles"][:]:
                    self.tic_tac_table[i][j] = "X"
                elif (i, j) in self.player2["occupied_tiles"][:]:
                    self.tic_tac_table[i][j] = "O"

                '''
                # draw all X
                x_image = pygame.image.load(self.player1["image"])
                screen.blit(x_image, self.get_tiles((i, j)))
                #x_tile = Tile(i,j)
                #self.Xes.add(x_tile)

                # draw all O
                o_image = pygame.image.load(self.player2["image"])
                screen.blit(o_image, self.get_tiles((i, j)))
                '''

        #all_tiles.update()
        all_tiles.draw(screen)
        pygame.display.flip()

    def check_winner(self):
        # First Row
        if self.tic_tac_table[0][0] == self.tic_tac_table[0][1] == self.tic_tac_table[0][2] != "":
            print("The winner is:", self.tic_tac_table[0][0])
        # Second Row
        elif self.tic_tac_table[1][0] == self.tic_tac_table[1][1] == self.tic_tac_table[1][2] != "":
            print("The winner is:", self.tic_tac_table[1][0])
        # Third Row
        elif self.tic_tac_table[2][0] == self.tic_tac_table[2][1] == self.tic_tac_table[2][2] != "" :
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


    def check_events(self, event):
        pygame.time.delay(100)

        '''
        # Keyboard Action
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this

            elif keys[pygame.K_RIGHT]:

            elif keys[pygame.K_UP]:

            elif keys[pygame.K_DOWN]:

        '''

        # Mouse Action
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()

            # First Row
            if 200 < mouse_coord[0] < 400 and 0 < mouse_coord[1] < 200:
                self.update_player((0, 0))
                self.update_table((0, 0))
            if 400 < mouse_coord[0] < 600 and 0 < mouse_coord[1] < 200:
                self.update_player((0, 1))
                self.update_table((0, 1))
            if 600 < mouse_coord[0] < 800 and 0 < mouse_coord[1] < 200:
                self.update_player((0, 2))
                self.update_table((0, 2))

            # Second Row
            if 200 < mouse_coord[0] < 400 and 200 < mouse_coord[1] < 400:
                self.update_player((1, 0))
                self.update_table((1, 0))
            if 400 < mouse_coord[0] < 600 and 200 < mouse_coord[1] < 400:
                self.update_player((1, 1))
                self.update_table((1, 1))
            if 600 < mouse_coord[0] < 800 and 200 < mouse_coord[1] < 400:
                self.update_player((1, 2))
                self.update_table((1, 2))

            # Third Row
            if 200 < mouse_coord[0] < 400 and 400 < mouse_coord[1] < 600:
                self.update_player((2, 0))
                self.update_table((2, 0))
            if 400 < mouse_coord[0] < 600 and 400 < mouse_coord[1] < 600:
                self.update_player((2, 1))
                self.update_table((2, 1))
            if 600 < mouse_coord[0] < 800 and 400 < mouse_coord[1] < 600:
                self.update_player((2, 2))
                self.update_table((2, 2))

            self.check_winner()
            print(self)

    def start_game(self):
        game.draw_table()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.check_events(event)
                pygame.display.update()

        else:
            pygame.quit()


tile_1 = {
    "x_coord": 200,
    "y_coord": 0,
    "side": 200,
    "width": 5
}

if __name__ == '__main__':
    pygame.init()

    game = TicTacToe()
    game.start_game()

