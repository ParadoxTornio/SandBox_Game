from config import *
import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, name, image_path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.picture = pygame.image.load(image_path)
        self.image = pygame.Surface((8, 8))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.name = name
        self.image.blit(self.picture, (0, 0))

    def draw_element(self):
        pass

    def change_position(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class SolidElement(Element):
    def __init__(self, name, image_path, pos, solidity, fragility):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.fragility = fragility


class FireElement(Element):
    def __init__(self, name, image_path, pos):
        super().__init__(name, image_path, pos)

    def update(self):
        counter = 0
        for i in range(10):
            if counter == 10:
                self.kill()
            counter += 1
        pygame.display.flip()


class LiquidElement(Element):
    def __init__(self, name, image_path, pos, ph, liquidity):
        super().__init__(name, image_path, pos)
        self.ph = ph
        self.liquidity = liquidity

    def update(self):
        if self.rect.y <= 500:
            # print(self.rect.center, id(self))
            self.rect.y += self.liquidity // 5
