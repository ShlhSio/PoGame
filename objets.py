import pygame


#test de la POO basique
class Turret:
    calibre = "7.62"

    def __init__(self, size, accuracy, rpm):
        self.size = size
        self.accuracy = accuracy
        self.rpm = rpm

    def __str__(self):
        return f"The turret is {self.size} cm tall, it hits with an accuracy of {self.accuracy*100}% " \
               f"and it fires {self.rpm} bullets per burst"

    def fire(self):
        return f"ratatata"


class BigTurret(Turret):
    def fire(self):
        return f'bambambambam'
    pass

#Je le conserve à titre d'exemple de syntaxe


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('images/Ninja1.png'))
        self.images.append(pygame.image.load('images/Ninja2.png'))
        self.images.append(pygame.image.load('images/Ninja3.png'))
        self.images.append(pygame.image.load('images/Ninja4.png'))
        self.images.append(pygame.image.load('images/Ninja5.png'))
        self.images.append(pygame.image.load('images/Ninja6.png'))
        self.images.append(pygame.image.load('images/Ninja7.png'))
        self.images.append(pygame.image.load('images/Ninja8.png'))
        self.images.append(pygame.image.load('images/Ninja9.png'))
        self.images.append(pygame.image.load('images/Ninja10.png'))
        self.images.append(pygame.image.load('images/Ninja11.png'))
        self.images.append(pygame.image.load('images/Ninja12.png'))
        self.images.append(pygame.image.load('images/Ninja13.png'))
        self.images.append(pygame.image.load('images/Ninja14.png'))
        self.images.append(pygame.image.load('images/Ninja15.png'))
        self.images.append(pygame.image.load('images/Ninja16.png'))
        self.images.append(pygame.image.load('images/Ninja17.png'))
        self.images.append(pygame.image.load('images/Ninja18.png'))
        self.images.append(pygame.image.load('images/Ninja19.png'))
        self.images.append(pygame.image.load('images/Ninja20.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


class Turret(pygame.sprite.Sprite):
    def __init__(self):
        super(Turret, self).__init__()

        self.images = []


        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        #j'imagine qu'il faudra ici qu'une boucle if choisisse le bon sprite en fonction de l'input

        return


