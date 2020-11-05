from abc import ABC

from . import has_energy
from . import game_object
from . import position
from game import world
from game.spare_battery import SpareBattery
from game import position as pos
import pygame
from game.controllable import Controllable


class Robot(has_energy.HasEnergy, game_object.GameObject, Controllable):
    def __init__(self, x, y, battery_loading):
        self.field_position_x = x
        self.field_position_y = y
        self.battery_loading = battery_loading
        game = world.Game.get_instance()
        pos = game.get_middle_position_of_field(x, y)
        x, y = pos.as_tuple()
        self.battery_picked = False
        super().__init__(x, y)

    def update_position(self):
        game = world.Game.get_instance()
        pos = game.get_middle_position_of_field(self.field_position_x, self.field_position_y)
        x, y = pos.as_tuple()
        self.position.x = x
        self.position.y = y

    def is_spare_battery(self):
        game = world.Game.get_instance()
        objects_at_position = game.get_objects_at(*self.position.as_tuple())
        spare_batterys = list(filter(lambda game_object: isinstance(game_object, SpareBattery), objects_at_position))
        if len(spare_batterys) == 1 and not self.battery_picked:
            spare_loading = spare_batterys[0].get_battery_loading()
            spare_batterys[0].battery_loading = self.get_battery_loading()
            self.battery_loading = spare_loading
            self.battery_picked = True

    def update(self):
        self.is_spare_battery()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
            elif event.key == pygame.K_UP:
                self.move_up()
            elif event.key == pygame.K_DOWN:
                self.move_down()

    def move_up(self):
        return self.move(0, -1)

    def move_down(self):
        return self.move(0, 1)

    def move_right(self):
        return self.move(1, 0)

    def move_left(self):
        return self.move(-1, 0)

    def move(self, x_offset, y_offset):
        if self.battery_loading > 0:
            self.field_position_x += x_offset
            self.field_position_y += y_offset
            self.update_position()
            self.battery_loading -= 1
            self.battery_picked = False
        else:
            print("CANT MOVE !!")
            game = world.Game.get_instance()
            game.game_over()

    def draw(self, game):
        font_size = 60
        myfont = pygame.font.SysFont("Comic Sans MS", font_size)
        # apply it to text on a label
        label = myfont.render(str(self.get_battery_loading()), 1, (0, 255, 0))
        # put the label object on the screen at point x=100, y=100
        x, y = self.position.as_tuple()
        x -= font_size / 4
        y -= font_size / 4
        game.screen.blit(label, (x, y))

    def get_battery_loading(self):
        return self.battery_loading
