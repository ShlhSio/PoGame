from objets import *
from world import *
from constants import *

pygame.init()
def create_screen(world):
    # Initialise screen

    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE + ITEM_SIZE*8
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("Infiltrator Game")

    # Fill background with white
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

   #blit my layer
    layer = pygame.image.load('images/pogame_background.jpg')
    layer = pygame.transform.scale(layer, (WORLD_WIDTH*ROOM_SIZE, WORLD_HEIGHT*ROOM_SIZE))
    background.blit(layer, (0, 0, WORLD_HEIGHT*ROOM_SIZE, WORLD_WIDTH*ROOM_SIZE))


    #background = pygame.transform.scale(background, (board_width, board_height))
    #rect = background.get_rect()
    #rect = rect.move((0, 0))
    #screen.blit(background, rect)

    return screen, background


def update_screen(screen, background, world, player, inventory):

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
    # affichage de l'inventaire
    x = 10
    rang = 0
    for item in inventory:
        y = WORLD_HEIGHT * ROOM_SIZE + ITEM_SIZE * 4
        color = item_color(inventory[rang])
        pygame.draw.circle(
            screen,
            color,
            (x, y),
            ITEM_SIZE,
        )
        x += ITEM_SIZE*3
        rang += 1

    pygame.display.flip()
