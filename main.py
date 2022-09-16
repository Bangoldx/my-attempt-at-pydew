import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        RES = (1280,720)
        self.screen = pygame.display.set_mode(RES, pygame.SCALED | pygame.RESIZABLE) 
        pygame.display.set_caption('Pydew Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                dt = self.clock.tick() / 1000
                self.level.run(dt)
                pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run() 