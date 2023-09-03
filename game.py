import pygame
import copy
from config import *
from menu import Menu, ELEMENT_SELECTED
from utils import custom_collision


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('images/background_2.png')
        self.table_rect = pygame.rect.Rect(0, 82, 1280, 424)
        self.screen.blit(self.background, (0, 0))
        self.clear_picture = pygame.image.load('images/musorka.png')
        self.clear_image = pygame.Surface((50, 50))
        self.clear_rect = self.clear_image.get_rect()
        self.clear_rect.x = 25
        self.clear_rect.y = 25
        self.menu = Menu(self.screen)
        print(self.clear_rect.center)
        pygame.display.flip()
        self.running = True
        self.selected_element = None
        self.elements_group = pygame.sprite.Group()

    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            # print(self.clock.get_fps())
            self.update()
            self.events()
            self.draw()

    def update(self):
        pygame.display.set_caption(str(self.clock.get_fps()))
        self.elements_group.update()

    def events(self):
        for sprite_1 in self.elements_group:
            collision = pygame.sprite.spritecollide(sprite_1, self.elements_group, False, custom_collision)
            for sprite_2 in collision:
                sprite_1.interaction(sprite_2)
        for event in pygame.event.get():
            mouse_event = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == ELEMENT_SELECTED:
                self.selected_element = event.message
                print(event.message)
            elif (mouse_event[0] or mouse_event[2]) and self.selected_element and \
                    self.table_rect.collidepoint(mouse_pos):
                if mouse_event[0]:
                    self.add_element()
                elif mouse_event[2]:
                    self.selected_element = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.clear_rect.collidepoint(mouse_pos):
                    self.elements_group.empty()
            self.menu.handle_events(event)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.elements_group.draw(self.screen)
        self.menu.draw()
        self.screen.blit(self.clear_picture, (25, 25))
        pygame.display.flip()

    def add_element(self):
        mouse_pos = pygame.mouse.get_pos()
        copy_element = copy.copy(self.selected_element)
        copy_element.image = self.selected_element.image.copy()
        copy_element.rect = self.selected_element.rect.copy()
        copy_element.change_position(mouse_pos)
        self.elements_group.add(copy_element)
        print(mouse_pos, copy_element.pos)


game = Game()
while game.running:
    game.new()
pygame.quit()
