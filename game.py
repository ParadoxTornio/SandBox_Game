import pygame
from config import *
from menu import Menu, ELEMENT_SELECTED
import copy


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('images/background_2.png')
        self.screen.blit(self.background, (0, 0))
        self.menu = Menu(self.screen)
        pygame.display.flip()
        self.running = True
        self.selected_element = None
        self.elements_group = pygame.sprite.Group()

    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == ELEMENT_SELECTED:
                self.selected_element = event.message
                print(event.message)
            elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_element:
                if event.button == 1:
                    self.add_element()
                elif event.button == 3:
                    self.selected_element = None
            self.menu.handle_events(event)

    def draw(self):
        self.elements_group.draw(self.screen)
        pygame.display.flip()

    def add_element(self):
        mouse_pos = pygame.mouse.get_pos()
        copy_element = copy.copy(self.selected_element)
        copy_element.pos = mouse_pos
        self.elements_group.add(copy_element)
        print(mouse_pos)


game = Game()
while game.running:
    game.new()

pygame.quit()
