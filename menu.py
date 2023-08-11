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

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(mouse_pos):
                self.click_action()

    def click_action(self):
        print('работает')

    def draw(self, screen):
        print('3478378')


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


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.elements_button = MenuButton('images/button_0.png', (WIDTH - 75, 25), 'button', self)
        self.menu_buttons_group = pygame.sprite.Group()
        self.menu_buttons_group.add(self.elements_button)

    def show_menu(self):
        # self.screen.fill(BLACK)
        # pygame.display.flip()
        fire_button = Button('images/element_buttons/fire.png', (50, 75), 'button')
        self.menu_buttons_group.add(fire_button)
        self.menu_buttons_group.draw(self.screen)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         exit()
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1 and self.esc_button_rect.collidepoint(event.pos):
        #         # self.menu_buttons_group.vi
        #         pass

    def hide_menu(self):
        self.menu_buttons_group.clear(self.screen, )

    def draw(self):
        self.menu_buttons_group.draw(self.screen)

    def handle_events(self, event):
        for button in self.menu_buttons_group:
            button.update(event)
