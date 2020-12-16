from screen import *
import pygame




def main():
    alive = True
    running = True
    fps = 30
    background_change = 1
    gold_count = 0
    win_count = 0


    while alive and running:
        # Création du "monde" tel que nous le définissons
        world, portal = create_world()
        # Création des surfaces de dessin
        screen, background = create_screen(world)

        if background_change > 5:
            break
        # Création d'une horloge
        clock = pygame.time.Clock()
        # Initalisation du joueur
        player = [0, 0]
        inventory = []
        index = get_index(player[0], player[1])

        # initialisation des tourelles
        turret1 = Turret()
        turret2 = Turret()
        turret3 = Turret()

        # condition de victoire
        win_count += gold_count

        if win_count > 20:
            break

        update_screen(screen, background, background_change, world, inventory, portal, turret1, turret2, turret3, win_count, player)
        clock.tick(fps)
        quitter = False

        # Une boucle qui relance le jeu à chaque fois que le joueur récupère le datadisc
        while not quitter:
            # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
            update_screen(screen, background, background_change, world, inventory, portal, turret1, turret2, turret3, win_count, player)
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quitter = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if player[0] > 0:
                            player = (player[0] - 1, player[1])
                            index = get_index(player[0], player[1])
                            print("sol :", world[index], "inventaire :", inventory)

                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if player[0] < WORLD_WIDTH - 1:
                            player = (player[0] + 1, player[1])
                            index = get_index(player[0], player[1])
                            print("sol :", world[index], "inventaire :", inventory)

                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        if player[1] > 0:
                            player = (player[0], player[1] - 1)
                            index = get_index(player[0], player[1])
                            print("sol :", world[index], "inventaire :", inventory)

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
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

            # action des tourelles
            index = get_index(player[0], player[1])

            if invisibility_cloak not in inventory:
                if turret1.range(player) or turret2.range(player) or turret3.range(player):
                    break
            else:
                pass

            gold_count = inventory.count("gold")


            # changement de décor
            if portail in inventory:
                background_change += 1
                break

            update_screen(screen, background, background_change, world, inventory, portal, turret1, turret2, turret3, win_count, player)
            clock.tick(fps)


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()








