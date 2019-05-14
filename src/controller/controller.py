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
        self.game_loop()

    def start_button_pressed(self, color, player_name):
        player = Player(color, player_name)
        player_list = [player]
        game_state = GameState(player_list)
        return game_state

    def game_loop(self):
        while True:
            if self.game_state is None:
                self.view.draw()
                self.view.events()
                # event_argument_list = self.view.get_event()
                # event = event_argument_list[0][0]
                # args = event_argument_list[0][0]
                # if event in self.event_list_start_view.keys:
                #     if args is not None:
                #         self.game_state = self.event_list_start_view[event](args)
            # if self.game_state is not None:
            #     self.view.draw()
            #     event_argument_list = self.view.get_event()
            #     self.game_state.update()
            #     pass


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()

