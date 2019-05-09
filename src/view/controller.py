from view import View


class Controller:
    def __init__(self):
        self.view = View(1300, 800)
        self.view.change_view_state(View.STARTVIEW)

        start_button = self.view.get_element_by_id("start_button")
        start_button.on("click", self.view.change_view_state, state=View.GAMEVIEW)

        # start_message = self.view.get_element_by_id("headline")
        # first_button = self.view.get_element_by_id("start_button")
        # text_button = self.view.get_element_by_id("starttext")

        # start_button.on("click", greet)
        # first_button.on("hover", lambda: print("Hover!"))

        # self.game_loop()

    def game_loop(self):
        while True:
            self.view.events()
            self.view.draw()


if __name__ == "__main__":
    controller = Controller()
    controller.game_loop()
