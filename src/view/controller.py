from view import View
import sys


class Controller:
    def __init__(self):
        self.view = View()
        self.view.change_view_state(View.STARTVIEW)

        start_button = self.view.get_element_by_id("start_button")
        quit_button = self.view.get_element_by_id("quit_button")
        start_button.on("click", self.view.change_view_state, state=View.GAMEVIEW)
        quit_button.on("click", lambda: sys.exit())

    def game_loop(self):
        while True:
            self.view.events()
            self.view.draw()


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()
