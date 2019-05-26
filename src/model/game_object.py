from abc import abstractmethod
import uuid

class GameObject:

    def __init__(self, position):
        self.position = position
        self.id = uuid.uuid4()

    @abstractmethod
    def update(self, *args):
        return self.position
