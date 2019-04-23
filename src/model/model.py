import pickle


class Player:

    def __init__(self, name="player 1", color="red"):
        self.name = name
        self.color = color

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def store_data(self):
        pickle.dump(self, open("save.p", "wb"))

    def read_data(self):
        loaded = pickle.load(open("save.p", "rb"))
        self.__dict__ = loaded.__dict__
