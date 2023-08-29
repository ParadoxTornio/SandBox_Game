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
    def __init__(self, name, image_path, pos, solidity, fragility, temperature_resistance, element_type):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.fragility = fragility
        self.temperature_resistance = temperature_resistance
        self.element_type = element_type

    def interaction(self, sprite_1, sprite_2):
        if sprite_1.element_type != sprite_2.element_type:
            if sprite_1.element_type == 'Solid' and \
                    sprite_2.element_type == 'Liquid':
                if self.solidity < sprite_2.ph:
                    self.kill()
            elif sprite_1.element_type == 'Solid' and \
                    sprite_2.element_type == 'Fire':
                if sprite_1.temperature_resistance <= sprite_2.temperature:
                    self.kill()


class FireElement(Element):
    def __init__(self, name, image_path, pos, temperature, element_type):
        super().__init__(name, image_path, pos)
        self.counter = 0
        self.temperature = temperature
        self.element_type = element_type

    def kill(self):
        pass
    # def update(self):
    #     print(self.counter)
    #     if self.counter == 60:
    #         pygame.sprite.Sprite.kill(self)
    #         self.counter = 0
    #     else:
    #         self.counter += 1
    #     self.kill()


class LiquidElement(Element):
    def __init__(self, name, image_path, pos, ph, liquidity, element_type):
        super().__init__(name, image_path, pos)
        self.ph = ph
        self.liquidity = liquidity
        self.element_type = element_type

    def update(self):
        if self.rect.y <= 503:
            # print(self.rect.center, id(self))
            self.rect.y += self.liquidity // 5
