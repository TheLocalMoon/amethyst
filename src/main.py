import pygame
from sys import exit

class Amethyst:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load("shared/audio/music/outofrange.ogg")
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    amethyst = Amethyst()
    amethyst.run()
