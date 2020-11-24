import pygame

from screen import create_screen, update_screen
from world import *


def main():
    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    player = [0, 0]
    index = get_index(player[0], player[1])
    inventory = []
    print("sol :", world[index], "inventaire :", inventory)


    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, player)
    clock.tick()
    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.

    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).
        index = get_index(player[0], player[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # L'utilisateur souhaite fermer la fenêtre ou quitter par un autre moyen (menus ...).
                # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va se
                # terminer.
                running = False
            elif event.type == pygame.KEYDOWN:
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    # L'utilisateur a appuyé sur "Q", pour Quitter.
                    # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va
                    # se terminer.
                    running = False
                elif event.key == pygame.K_LEFT:
                    if player[0] > 0:
                        player = (player[0] - 1, player[1])
                        index = get_index(player[0], player[1])
                        print("sol :", world[index], "inventaire :", inventory)
                elif event.key == pygame.K_RIGHT:
                    if player[0] < WORLD_WIDTH - 1:
                        player = (player[0] + 1, player[1])
                        index = get_index(player[0], player[1])
                        print("sol :", world[index], "inventaire :", inventory)
                elif event.key == pygame.K_UP:
                    if player[1] > 0:
                        player = (player[0], player[1] - 1)
                        index = get_index(player[0], player[1])
                        print("sol :", world[index], "inventaire :", inventory)
                elif event.key == pygame.K_DOWN:
                    if player[1] < WORLD_HEIGHT - 1:
                        player = (player[0], player[1] + 1)
                        index = get_index(player[0], player[1])
                        print("sol :", world[index], "inventaire :", inventory)
                elif event.key == pygame.K_e:
                    if not world[index]:
                        print("il n'y a rien ici")
                    else:
                        print(f"You have taken {world[index][0]} ")
                        transfer_item(world[index], inventory, world[index][0])
                        print("sol :", world[index], "inventaire :", inventory)

                elif event.key == pygame.K_f:
                    if not inventory:
                        print("il n'y a rien dans votre inventaire")
                    else:
                        print(f"You put {inventory[0]} down ")
                        transfer_item(inventory, world[index], inventory[0])
                        print("sol :", world[index], "inventaire :", inventory)

            elif event.type == pygame.KEYUP:
                # Une touche du clavier a été relachée.
                pass

        update_screen(screen, background, world, player)
        clock.tick()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
