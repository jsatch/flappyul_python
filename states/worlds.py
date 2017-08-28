from states.states import *
from utiles import load_png
import pygame
from pygame.locals import *
import configs
import sys

class MenuState(GameState):
    def __init__(self, gsm):
        super().__init__(gsm)
        self.background, self.background_rect = load_png('bg.png')
        self.play_button, self.play_button_rect  = load_png('but_play.png')
        self.flappy_title, self.flappy_title_rect = load_png('flappy_titulo.png');

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                self.gsm.set(PlayState(self.gsm))

    def update(self, dt):
        self.handle_input()

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.play_button, (
            (configs.GAME_WIDTH / 2) - self.play_button_rect.width / 2,
            (configs.GAME_HEIGHT / 2) - self.play_button_rect.height / 2))
        screen.blit(self.flappy_title, (
            (configs.GAME_WIDTH / 2) - self.flappy_title_rect.width / 2,
            (configs.GAME_HEIGHT / 4) - self.flappy_title_rect.height / 2))

class PlayState(GameState):
    def __init__(self, gsm):
        super().__init__(gsm)
        self.background, self.background_rect = load_png('bg.png')

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update(self, dt):
        self.handle_input()

    def render(self, screen):
        screen.blit(self.background, (0, 0))
