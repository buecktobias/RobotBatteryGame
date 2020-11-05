from . import has_energy
from . import game_object
from game import world
import pygame


class SpareBattery(has_energy.HasEnergy, game_object.GameObject):
    def __init__(self, x, y, battery_loading):
        self.battery_loading = battery_loading
        game = world.Game.get_instance()
        pos = game.get_middle_position_of_field(x, y)
        x, y = pos.as_tuple()
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self, game):
        font_size = 60
        myfont = pygame.font.SysFont("Comic Sans MS", font_size)
        # apply it to text on a label
        label = myfont.render(str(self.get_battery_loading()), 1, (255, 255, 255))
        # put the label object on the screen at point x=100, y=100
        x, y = self.position.as_tuple()
        x -= font_size / 4
        y -= font_size / 4
        game.screen.blit(label, (x, y))

    def get_battery_loading(self):
        return self.battery_loading
