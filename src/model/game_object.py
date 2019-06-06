from abc import abstractmethod
import uuid


class GameObject:

    def __init__(self, position):
        self.position = position
        self.id = uuid.uuid4()

    @abstractmethod
    def update(self, *args):
        return self.position

    def __str__(self):
        return "Game object {} at position {}".format(self.position, self.id)
