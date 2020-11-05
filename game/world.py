from typing import List

import pygame
from game.game_object import GameObject
from game.field import Field
from game.position import Position
from .controllable import Controllable
from .has_energy import HasEnergy
from .spare_battery import SpareBattery
from .robot import Robot
from game.level1 import Level1


class Game:
    instance = None

    def __init__(self):
        pygame.init()
        self.level = Level1()
        self.size = self.width, self.height = (500, 500)
        self.screen = pygame.display.set_mode(self.size)
        self.done = False
        self.game_objects: List[GameObject] = []
        self.start_game_objects = []
        self.grid = self.from_position, self.to_position, self.field_size = (Position(0, 0), Position(*self.size), 100)
        Game.instance = self

    def get_objects_at(self, x, y):
        return list(filter(lambda game_object: game_object.position.x == x and game_object.position.y == y, self.game_objects))

    @classmethod
    def get_instance(cls):
        return cls.instance

    def get_middle_position_of_field(self, x, y):
        from_x, from_y = self.from_position.as_tuple()
        middle_x = from_x + x * self.field_size + self.field_size / 2
        middle_y = from_y + y * self.field_size + self.field_size / 2
        return Position(middle_x, middle_y)

    def create_grid(self, from_position, to_position, field_size):
        from_x, from_y = from_position.as_tuple()
        to_x, to_y = to_position.as_tuple()

        for y in range(from_y, to_y, field_size):
            for x in range(from_x, to_x, field_size):
                self.game_objects.append(Field(x, y, field_size))

    def start(self):
        self.game_objects = []
        self.level.load()
        self.loop()

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def has_won(self):
        font_size = 60
        myfont = pygame.font.SysFont("Comic Sans MS", font_size)
        # apply it to text on a label
        label = myfont.render("Gewonnen !!", 1, (0, 255, 0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (self.size[0] / 2, self.size[1] / 2))

    def has_lost(self):
        font_size = 60
        myfont = pygame.font.SysFont("Comic Sans MS", font_size)
        # apply it to text on a label
        label = myfont.render("Verloren !!", 1, (0, 255, 0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (self.size[0] / 2, self.size[1] / 2))

    def game_over(self):
        batteries = filter(lambda game_object: isinstance(game_object, HasEnergy), self.game_objects)
        won = all([batterie.get_battery_loading() for batterie in batteries])
        if won:
            self.has_won()
        else:
            self.has_lost()

        self.start()

    def loop(self):
        while not self.done:
            for game_object in self.game_objects:
                game_object.update()
            self.screen.fill((0, 0, 0))
            for game_object in self.game_objects:
                game_object.draw(self)

            controllables = filter(lambda game_object: isinstance(game_object, Controllable), self.game_objects)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                for controllable in controllables:
                    controllable.on_event(event)

            pygame.display.flip()
