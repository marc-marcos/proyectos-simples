import pygame
import time
import numpy

# GLOBAL VARIABLES

ballNum = 20

# BYNARY STUFF

def numToLights(num):
    # bin(n).replace("0b", "")
    binaryNum = bin(num).replace("0b", "")

    binaryStr = (ballNum - len(binaryNum))*"0" + str(binaryNum)  
        
    return list(binaryStr)

# PYGAME STUFF

pygame.init()

pygame.display.set_caption('Binary Clock')
window_surface = pygame.display.set_mode((1000, 200))

background = pygame.Surface((1000, 200))
background.fill(pygame.Color('#000000'))

is_running = True

positions = numpy.linspace(100, 900, 20)

timeAfter = time.time()

while is_running:
    for i in positions:
        pygame.draw.circle(background, (80, 0, 0), [int(i), 100], 12)

    lst = numToLights(int(time.time() - timeAfter))
    print(lst)

    for i in range(len(lst)):
        if lst[i] == "1":
            pygame.draw.circle(background, (200, 0, 0), [int(positions[i]), 100], 10)
            print('in')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))

    pygame.display.update()

