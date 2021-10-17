import pygame

class Besouro(pygame.sprite.Sprite):
    def __init__(self, place, cor, tamanho):
        super(Besouro, self).__init__()
        #Define dados
        self.place = place
        self.tamanho = tamanho
        self.cor = cor
        self.surf = pygame.Surface(self.tamanho)
        self.surf.fill(self.cor)
        self.rect = self.surf.get_rect()
        print(place)
        self.rect.center(self.place[0] / 2, self.place[1] / 2)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        pass
