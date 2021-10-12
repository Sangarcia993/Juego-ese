import pygame
import time



def move(screen, image, x, y, direction, distance):
    for i in range(x, x+distance, 7):
        screen.blit(image, (i, y))
        #dibuja un cuadrado negro debajo para que no pase eso
        pygame.display.update()

