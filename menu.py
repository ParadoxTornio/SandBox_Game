import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, position, text):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.text = text
        self.picture = pygame.image.load(image_path)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.image.blit(self.picture, (0, 0))

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(mouse_pos):
                self.click_action()

    def click_action(self):
        print('!')


class MenuButton(Button):
    def __init__(self, image_path, position, text, menu_object):
        super().__init__(image_path, position, text)
        self.menu_object = menu_object
        self.is_open = False
        # self.is_visible = True

    def click_action(self):
        if self.is_open:
            self.menu_object.hide_menu()
        else:
            self.is_open = True
            self.menu_object.show_menu()

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(mouse_pos):
                self.is_open = False
                self.click_action()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.elements_button = MenuButton('images/button_0.png', (WIDTH - 75, 25), 'button', self)
        self.is_visible = True
        self.menu_buttons_group = pygame.sprite.Group()
        self.menu_buttons_group.add(self.elements_button)

    def show_menu(self):
        # self.screen.fill(BLACK)
        # pygame.display.flip()
        water_button = Button('images/element_buttons/water.png', (50, 75), 'button')
        fire_button = Button('images/element_buttons/fire.png', (150, 75), 'button')
        metal_button = Button('images/element_buttons/metal.png', (250, 75), 'button')
        c4_button = Button('images/element_buttons/C4.png', (1150, 75), 'button')
        gunpowder_button = Button('images/element_buttons/gunpowder.png', (50, 175), 'button')
        glass_button = Button('images/element_buttons/glass.png', (550, 75), 'button')
        buf_metal_button = Button('images/element_buttons/buffed_metal.png', (350, 75), 'button')
        lava_button = Button('images/element_buttons/lava.png', (850, 75), 'button')
        poison_button = Button('images/element_buttons/poison.png', (950, 75), 'button')
        bricks_button = Button('images/element_buttons/bricks.png', (650, 75), 'button')
        concrete_button = Button('images/element_buttons/concrete.png', (450, 75), 'button')
        sand_button = Button('images/element_buttons/sand.png', (750, 75), 'button')
        stone_button = Button('images/element_buttons/stone.png', (1050, 75), 'button')
        esc_button = MenuButton('images/esc_button.png', (WIDTH - 75, 25), 'button', self)
        esc_button_rect = pygame.Rect((WIDTH - 75, 25), (50, 50))
        self.menu_buttons_group.add(esc_button)
        self.menu_buttons_group.add(water_button)
        self.menu_buttons_group.add(fire_button)
        self.menu_buttons_group.add(metal_button)
        self.menu_buttons_group.add(buf_metal_button)
        self.menu_buttons_group.add(concrete_button)
        self.menu_buttons_group.add(glass_button)
        self.menu_buttons_group.add(bricks_button)
        self.menu_buttons_group.add(sand_button)
        self.menu_buttons_group.add(lava_button)
        self.menu_buttons_group.add(poison_button)
        self.menu_buttons_group.add(stone_button)
        self.menu_buttons_group.add(c4_button)
        self.menu_buttons_group.add(gunpowder_button)
        self.menu_buttons_group.draw(self.screen)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and esc_button_rect.collidepoint(mouse_pos):
                    # esc_button.update(event)
                    self.screen.fill(BLACK)

    def hide_menu(self):
        # self.menu_buttons_group.clear(self.screen, )
        self.screen.fill(BLACK)
        pygame.display.flip()

    def draw(self):
        self.menu_buttons_group.draw(self.screen)

    def handle_events(self, event):
        for button in self.menu_buttons_group:
            button.update(event)
