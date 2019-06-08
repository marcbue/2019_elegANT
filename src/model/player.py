import pickle

class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        # TODO: needs to be updated every time as well
        # TODO: for what needed, uuids or also positions?
        # All ants the player owns.
        self.ants = set()

    def __str__(self):
        return "Player {} with color {}".format(self.name, self.color)

    def store_data(self):
        """stores the data of a player in a pickle file"""
        pickle.dump(self, open(str(self.name) + ".p", "wb"))

    def read_data(self, filename):
        """reads the data of a player from a pickle file"""
        loaded = pickle.load(open(filename, "rb"))
        self.__dict__ = loaded.__dict__
