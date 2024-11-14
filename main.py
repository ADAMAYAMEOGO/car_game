import pygame
import pygame.locals
from vehicle import Vehicle
from car import Car
from truck import Truck
from pygame.locals import *


if __name__ == "__main__":
   
   car1 = Vehicle()
   car2 = Car()
   truck = Truck()
   car2.position=250
   #car2.color = (150, 100, 255)

   print(car1.color)
   #print(car2.color)
   speed_car = 15
   speed_truc = 10
   SCREEN_WIDTH = 800
   SCREEN_HEIGHT = 600
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   running = True

   while running:
      for event in pygame.event.get():
         if event.type == pygame.locals.QUIT:
            running = False

         if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_a:
               car2.backward(speed_car)

            if event.key == pygame.locals.K_z:
               car2.forward(speed_car)

            if event.key == pygame.locals.K_o:
               truck.backward(speed_truc)

            if event.key == pygame.locals.K_p:
               truck.forward(speed_truc)
            

            if event.key == pygame.locals.K_LEFT:
                truck.backward(speed_truc)
                car2.backward(speed_car)
                print(car1.color)

            elif event.key == pygame.locals.K_RIGHT:
                car2.forward(speed_car)
                truck.forward(speed_truc)

            elif event.key == pygame.locals.K_DOWN:
               truck.go_down(speed_truc)
               car2.go_down(speed_car)
               print("en bas")
            elif event.key == pygame.locals.K_UP:
               truck.go_up(speed_truc)
               car2.go_up(speed_car)
               print("en haut")
            elif event.key == pygame.locals.K_ESCAPE:
                running = False

      screen.fill((255, 255, 255))
      truck.draw(screen)
      car2.draw(screen)

      pygame.display.flip()


pygame.quit()



