from src.model.player import Player
from src.model.game_state import GameState
from src.view.view import View


class Controller:
    def __init__(self):
        self.player = Player()
        self.view = View(1300, 800)
        self.view.change_view_state(View.STARTVIEW)
        self.game_state = None

        self.event_list_start_view = {
            'start_button': self.start_button_pressed
        }

        self.event_list_game_view = {
            'build_scout': self.create_ant
        }
        self.game_loop()

    def start_button_pressed(self, color, player_name):
        """
        Event-handler for the start button to change Viewstate from Startview to Gameview
        :param color: Color chosen by player
        :param player_name: Name chosen by player
        :return: returns a game_state object for initialization of the game
        """
        self.view.change_view_state(View.GAMEVIEW)
        player = Player(color, player_name)
        player_list = [player]
        game_state = GameState(player_list)
        return game_state

    def create_ant(self, nest_position, ant_amount):
        """
        Event-handler for creating ants using the create ants button
        :param nest_position: Position of nest that should create ants
        :param ant_amount: Amount of ants created with one event
        :return: empty
        """
        self.game_state.create_ants(nest_position, ant_amount)

    def game_loop(self):
        """
        Main game loop
        :return: empty
        """
        while True:
            if self.game_state is None:
                self.view.draw()

                # Get the list of events from view
                # event_argument_list = self.view.get_event()
                event_argument_list = self.view.events()
                if event_argument_list:
                    print(event_argument_list)

                # Getting events and arguments as two lists
                event = list(event_argument_list.keys())
                args = list(event_argument_list.values())

                # Initializing player and game_state class
                for i in range(len(event)):
                    if event[i] in self.event_list_start_view.keys():
                        if args[i] is not None:
                            self.game_state = self.event_list_start_view[event[i]](*args[i])

            if self.game_state is not None:
                self.view.draw()
                self.view.events()

                # TODO Handling of the events in Gameview
                # # Get the list of events from view
                # # event_argument_list = self.view.get_event()
                # event_argument_list = {}
                # if i == 10:
                #     event_argument_list = {'create_ant_button': ([10, 100], 1)}
                #
                # # Getting events and arguments as two lists
                # event = list(event_argument_list.keys())
                # args = list(event_argument_list.values())
                #
                # # Initializing player and game_state class
                # for i in range(len(event)):
                #     if event[i] in self.event_list_game_view.keys():
                #         if args[i] is not None:
                #             self.game_state = self.event_list_game_view[event[i]](*args[i])


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()
