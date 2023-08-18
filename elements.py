from config import *
import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, name, image_path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.picture = pygame.image.load(image_path)
        self.image = pygame.Surface((4, 4))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.name = name
        self.image.blit(self.picture, (0, 0))

    def draw_element(self):
        pass


class SolidElement(Element):
    def __init__(self, solidity, fragility):
        pygame.sprite.Sprite.__init__(self)
        self.solidity = solidity
        self.fragility = fragility


class GasElement(Element):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class LiquidElement(Element):
    def __init__(self, ph, liquidity):
        pygame.sprite.Sprite.__init__(self)
        self.ph = ph
        self.liquidity = liquidity
