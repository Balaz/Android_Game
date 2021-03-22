# TODO: Write the GAME

import pygame

class TicTaToe:
    def __init__(self):
        pass


# (0,0) = Top Left Corner
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
GAME_NAME = "TIC TAC TOE MotherFucker"

player = {
    "x_coord": 50,
    "y_coord": 50,
    "step": 20
}

tile_1 = {
    "x_coord": 200,
    "y_coord": 0,
    "side": 200,
    "width": 5
}


def drawTable():

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(GAME_NAME)

    #Red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (player["x_coord"], player["y_coord"], 50, 50))

    table_color = pygame.Color(30, 180, 0)
    # Vertical
    pygame.draw.line(screen, table_color, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, table_color, (400, 0), (400, 600), 10)
    pygame.draw.line(screen, table_color, (600, 0), (600, 600), 10)
    pygame.draw.line(screen, table_color, (800, 0), (800, 600), 10)

    # Horizontal
    pygame.draw.line(screen, table_color, (200, 0), (800, 0), 10)
    pygame.draw.line(screen, table_color, (200, 200), (800, 200), 10)
    pygame.draw.line(screen, table_color, (200, 400), (800, 400), 10)
    pygame.draw.line(screen, table_color, (200, 600), (800, 600), 10)

def check_event(event):
    pass


def start_game():
    running = True
    while running:
        for event in pygame.event.get():
            pygame.time.delay(100)

            if event.type == pygame.QUIT:
                running = False

            # Keyboard Action
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this
                    player["x_coord"] -= player["step"]
                elif keys[pygame.K_RIGHT]:
                    player["x_coord"] += player["step"]
                elif keys[pygame.K_UP]:
                    player["y_coord"] -= player["step"]
                elif keys[pygame.K_DOWN]:
                    player["y_coord"] += player["step"]

            # Mouse Action
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coord = pygame.mouse.get_pos()
                if 200 < mouse_coord[0] < 400 and 0 < mouse_coord[1] < 200:
                    print(mouse_coord)

            else:
                pygame.quit()
            #pygame.display.update()


if __name__ == '__main__':

    pygame.init()

    drawTable()

    start_game()
