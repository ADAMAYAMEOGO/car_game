import pygame
from vehicle import Vehicle
from multipledispatch import dispatch

class Car(Vehicle):

    @dispatch(object)
    def draw(self, screen):
       self.draw(screen,(255, 0, 0))
     
    @dispatch(object, object)
    def draw(self, screen, color):
        pygame.draw.rect(screen, super().color, pygame.Rect(super().position -30, super().height - 20, 60, 60))
        self._rear_wheel.draw(screen)
        self._front_wheel.draw(screen)

