import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, position, text):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.text = text
        self.picture = pygame.image.load(image_path)
        self.image = pygame.Surface((50, 50))
        self.image_rect = self.image.get_rect()
        self.image.blit(self.picture, (0, 0))
        self.image_rect.x = position[0]
        self.image_rect.y = position[1]
    def update(self):



class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.elements_button = pygame.image.load('images/button_0.png')
        self.elements_button_rect = pygame.Rect(WIDTH - 50, 0, 50, 50)
        self.screen.blit(self.elements_button, self.elements_button_rect)
        self.esc_button = pygame.image.load('images/esc_button.png')
        self.esc_button_rect = pygame.Rect(WIDTH - 50, 0, 50, 50)
        self.menu_buttons_group = pygame.sprite.Group()
        self.menu_buttons_group.add(self.elements_button_rect, self.esc_button_rect)

    def show_menu(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.esc_button, self.esc_button_rect)
        pygame.display.flip()
        self.screen.blit(self.elements_button, (50, 50))
        self.screen.blit(self.elements_button, (150, 50))
        self.screen.blit(self.elements_button, (250, 50))
        self.screen.blit(self.elements_button, (350, 50))
        self.screen.blit(self.elements_button, (450, 50))
        self.screen.blit(self.elements_button, (550, 50))
        self.screen.blit(self.elements_button, (650, 50))
        self.screen.blit(self.elements_button, (750, 50))
        self.screen.blit(self.elements_button, (850, 50))
        self.screen.blit(self.elements_button, (950, 50))
        self.screen.blit(self.elements_button, (1050, 50))
        self.screen.blit(self.elements_button, (1150, 50))
        self.screen.blit(self.elements_button, (50, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.esc_button_rect.collidepoint(event.pos):
                    # self.menu_buttons_group.vi
                    pass
