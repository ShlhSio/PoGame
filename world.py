import random

from constants import *


def create_world():
    world = []
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            world.append([])
            index = get_index(x, y)
            if random.randint(0,5) == 0 and (x or y):
                world.insert(index, random.choices(available_items, k=random.randint(1,3)))
        print()
    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.

    return world


def transfer_item(source, target, item):
    source.remove(item)
    target.append(item)
    return source, target


def get_index(x, y):
    return y * WORLD_WIDTH + x


def get_room(world, x, y):
    return world[get_index(x, y)]


def item_color(item):
    if item == available_items[0]:
        color = (255,156,156)
    elif item == available_items[1]:
        color = (255,172,64)
    elif item == available_items[2]:
        color = (255,115,152)
    elif item == available_items[3]:
        color = (194,28,255)
    elif item == available_items[4]:
        color = (124,255,92)
    elif item == available_items[5]:
        color = (198,255,10)
    else:
        color = (0, 0, 0)
    return (color)


