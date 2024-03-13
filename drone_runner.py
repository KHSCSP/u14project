'''
    36 drones are preparing to put on a show. 
    We are given their coordinates and velocities 
    60 seconds before the show begins. 
    Your job is to use the initial information 
    to create a list of Drone objects, 
    ‘move’ the drones for 60 iterations, 
    then draw the drones to the screen at this point in time.
'''

from drone import Drone
import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drone Challenge!')
screen.fill((255,255,255))


# get the initial values from the text file
f = open("u14project/in.txt")
lines = f.readlines()
f.close()

# NOTE each row of the text file includes 4 numbers:
# initial x, initial y, x velocity, y velocity

drones = []
for line in lines:
    temp = line.strip().split()
    # TODO convert each item in 'temp' to an int
    # create a Drone object (using x, y, xv, and yv)
    # add this Drone to your list of drones

    

# TODO for 60 iterations move each drone



# TODO draw each drone at its current coordinate




# stay on screen
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -------- end event loop    
