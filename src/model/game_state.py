from .nest import Nest


class GameState:
    def __init__(self, players):
        self.all_objects = {}
        self.players = players

        for i, player in enumerate(players):
            pos = (i*10, i*10)
            self.all_objects[pos] = [Nest(pos, player.color)]

    def add_objects(self, object_list):
        for object in object_list:
            self.all_objects[object.pos] = object

