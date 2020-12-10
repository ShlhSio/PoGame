import pygame
from world import *
from constants import *
import os
import sys

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

    return screen, background


def update_screen(screen, background, background_change, world, player, inventory, portal, turret1, turret2, turret3):

    # ajout du fond, le but est qu'il change à chaque nouvelle création
    layer = pygame.image.load(os.path.join('images', 'fond' + str(background_change) + '.jpg'))
    layer = pygame.transform.scale(layer, (WORLD_WIDTH * ROOM_SIZE, WORLD_HEIGHT * ROOM_SIZE))
    background.blit(layer, (0, 0, WORLD_HEIGHT * ROOM_SIZE, WORLD_WIDTH * ROOM_SIZE))

    # affichage du joueur
    player_sprite = pygame.image.load('images/thief.png')
    player_sprite = pygame.transform.scale(player_sprite, (ROOM_SIZE, ROOM_SIZE))
    player_x, player_y = player
    screen.blit(background, (0, 0))
    screen.blit(player_sprite, (player_x * ROOM_SIZE, player_y * ROOM_SIZE))

    # affichage du portail
    win_x, win_y = portal
    portal = pygame.image.load("images/portal.png")
    portal = pygame.transform.scale(portal, (ROOM_SIZE, ROOM_SIZE))
    screen.blit(portal, (win_x * ROOM_SIZE, win_y * ROOM_SIZE))
    # affichage des tours puis de leur portée
    turret = pygame.image.load('images/turret.png')
    turret = pygame.transform.scale(turret, (ROOM_SIZE*3, ROOM_SIZE*3))

    screen.blit(turret, (turret1.x * ROOM_SIZE, turret1.y * ROOM_SIZE))
    screen.blit(turret, (turret2.x * ROOM_SIZE, turret2.y * ROOM_SIZE))
    screen.blit(turret, (turret3.x * ROOM_SIZE, turret3.y * ROOM_SIZE))

    pygame.draw.circle(screen, (0, 0, 0), (turret1.x * ROOM_SIZE + ROOM_SIZE/2, turret1.y * ROOM_SIZE+ ROOM_SIZE/2),
                       ROOM_SIZE * 3, 2)
    pygame.draw.circle(screen, (0, 0, 0), (turret2.x * ROOM_SIZE+ ROOM_SIZE/2, turret2.y * ROOM_SIZE+ ROOM_SIZE/2),
                       ROOM_SIZE * 3, 2)
    pygame.draw.circle(screen, (0, 0, 0), (turret3.x * ROOM_SIZE+ ROOM_SIZE/2, turret3.y * ROOM_SIZE+ ROOM_SIZE/2),
                       ROOM_SIZE * 3, 2)

    # affichage des objets présents sur la map
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            index = get_index(x, y)
            objet_x, objet_y = (x, y)
            if not world[index]:
                pass
            elif portail in world[index]:
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



