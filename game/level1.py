from game.level import Level
from game import world
from game.spare_battery import SpareBattery
from game.robot import Robot
from game.position import Position


class Level1(Level):
    def load(self):
        game = world.Game.get_instance()
        spare_battery1 = SpareBattery(4, 0, 3)
        spare_battery2 = SpareBattery(4, 3, 3)
        spare_battery3 = SpareBattery(0, 1, 2)
        robot1 = Robot(2, 4, 9)
        game.create_grid(Position(0, 0), Position(500, 500), 100)
        game.add_game_object(spare_battery1)
        game.add_game_object(spare_battery2)
        game.add_game_object(spare_battery3)
        game.add_game_object(robot1)
