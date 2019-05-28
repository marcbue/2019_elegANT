import time
import sys

from threading import Thread

from src.model.player import Player
from src.model.game_state import GameState
from src.view.view import View

from src.settings import all_params


class Controller:
    def __init__(self):

        # self.player = Player()
        self.view = View(1300, 800)
        self.view.change_view_state(View.STARTVIEW)
        self.game_state = None

        self.event_list_start_view = {
            'start_button': self.start_button_pressed,
            'quit_game': self.quit_button_pressed
        }

        self.event_list_game_view = {
            'build_scout': self.create_ant,
            'quit_game': self.quit_button_pressed
        }

        self.event_list = {
            'start_view': self.event_list_start_view,
            'game_view': self.event_list_game_view
        }
        self.game_loop()

    def start_button_pressed(self, color, player_name):
        """
        Event-handler for the start button to change Viewstate from Startview to Gameview
        :param color: Color chosen by player
        :param player_name: Name chosen by player
        :return: returns a game_state object for initialization of the game
        """
        if player_name:
            self.view.change_view_state(View.GAMEVIEW)
            player = Player(color, player_name)
            player_list = [player]
            game_state = GameState(player_list)
            return game_state
        else:
            # TODO Get view to show pop up with message
            print('Player name not entered')

    def quit_button_pressed(self):
        """

        :return: empty
        """
        sys.exit()

    def create_ant(self, button):
        """
        Event-handler for creating ants using the create ants button
        :param nest_position: Position of nest that should create ants
        :param ant_amount: Amount of ants created with one event
        :return: empty
        """
        button.state = 'loading'

        def _create_ant():
            time.sleep(4)
            nest = self.game_state.get_nests()[0]
            self.game_state.create_ants(nest, amount=1)
            self.view.increment_ant_count()

        thread = Thread(target=_create_ant)
        thread.start()

    def get_events(self, view_state):

        # Get the list of events from view
        event_argument_list = self.view.events()
        # Getting events and arguments as two lists
        event = list(event_argument_list.keys())
        args = list(event_argument_list.values())

        for i in range(len(event)):
            if event[i] in self.event_list[view_state].keys():
                if args[i] is not None:
                    if view_state == 'start_view':
                        self.game_state = self.event_list[view_state][event[i]](*args[i])
                    else:
                        self.event_list[view_state][event[i]](*args[i])

    def game_state_init(self):
        """

        :return:
        """

        self.get_events('start_view')

    def game_state_update(self):
        """

        :return:
        """

        self.view.update(self.game_state.get_objects_in_region(self.view.pos[0], self.view.pos[1]))
        self.get_events('game_view')
        self.game_state.update()

    def game_loop(self):
        """
        Main game loop
        :return: empty
        """
        # Currently Frame rate set to 30
        max_frames = all_params.controller_params.framerate
        while True:

            current_time = time.time()

            if self.game_state is None:
                self.view.draw()
                self.game_state_init()

            else:
                self.view.draw()
                self.game_state_update()

            # For frame rate adjustment
            exit_time = time.time()
            time_elapsed = exit_time - current_time
            frames_per_sec = 1. / max_frames
            time.sleep(max(frames_per_sec - time_elapsed, 0))


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()
