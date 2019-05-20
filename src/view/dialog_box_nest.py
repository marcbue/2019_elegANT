# from nest import Nest
# from button import Button
# from dialog_box import DialogBox
#
#
# # Keep in mind: nest inherits from UIelement, DialogBox from ViewElement
# class DialogBoxNest(DialogBox, Nest):
#     """Defines dialog box for ant-building. Inherits from Nest and Button classes"""
#     def __init__(self, view, identifier, x, y, width, height, radius, active=False):
#         # With super, inherits all variables from Dialog_box, except radius and active from Nest
#         super(DialogBoxNest, self).__init__(view, identifier, x, y, radius, active, width=self.view[0]*0.3,
#                                             height=self.view[1]*0.3)  # to add inherited variable 'ant_types'
#         self.buttons = []
#         self.active = active  # if nest is active, then DialogBoxNest becomes active
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y
#         self.ant_types = ['drone', 'soldier', 'scout']
#
#         type_n = len(self.ant_types)  # Assuming types of ants held in 'ant_types' list
#         for i, type in enumerate(self.ant_types):  # creating button for each ant type
#             x = self.x - self.width/2 + (type_n * self.width/3)
#             y = self.y - radius - self.view[1]*.05
#             # self.view.screen.blit(f"{type}", (x, y - self.view[1]*.05))
#             button = Button(self.view, f"b{i}", x, y, width/3, height, shape="square")
#             # something here to draw sprites on button
#             button.on("click", self.select_type, button_clicked=button)
#             self.buttons.append(button)
#         self.select_type(button)
#
#     # Drawing buttons for three ant classes
#     def draw(self):
#         if self.nest.active:  # if there was a click on the nest...
#             # DialogBox.draw(self.view, "db_nest", self.x, self.y, self.width, self.height)  # draw the dialog box
#             for button in self.buttons:  # then, inside, draw the UIelement buttons for each ant type
#                 button.draw()
#
#     def select_type(self, button_clicked):
#         self.new_type = button_clicked.ant  # 'b{0,1,2}' are identifiers
#         # next, open up build confirmation dialog
#
#     def get_type(self):
#         return self.new_type  # to be called by controller
#
# # TODO 5.20.19
# # Add place to show nest resources
# # Ensure dialog_box.py to close to box
# # Ensure logic in dialog_box.py to draw the box
# # Add sprites to each of three ant type buttons
# # Display (1) resources it takes to build each ant and (2) build time on buttons
# # Add proper name for 'ant_types' class variable from undetermined parent class
# # Specify data type for x,y,height,width in ?float64
# # To create parent class 'confirmation dialog box', which will pass variable 'confirm=True/False'. For ant building,...
# #   quitting game, etc.
#
