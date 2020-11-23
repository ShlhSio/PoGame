import random

from constants import *


def create_world():
    available_items = ["morgenstern", "bouclier", "pilum", "orange", "casque", "bottes"]
    world = []
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            index = get_index(x, y)
            world.insert(index, random.choices(available_items, k=3))
        print()
    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.

    return world


def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target


def get_index(x, y):
    return y * WORLD_WIDTH + x



