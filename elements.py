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

    def interaction(self, sprite_2):
        pass


class SolidElement(Element):
    def __init__(self, name, image_path, pos, solidity, fragility, temperature_resistance, element_type):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.fragility = fragility
        self.temperature_resistance = temperature_resistance
        self.element_type = element_type

    def interaction(self, sprite_2):
        if not isinstance(sprite_2, SolidElement):
            if isinstance(sprite_2, LiquidElement):
                if self.solidity < sprite_2.ph:
                    self.kill()
            elif isinstance(sprite_2, FireElement):
                if self.temperature_resistance <= sprite_2.temperature:
                    self.kill()


class FireElement(Element):
    def __init__(self, name, image_path, pos, temperature, element_type):
        super().__init__(name, image_path, pos)
        self.counter = 0
        self.temperature = temperature
        self.element_type = element_type

    def kill(self):
        pass

    # def interaction(self, sprite_2):
    #     if isinstance(sprite_2, LiquidElement):
    #         if self.solidity < sprite_2.ph:
    #             self.kill()
    #     elif isinstance(sprite_2, FireElement):
    #         if self.temperature_resistance <= sprite_2.temperature:
    #             self.kill()

    # def update(self):
    #     print(self.counter)
    #     if self.counter == 60:
    #         pygame.sprite.Sprite.kill(self)
    #         self.counter = 0
    #     else:
    #         self.counter += 1
    #     self.kill()


class LiquidElement(Element):
    def __init__(self, name, image_path, pos, ph, liquidity, evaporation_temperature, element_type):
        super().__init__(name, image_path, pos)
        self.ph = ph
        self.liquidity = liquidity
        self.evaporation_temperature = evaporation_temperature
        self.element_type = element_type

    def update(self):
        if self.rect.y <= 503:
            self.rect.y += self.liquidity // 5

    def interaction(self, sprite_2):
        if isinstance(sprite_2, FireElement):
            if sprite_2.temperature >= self.evaporation_temperature:
                self.kill()
                print('kill')
        elif isinstance(sprite_2, LiquidElement):
            if sprite_2.rect.x >= 0 and sprite_2.rect.right <= WIDTH or \
                    self.rect.x >= 0 and self.rect.right <= WIDTH:
                if sprite_2.rect.x < self.rect.x:
                    self.rect.x = sprite_2.rect.x + sprite_2.rect.width
                elif sprite_2.rect.x >= self.rect.x:
                    self.rect.x = sprite_2.rect.x - sprite_2.rect.width


class ExplodingElement(Element):
    def __init__(self, name, image_path, pos, explosion_power, element_type):
        super().__init__(name, image_path, pos)
        self.explosion_power = explosion_power
        self.element_type = element_type
