# --player.py--
import pygame

class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity_y = 0
        self.velocity_x = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.speed = 5
        self.on_ground = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def update(self, screen_width, screen_height):
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        self.x += self.velocity_x

        if self.x <= 0:
            self.x = 0
        elif self.x + self.size >= screen_width:
            self.x = screen_width - self.size
            
        if self.y <= 0:
            self.y = 0
            self.velocity_y = 0
        elif self.y + self.size >= screen_height:
            self.y = screen_height - self.size
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def move_left(self):
        self.velocity_x = -self.speed

    def move_right(self):
        self.velocity_x = self.speed

    def stop_moving(self):
        self.velocity_x = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

    def check_collision(self, ground_y):
        if self.y + self.size >= ground_y:
            self.y = ground_y - self.size
            self.velocity_y = 0
            self.on_ground = True

        if self.y <= 0:
            self.y = 0
            self.velocity_y = 0
