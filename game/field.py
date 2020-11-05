from game import game_object
import pygame


class Field(game_object.GameObject):
    def __init__(self, x, y, size):
        self.size = size
        super().__init__(x, y)

    def update(self):
        pass

    @property
    def middle(self):
        return self.position.x + self.size / 2, self.position.y + self.size / 2

    @property
    def top_left(self):
        return self.position.x, self.position.y

    @property
    def top_right(self):
        return self.position.x + self.size, self.position.y

    @property
    def bottom_left(self):
        return self.position.x, self.position.y + self.size

    @property
    def bottom_right(self):
        return self.position.x + self.size, self.position.y + self.size

    def draw(self, game):
        white = (255, 255, 255)
        # TOP
        pygame.draw.line(game.screen, white, self.top_left, self.top_right)
        # LEFT
        pygame.draw.line(game.screen, white, self.top_left, self.bottom_left)
        # RIGHT
        pygame.draw.line(game.screen, white, self.top_right, self.bottom_right)
        # BOTTOM
        pygame.draw.line(game.screen, white, self.bottom_left, self.bottom_right)