import pygame
from world import *
from constants import *



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

    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            index = get_index(x, y)
            objet_x, objet_y = (x, y)
            if not world[index]:
                pass
            else:
                color = item_color(world[index][0])
                pygame.draw.rect(
                    screen,
                    color,
                    [
                        objet_x * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 4,
                        objet_y * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 4,
                        ITEM_SIZE,
                        ITEM_SIZE,
                    ],
                )
                if len(world[index]) < 2:
                    pass
                else:
                    color = item_color(world[index][1])

                    pygame.draw.rect(
                        screen,
                        color,
                        [
                            objet_x * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 2,
                            objet_y * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 4,
                            ITEM_SIZE,
                            ITEM_SIZE,
                        ],
                    )
                if len(world[index]) < 3:
                    pass
                else:
                    color = item_color(world[index][2])

                    pygame.draw.rect(
                        screen,
                        color,
                        [
                            objet_x * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 1.25,
                            objet_y * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 4,
                            ITEM_SIZE,
                            ITEM_SIZE,
                        ],
                    )
                if len(world[index]) < 4:
                    pass
                else:
                    color = item_color(world[index][3])

                    pygame.draw.rect(
                        screen,
                        color,
                        [
                            objet_x * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 1,
                            objet_y * ROOM_SIZE + (ROOM_SIZE - ITEM_SIZE) / 4,
                            ITEM_SIZE,
                            ITEM_SIZE,
                        ],
                    )
                


    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
