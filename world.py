import random
from constants import *
import math


def create_world():
    world = []
    for y in range(WORLD_WIDTH):
        for x in range(WORLD_HEIGHT):
            world.append([])
            index = get_index(x, y)
            if random.randint(0, 20) == 0 and (x or y):
                world[index].insert(0, gold)
            else:
                pass

        print()

    index_cloak1 = get_index(random.randint(2, WORLD_WIDTH - 1), random.randint(2, WORLD_HEIGHT - 1))
    world[index_cloak1].clear()
    world[index_cloak1].insert(0, invisibility_cloak)
    index_cloak2 = get_index(random.randint(2, WORLD_WIDTH - 1), random.randint(2, WORLD_HEIGHT - 1))
    win_x, win_y = random.randint(2, WORLD_WIDTH-1), random.randint(2, WORLD_HEIGHT-1)
    index_win = get_index(win_x, win_y)
    world[index_win].clear()
    world[index_win].insert(0, portail)
    portal = [win_x, win_y]

    return world, portal


def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    else:
        pass
    return source, target


def get_index(x, y):
    return y * WORLD_HEIGHT + x


def get_room(world, x, y):
    return world[get_index(x, y)]


def item_color(item):
    if item == portail:
        color = (139, 0, 0)
    elif item == gold:
        color = (255, 215, 0)
    elif item == invisibility_cloak:
        color = (83, 133, 80)
    else:
        color = (0, 0, 0)
    return color


class Turret:

    def __init__(self):
        self.x = random.randint(5, WORLD_WIDTH-1)
        self.y = random.randint(5, WORLD_HEIGHT-1)
        self.index = get_index(self.x, self.y)
        self.radius = [self.x * ROOM_SIZE + ROOM_SIZE/2, self.y * ROOM_SIZE+ ROOM_SIZE/2]

    def range(self, player):
        distance = math.sqrt(pow((self.x - player[0]), 2) + pow((self.y - player[1]), 2))
        if distance < 3:
            distance = True
        else:
            distance = False
        return distance




