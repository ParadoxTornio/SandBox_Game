import pygame
from config import *
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.screen.fill(BLACK)
        self.menu = Menu(self.screen)
        pygame.display.flip()
        self.running = True

    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def update(self):
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1 and self.menu.elements_button_rect.collidepoint(event.pos):
            #         self.menu.show_menu()
            self.menu.handle_events(event)

    def draw(self):
        self.screen.fill(BLACK)
        self.menu.draw()
        pygame.display.flip()


game = Game()
while game.running:
    game.new()

pygame.quit()
