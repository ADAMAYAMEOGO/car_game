import pygame
from wheel import Wheel

class Vehicle:

    # ------------------------------
    # constructor
    # ------------------------------

    def __init__(self):
        self._wheels_espace_x = 150
        self._wheels_espace_y = 40
        self._rear_wheel = Wheel()
        self._front_wheel = Wheel()
        self.color= (0, 0, 255)
        self.position = 450
        self.height= 320
        
        
    # ------------------------------
    # proprities
    # ------------------------------

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
        self._wheels_position()

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color= color

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
        self._wheels_height()

    # ------------------------------
    # methods
    # ------------------------------

    def _wheels_position(self):
        self._front_wheel.position= self.position + self._wheels_espace_x / 5 
        self._rear_wheel.position= self.position - self._wheels_espace_x / 5 

    def _wheels_height(self):
        self._front_wheel.height= self.height + self._wheels_espace_y
        self._rear_wheel.height= self.height + self._wheels_espace_y

    def forward(self, distance):
        self.position += distance

    def backward(self, distance):
        self.position -= distance

    def go_down(self,height):
        self.height += height

    def go_up(self,height):
        self.height -= height

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position, self.height), 50)
        self._rear_wheel.draw(screen)
        self._front_wheel.draw(screen)


