from collections import OrderedDict

import pygame
from pygame import K_UP, K_RIGHT, K_DOWN, K_LEFT, K_PLUS, K_MINUS

from .view_element import ViewElement
from .nest import Nest
from .ant import Ant
from .food_source import FoodSource

from src.model.nest import Nest as Model_Nest
from src.model.ant import Ant as Model_Ant
from src.model.ant import Food as Model_Food


class World(ViewElement):
    def __init__(self, view, identifier, x, y, width, height):
        super(World, self).__init__(view, identifier, x, y, width, height)
        self.game_elements = OrderedDict()
        self.i = 0

    def event_handler(self, event):
        # TODO check if needed: pos = self.view.mouse_pos
        pressed_key = pygame.key.get_pressed()

        # Detect if arrow key is still pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == K_UP or event.key == K_RIGHT or event.key == K_DOWN:
                pygame.time.set_timer(pygame.KEYDOWN, 10)
        if event.type == pygame.KEYUP:
            if not (pressed_key[K_LEFT] or pressed_key[K_UP] or pressed_key[K_RIGHT] or pressed_key[K_DOWN]):
                pygame.time.set_timer(pygame.KEYDOWN, 0)

        # Move view position
        increment = 1
        if pressed_key[K_LEFT]:
            self.view.pos[0][0] -= increment
            self.view.pos[1][0] -= increment
        if pressed_key[K_UP]:
            self.view.pos[0][1] += increment
            self.view.pos[1][1] += increment
        if pressed_key[K_RIGHT]:
            self.view.pos[0][0] += increment
            self.view.pos[1][0] += increment
        if pressed_key[K_DOWN]:
            self.view.pos[0][1] -= increment
            self.view.pos[1][1] -= increment

        # Zoom view
        if pressed_key[K_PLUS]:
            pass
        if pressed_key[K_MINUS]:
            pass

    def draw(self):
        for element in self.game_elements.values():
            element.draw()

    def update(self, game_state):
        element_ids = []
        
        for element in game_state:
            element_ids.append(element.id)
            # Update elements
            if element.id in self.game_elements.keys():
                view_element = self.game_elements[element.id]
                view_element.x, view_element.y = self._to_view_coordinates(element.position)
                if type(element) == Model_Ant:
                    view_element.direction = element.direction
                    view_element.has_food = element.has_food
                if type(element) == Model_Food:
                    view_element.value = element.size
            # Create elements
            else:
                view_x, view_y = self._to_view_coordinates(element.position)
                if hasattr(element, 'owner'):
                    color = element.owner.color

                if type(element) == Model_Nest:
                    self.game_elements[element.id] = Nest(self.view, element.id, view_x,
                                                          view_y, 128, color, element.health)

                elif type(element) == Model_Ant:
                    self.game_elements[element.id] = Ant(self.view, element.id, view_x, view_y,
                                                         color, element.direction, element.energy)
                elif type(element) == Model_Food:
                    self.game_elements[element.id] = FoodSource(self.view, element.id, view_x, view_y, 128, 100)
                
                # Establish z-index order
                self.game_elements = OrderedDict(sorted(self.game_elements.items(), key=lambda x: x[1].z_index))

        # Remove out of view elements
        for element_id in list(self.game_elements.keys()):
            if element_id not in element_ids:
                del self.game_elements[element_id]

    def _to_view_coordinates(self, position):
        view_x = int(position[0] - self.view.pos[0][0])
        view_y = int(self.view.pos[0][1] - position[1])
        return view_x, view_y
