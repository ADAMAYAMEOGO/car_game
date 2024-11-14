from vehicle import Vehicle
import pygame

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self._front_wheel.diameter = self._front_wheel.diameter * 2
        self._rear_wheel.diameter = self._rear_wheel.diameter * 2

    def draw(self, screen):
        truck_rect = pygame.Rect(super().position - 30, super().height - 30, 100, 60)
        pygame.draw.rect(screen, super().color, truck_rect)
        self._rear_wheel.draw(screen)
        self._front_wheel.draw(screen)
        window_width = 20
        window_height = 15
        window_color = (255, 255, 255)
        window_x_offset = 5
        window_y_position = truck_rect.top + 5
        pygame.draw.rect(screen, window_color, (truck_rect.left + window_x_offset, window_y_position, window_width, window_height))
        pygame.draw.rect(screen, window_color, (truck_rect.right - window_width - window_x_offset, window_y_position, window_width, window_height))

    
