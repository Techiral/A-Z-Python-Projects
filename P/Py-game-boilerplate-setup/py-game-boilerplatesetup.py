import pygame as pgm # for pygame
from pygame.locals import * # for QUIT
import sys  # for sys.exit()

pgm.init() #Initilize pygame

WIDTH,HEIGHT = 500,500 #Defining the width and height of the screen
FPS=60  #Defining Frame rate

screen=pgm.display.set_mode((WIDTH,HEIGHT)) #Setting the screen
pgm.display.set_caption("Pygame-Bolierplate-Setup") #Setting the caption of the screen

clock=pgm.time.Clock() #Setting the clock
bool=True

while bool:    #Main loop which functions as the game loop for the time being run during the game
    for event in pgm.event.get():
        if event.type==QUIT:
            bool=False
            pgm.quit()
            sys.exit()  #ALL the game functions will be written here

    screen.fill((255,255,255)) #Filling the screen with white color[Could have been also done with Black using(0,0,0)]
    pgm.display.update() #Updating the screen
    clock.tick(FPS)

pgm.quit() #Quitting pygame
sys.exit() #Quitting the program



