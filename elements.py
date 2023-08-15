from config import *
import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, name, element_class, image_path):
        super().__init__(name, element_class, image_path)
        self.picture = pygame.image.load(image_path)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()
        self.mouse_pos = pygame.mouse.get_pos()

    def draw_element(self):
        self.image.blit(self.picture, self.mouse_pos)
