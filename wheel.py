import pygame

class Wheel:
    def __init__(self):
        self.position = 200
        self.diameter = 10
        self.height = 320

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter 

    def draw(self, screen):
        #print(f"heigt: {self.height}")
        pygame.draw.circle(screen, (0, 0, 0), (self.position, self.height), self.diameter)



