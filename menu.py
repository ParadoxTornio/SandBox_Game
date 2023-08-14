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
        self.is_visible = False
        # if self.is_visible:
        self.image.blit(self.picture, (0, 0))
        # sys_font = pygame.font.SysFont('Arial', 25, False, False)
        # text_surface = sys_font.render(self.text, True, (194, 23, 29))
        # text_rect = text_surface.get_rect()
        # text_rect.x =
        # self.image.blit(text_surface, text_rect)

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(mouse_pos):
                self.click_action()

    def click_action(self):
        print(self.text)


class MenuButton(Button):
    def __init__(self, image_path, position, text, menu_object):
        super().__init__(image_path, position, text)
        self.menu_object = menu_object
        self.esc_picture = pygame.image.load('images/esc_button.png')
        self.is_open = False

    def click_action(self):
        if self.is_open:
            self.is_open = False
            self.menu_object.hide_menu()
        else:
            self.is_open = True
            self.image.blit(self.esc_picture, (0, 0))
            self.menu_object.show_menu()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.elements_button = MenuButton('images/button_0.png', (WIDTH - 75, 25), 'button', self)
        self.background_image = pygame.image.load('images/background.png')
        self.menu_buttons_group = pygame.sprite.Group()
        self.menu_buttons_group.add(self.elements_button)
        self.draw()
        self.create_buttons()

    def show_menu(self):
        self.menu_buttons_group.draw(self.screen)

    def hide_menu(self):
        self.menu_buttons_group.clear(self.screen, self.background_image)

    def create_buttons(self):
        water_button = Button('images/element_buttons/water.png', (50, 75), 'вода')
        fire_button = Button('images/element_buttons/fire.png', (150, 75), 'огонь')
        metal_button = Button('images/element_buttons/metal.png', (250, 75), 'металл')
        c4_button = Button('images/element_buttons/C4.png', (1150, 75), 'С-4')
        gunpowder_button = Button('images/element_buttons/gunpowder.png', (50, 175), 'порох')
        glass_button = Button('images/element_buttons/glass.png', (550, 75), 'стекло')
        buf_metal_button = Button('images/element_buttons/buffed_metal.png', (350, 75), 'укреплённый металл')
        lava_button = Button('images/element_buttons/lava.png', (850, 75), 'лава')
        poison_button = Button('images/element_buttons/poison.png', (950, 75), 'кислота')
        bricks_button = Button('images/element_buttons/bricks.png', (650, 75), 'кирпичи')
        concrete_button = Button('images/element_buttons/concrete.png', (450, 75), 'бетон')
        sand_button = Button('images/element_buttons/sand.png', (750, 75), 'песок')
        stone_button = Button('images/element_buttons/stone.png', (1050, 75), 'камень')
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

    def draw(self):
        self.menu_buttons_group.draw(self.screen)

    def handle_events(self, event):
        for button in self.menu_buttons_group:
            button.update(event)
