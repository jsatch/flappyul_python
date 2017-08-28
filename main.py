import pygame
from pygame.locals import *
from states.worlds import MenuState
from states.states import GameStateManager
import configs

class GameMain:
    def __init__(self, title):
        self.screen = None
        self.gsm = GameStateManager()
        self.title = title
        self.background = None

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            dt = clock.tick(60)
            self.render(clock.get_time())

    def create(self):
        pygame.init()
        self.screen = pygame.display.set_mode((configs.GAME_WIDTH, configs.GAME_HEIGHT))
        pygame.display.set_caption(self.title)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        self.gsm.push(MenuState(self.gsm))

    def render(self, delta):
        self.gsm.update(delta)
        self.gsm.render(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    main = GameMain('Flappy UL')
    main.create()
    main.run()
