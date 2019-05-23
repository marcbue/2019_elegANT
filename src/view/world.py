import pygame
from pygame import K_UP, K_RIGHT, K_DOWN, K_LEFT, K_PLUS, K_MINUS

from .view_element import ViewElement
from .nest import Nest
from .ant import Ant

from src.model.game_object import GameObject
from src.model.kd_tree_and_dict import KdTreeAndDict
#from src.model.nest import Nest
from src.model.world import World


class World(ViewElement):
    def __init__(self, view, identifier, x, y, width, height):
        super(World, self).__init__(view, identifier, x, y, width, height)
        self.game_elements = {}
        
        self.game_elements["N1"] = Nest(self.view, "nest", 650, 400, 30, (220, 0, 0))
        self.game_elements["A1"] = Ant(self.view, "ant", 650, 500, 10, (220, 0, 0))
        

    def event_handler(self, event):
        pos = self.view.mouse_pos
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
            if self.view.pos[0][0] > 0:
                self.view.pos[0][0] -= increment
                self.view.pos[1][0] -= increment
        if pressed_key[K_UP]:
            if self.view.pos[0][1] > 0:
                self.view.pos[0][1] -= increment
                self.view.pos[1][1] -= increment
        if pressed_key[K_RIGHT]:
            if self.view.pos[1][0] < 9999:
                self.view.pos[0][0] += increment
                self.view.pos[1][0] += increment
        if pressed_key[K_DOWN]:
            if self.view.pos[1][1] < 9999:
                self.view.pos[0][1] += increment
                self.view.pos[1][1] += increment
        
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
            if element.id in self.game_elements.keys():
                view_element = self.game_elements[element.id]
                # update
                pass
            else:
                # create new
                # view_element = 
                pass
                
            # Remove out of view elements
            for element_id in self.game_elements.keys():
                if element_id not in element_ids:
                    del self.game_elements[element_id]                
            
            # Update position
            view_x, view_y = self._to_view_coordinates(element.position)
            view_element.x, viel_element.x = view_x, view_y

        # Test moving
        for element in self.game_elements.values():
            element.x, element.y = self._to_view_coordinates([200, 300])


    def _to_view_coordinates(self, position):
        view_x = int(position[0] - self.view.pos[0][0])
        view_y = int(position[1] - self.view.pos[0][1])
        return view_x, view_y
        
        
