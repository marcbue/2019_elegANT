class GameObject:

    def __init__(self, position):
        self.position = position

    # TODO: make abstract
    def update(self):
        return self.position