import pygame
from config import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.elements_button = pygame.image.load('button_0.png')
        self.elements_button_rect = pygame.Rect(WIDTH - 50, 0, 50, 50)
        self.screen.fill(BLACK)
        self.screen.blit(self.elements_button, self.elements_button_rect)
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.elements_button_rect.collidepoint(event.pos):
                    self.menu()

    def draw(self):
        pygame.display.flip()

    def menu(self):
        self.screen.fill(BLACK)
        self.update()
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
                self.running = False


game = Game()
while game.running:
    game.new()

pygame.quit()
