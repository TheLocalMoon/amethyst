# --main.py--
import pygame
import json
from pygame.locals import *
from sys import exit
from player import Player

class Amethyst:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.load_map("shared/maps/level1.json") # level 1 map
        self.level = 1

    def load_map(self, map_path):
        with open(map_path, "r") as f:
            map_data = json.load(f)
            self.background_color = map_data.get("background_color", (255, 255, 255))
            ground_data = map_data["ground"]
            self.ground_y = ground_data["y"]
            self.ground_width = ground_data["width"]
            self.ground_height = ground_data["height"]
            self.ground_color = ground_data["color"]
            player_spawn_data = map_data["player_spawn"]
            self.player = Player(player_spawn_data["x"], player_spawn_data["y"], player_spawn_data["size"], player_spawn_data["color"])

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load("shared/audio/music/outofrange.ogg")
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.player.move_left()
                    elif event.key == K_RIGHT:
                        self.player.move_right()
                    elif event.key == K_SPACE:
                        self.player.jump()
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.player.stop_moving()

            self.player.update(self.screen_width, self.screen_height)
            self.player.check_collision(self.ground_y)

            if self.player.x + self.player.size >= self.screen_width:
                self.level += 1
                next_map_path = f"shared/maps/level{self.level}.json"
                try:
                    self.load_map(next_map_path)
                except:
                    self.load_map("shared/maps/level1.json")

            self.screen.fill(self.background_color)
            self.player.draw(self.screen)
            pygame.draw.rect(self.screen, self.ground_color, (0, self.ground_y, self.ground_width, self.ground_height))

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    amethyst = Amethyst()
    amethyst.run()
