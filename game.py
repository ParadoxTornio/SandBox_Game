import pygame
from config import *
from menu import Menu, ELEMENT_SELECTED
from elements import Element


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
            elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_element:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    test_element = Element('test', 'images/test_frame.png', mouse_pos)
                    self.elements_group.add(test_element)
                    # self.elements_group.draw(self.screen)
                    print(mouse_pos, test_element)
                elif event.button == 2:
                    self.selected_element = None
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1 and self.menu.elements_button_rect.collidepoint(event.pos):
            #         self.menu.show_menu()
            self.menu.handle_events(event)

    def draw(self):
        self.elements_group.draw(self.screen)
        pygame.display.flip()

    def add_element(self):
        pass


game = Game()
while game.running:
    game.new()

pygame.quit()
