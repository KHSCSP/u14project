'''
    36 drones are preparing to put on a show. 
    We are given their coordinates and velocities 
    60 seconds before the show begins. 
    Your job is to use the initial information 
    to create a list of Drone objects, 
    ‘move’ the drones for 60 iterations (do NOT 'bounce'),
    then draw the drones to the screen at this point in time.
'''

from drone import Drone
import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Drone Challenge!')
screen.fill((255,255,255))

'''
TODO
read the data from the text file

NOTE each row of the text file includes 4 numbers:
initial x, initial y, x velocity, y velocity

create a list of 'drone' objects

functions you'll need:
.open(), .close(), .split(), .strip()
'''


# TODO for 60 iterations move and draw each drone






# -----no edits needed beyond here -----
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()