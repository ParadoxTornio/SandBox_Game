from config import *
import pygame
import random
import time


class Element(pygame.sprite.Sprite):
    def __init__(self, name, image_path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image_path
        self.picture = pygame.image.load(self.image_path)
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

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos)
        return new_instance

    def interaction(self, sprite_2):
        if self.groups() == sprite_2.groups() and \
                self.__class__ == sprite_2.__class__:
            sprite_2.kill()


class SteamElement(Element):
    def __init__(self, name, image_path, pos):
        super().__init__(name, image_path, pos)
        self.time_on_screen = None

    def update(self):
        self.rect.y -= 2
        if not self.time_on_screen:
            self.time_on_screen = time.perf_counter()
        elif time.perf_counter() - self.time_on_screen >= 2.5:
            pygame.sprite.Sprite.kill(self)


class SolidElement(Element):
    def __init__(self, name, image_path, pos, solidity, fragility, temperature_resistance, is_melting):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.fragility = fragility
        self.temperature_resistance = temperature_resistance
        self.is_melting = is_melting

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.solidity, self.fragility,
                                      self.temperature_resistance, self.is_melting)
        return new_instance

    def interaction(self, sprite_2):
        super().interaction(sprite_2)
        if not isinstance(sprite_2, SolidElement):
            if isinstance(sprite_2, LiquidElement):
                if self.solidity < sprite_2.ph:
                    try:
                        self.groups()[0].add(SteamElement('пар', 'images/пар.png', [self.rect.x, self.rect.y]))  # noqa
                    except IndexError:
                        pass
                    self.kill()
                else:
                    sprite_2.gravity = False
                    sprite_2.rect.y = self.rect.y - self.rect.height
                    sprite_2.rect.x = sprite_2.previous_x_position
            elif isinstance(sprite_2, FireElement):
                if self.is_melting:
                    if self.temperature_resistance <= sprite_2.temperature:
                        self.kill()


class FireElement(Element):
    def __init__(self, name, image_path, pos, temperature):
        super().__init__(name, image_path, pos)
        self.temperature = temperature
        self.time_on_screen = None

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.temperature)
        return new_instance

    def update(self):
        if not self.time_on_screen:
            self.time_on_screen = time.perf_counter()
        elif time.perf_counter() - self.time_on_screen >= 1:
            pygame.sprite.Sprite.kill(self)


class LiquidElement(Element):
    def __init__(self, name, image_path, pos, ph, liquidity, evaporation_temperature):
        super().__init__(name, image_path, pos)
        self.ph = ph
        self.liquidity = liquidity
        self.evaporation_temperature = evaporation_temperature
        self.gravity = True
        self.direction = None
        self.previous_x_position = self.pos[0]

    def update(self):
        if self.gravity:
            if self.rect.y <= 503:
                self.rect.y += self.liquidity // 5
        self.gravity = True

    def change_position(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.previous_x_position = pos[0]

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.ph, self.liquidity,
                                      self.evaporation_temperature)
        return new_instance

    def interaction(self, sprite_2):
        if isinstance(sprite_2, FireElement):
            if sprite_2.temperature >= self.evaporation_temperature:
                try:
                    self.groups()[0].add(SteamElement('пар', 'images/пар.png', [self.rect.x, self.rect.y]))  # noqa
                except IndexError:
                    pass
                self.kill()
                sprite_2.kill()
        elif isinstance(sprite_2, LiquidElement):
            if sprite_2.rect.x >= 0 and sprite_2.rect.right <= WIDTH or \
                    self.rect.x >= 0 and self.rect.right <= WIDTH:
                self.previous_x_position = self.rect.x
                if not self.direction:
                    if random.random() <= 0.5:
                        self.direction = 'Right'
                    else:
                        self.direction = 'Left'
                elif self.direction == 'Right':
                    self.rect.x = sprite_2.rect.x + sprite_2.rect.width
                else:
                    self.rect.x = sprite_2.rect.x - sprite_2.rect.width


class ExplodingElement(Element):
    def __init__(self, name, image_path, pos, explosion_power, gravity):
        super().__init__(name, image_path, pos)
        self.explosion_power = explosion_power
        self.gravity = gravity

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.explosion_power, self.gravity)
        return new_instance

    def update(self):
        if self.gravity:
            if self.rect.y <= 504:
                self.rect.y += 1

    def explode(self):
        center = self.rect.center
        self.rect.width = self.explosion_power * 12.5
        self.rect.height = self.explosion_power * 12.5
        self.rect.center = center

    def interaction(self, sprite_2):
        super().interaction(sprite_2)
        if isinstance(sprite_2, FireElement):
            self.explode()
        if isinstance(sprite_2, SolidElement):  # не взврывает камень
            if self.explosion_power >= sprite_2.solidity:  # не взврывает камень
                self.kill()  # не взврывает камень
                sprite_2.kill()  # не взврывает камень
        if isinstance(sprite_2, WoodElement):
            if self.explosion_power > sprite_2.solidity:
                self.kill()
                sprite_2.kill()
        if isinstance(sprite_2, GlassElement):
            if self.explosion_power >= sprite_2.solidity:
                self.kill()
                sprite_2.kill()
        else:
            self.kill()


class WoodElement(Element):
    def __init__(self, name, image_path, pos, solidity, temperature_resistance):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.temperature_resistance = temperature_resistance

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.solidity,
                                      self.temperature_resistance)
        return new_instance

    def interaction(self, sprite_2):
        super().interaction(sprite_2)
        if isinstance(sprite_2, FireElement):
            if self.temperature_resistance < sprite_2.temperature:
                self.kill()
        elif isinstance(sprite_2, LiquidElement):
            if self.solidity < sprite_2.ph:
                self.kill()
            else:
                sprite_2.gravity = False


class GlassElement(Element):
    def __init__(self, name, image_path, pos, solidity, temperature_resistance):
        super().__init__(name, image_path, pos)
        self.solidity = solidity
        self.temperature_resistance = temperature_resistance

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.solidity,
                                      self.temperature_resistance)
        return new_instance

    def interaction(self, sprite_2):
        super().interaction(sprite_2)
        if not isinstance(sprite_2, GlassElement):
            if isinstance(sprite_2, LiquidElement):
                sprite_2.gravity = False
                sprite_2.rect.y = self.rect.y - self.rect.height
                sprite_2.rect.x = sprite_2.previous_x_position
        if isinstance(sprite_2, FireElement):
            if sprite_2.temperature >= self.temperature_resistance:
                self.kill()
        if isinstance(sprite_2, LiquidElement):
            if sprite_2.ph >= self.solidity * 10:
                self.kill()
            else:
                sprite_2.gravity = False


class LavaElement(Element):
    def __init__(self, name, image_path, pos, temperature):
        super().__init__(name, image_path, pos)
        self.temperature = temperature
        self.gravity = True

    def update(self):
        if self.gravity:
            if self.rect.y <= 503:
                self.rect.y += 1

    def __copy__(self):
        new_instance = self.__class__(self.name, self.image_path, self.pos, self.temperature)
        return new_instance

    def interaction(self, sprite_2):
        if isinstance(sprite_2, LiquidElement):
            sprite_2.kill()
            try:
                if self.rect.y > sprite_2.rect.y:
                    cords = [self.rect.x, self.rect.y]
                else:
                    cords = [sprite_2.rect.x, sprite_2.rect.y]
                self.groups()[0].add(SteamElement('пар', 'images/пар.png', cords))  # noqa
                self.groups()[0].add(SolidElement('камень', 'images/stone_frame.png', cords  # noqa
                                                  , 15, 5, 2500, False))  # noqa
            except IndexError:
                pass
            self.kill()
        if isinstance(sprite_2, SolidElement):
            if sprite_2.is_melting:
                if self.temperature >= sprite_2.temperature_resistance:
                    sprite_2.kill()
            else:
                self.gravity = False
        if isinstance(sprite_2, WoodElement):
            if self.temperature >= sprite_2.temperature_resistance:
                sprite_2.kill()
        if isinstance(sprite_2, GlassElement):
            if self.temperature >= sprite_2.temperature_resistance:
                sprite_2.kill()
