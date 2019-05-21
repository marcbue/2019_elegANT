from abc import abstractmethod

class GameObject:

    def __init__(self, position):
        self.position = position

    @abstractmethod
    def update(self, *args):
        return self.position
