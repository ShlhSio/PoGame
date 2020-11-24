import pygame
from world import *
from constants import *
from pogame import *



def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("SciencesPo Game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if bool(x % 2) == bool(y % 2):

                color = (200, 200, 200)
            else:
                color = (250, 250, 250)

            pygame.draw.rect(
                background,
                color,
                [
                    x * ROOM_SIZE,
                    y * ROOM_SIZE,
                    ROOM_SIZE,
                    ROOM_SIZE,
                ],
            )

    return screen, background


def update_screen(screen, background, world, player):
    player_x, player_y = player
    screen.blit(background, (0, 0))
    # couleur (red, green, blue)
    pygame.draw.rect(
        screen,
        (224, 64, 64),
        [
            player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            PLAYER_SIZE,
            PLAYER_SIZE,
        ],
    )

    for y in range(WORLD_WIDTH):
        for x in range(WORLD_WIDTH):
            index = get_index(x, y)
            objet_x, objet_y = (x, y)
            color = item_color(world[index][0])
            pygame.draw.rect(
                screen,
                color,
                # je n'ai pas eu le temps de le faire pour chaque objet donc j'ai testé l'affichage au hasard.
                # j'ai aussi écrit une fonction qui donne la couleur de l'objet en fonction de sa place dans la liste des items disponibles pour la création du monde.
                [
                    objet_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 4,
                    objet_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 4,
                    ITEM_SIZE,
                    ITEM_SIZE,
                ],
            )


    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
