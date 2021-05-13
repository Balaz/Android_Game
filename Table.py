"""
Contains all the information related to the Board class
"""

from Macros import *


class Board:
    """
    Represents the table for the game, where the tiles are part of the board
     - if I click on a certain Tile object it will change accordingly to the game
    """

    def __init__(self):
        """
        Initializes the size of one tile
        the positions of the tiles based on the screen (macro)
        and the positions of the tiles based on the table
        """

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
            (0, 0): (200, 0),
            (0, 1): (400, 0),
            (0, 2): (600, 0),
            (200, 0): (0, 0),
            (400, 0): (0, 1),
            (600, 0): (0, 2),

            # Second Row
            (1, 0): (200, 200),
            (1, 1): (400, 200),
            (1, 2): (600, 200),
            (200, 200): (1, 0),
            (400, 200): (1, 1),
            (600, 200): (1, 2),

            # Third Row
            (2, 0): (200, 400),
            (2, 1): (400, 400),
            (2, 2): (600, 400),
            (200, 400): (2, 0),
            (400, 400): (2, 1),
            (600, 400): (2, 2),
        }

    @staticmethod
    def draw_lines():
        """
        Draws the vertical & horizontal lines on the table
        """

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
        """
        Draws all the images and lines on the screen
        """

        background.blit(background_image, (0, 0))

        self.draw_lines()

        screen.blit(background, (0, 0))
        pygame.display.update()
