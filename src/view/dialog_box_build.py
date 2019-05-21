from button import Button
from dialog_box import DialogBox


# Keep in mind: DialogBox inherits from ViewElement
class DialogBoxBuild(DialogBox):
    """
            A class used to create ant-building buttons
            It inherits from DialogBox class, which inherits from ViewElement
            ...
            Attributes
            ----------
            view: ?
                don't know man
            identifier: string
                identifier for created object
            x: int
                x position of upper left corner of dialog box
            y: int
                y position of upper left corner of dialog box
            width: int
                width of screen
            height: int
                height of screen size
            buttons: list
                list of buttons that build ants
            ant_types: list
                list of ant types (strings)

    """

    def __init__(self, view, identifier, x, y, width, height):
        """

        :param view: (instance) View belonging to current game state
        :param identifier: (str) Object identifier
        :param x: (int) X-position of upper left hand corner of box
        :param y: (int) Y-position of upper left hand corner of box
        :param width: (int) Width of screen
        :param height: (int) Height of screen

        """
        # With super, inherits all variables from Dialog_box
        super(DialogBoxBuild, self).__init__(view, identifier, x=0, y=int(self.view.size[1]*0.8), width=self.view.size[0], height=int(self.view.size[1]*0.2))
        # to add inherited variable 'ant_types'
        self.buttons = []
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.ant_types = ['drone', 'soldier', 'scout']

        type_n = len(self.ant_types)  # Assuming types of ants held in 'ant_types' list
        for i, type in enumerate(self.ant_types):  # creating button for each ant type
            x = self.x + int(self.width/3)
            # self.view.screen.blit(f"{type}", (x, y - self.view[1]*.05))
            button = Button(self.view, f"b{i}", x, y, width/3, height, shape="square")
            # something here to draw sprites on button
            button.on("click", self.select_type, button_clicked=button)
            self.buttons.append(button)
        self.select_type(button)

    # Drawing buttons for three ant classes
    def draw(self):
        # DialogBox.draw(self.view, "db_nest", self.x, self.y, self.width, self.height)  # draw the dialog box
        for button in self.buttons:  # then, inside, draw the UIelement buttons for each ant type
            button.draw()

    def select_type(self, button_clicked):
        self.new_type = button_clicked.ant  # 'b{0,1,2}' are identifiers
        # next, open up build confirmation dialog

    def get_type(self):
        return self.new_type  # to be called by controller

# TODO 5.20.19
# To adjusted build button locations with new view resolution
# Add place to show nest resources
# Ensure logic in dialog_box.py to close the box
# Ensure logic in dialog_box.py to draw the box
# Add sprites to each of three ant type buttons
# Display (1) resources it takes to build each ant and (2) build time on buttons (Safa working on this)
# Add proper name for 'ant_types' class variable from undetermined parent class (to be implemented by controller)
# Specify data type for x,y,height,width in ?float64
# To create parent class 'confirmation dialog box', which will pass variable 'confirm=True/False'. For ant building,...
#   quitting game, etc.

