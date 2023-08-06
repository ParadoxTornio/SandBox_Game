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
        self.screen.fill(BLACK)
        self.tutorial_screen()
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
                if event.button == 1:
                    self.screen.fill((0, 0, 0))

    def draw(self):
        pygame.display.flip()

    def tutorial_screen(self):
        sys_font = pygame.font.SysFont('Arial', 75, False, False)
        text_surface = sys_font.render('Чтобы выбрать любой элемент', True, (255, 255, 255))
        text_surface_2 = sys_font.render(' нажми на кнопку в правом верхнем углу', True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect_2 = text_surface_2.get_rect()
        text_rect.center = (WIDTH // 2, 30)
        text_rect_2.center = (WIDTH // 2, 100)
        self.screen.blit(text_surface, text_rect)
        self.screen.blit(text_surface_2, text_rect_2)

    def game_screen(self):
        pass


game = Game()
while game.running:
    game.new()

pygame.quit()
