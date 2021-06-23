import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

#pymunk : http://www.pymunk.org/en/latest/
#pygame : https://www.pygame.org/docs/ref/time.html#pygame.time.Clock 


#전역변수 설정
SCREEN_WD = 400
SCREEN_HT = 400
TARGET_FPS = 60

screen = pygame.display.set_mode((SCREEN_WD,SCREEN_HT),0,32) #set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
pygame.display.set_caption("PyMunk_Example") #window title
clock = pygame.time.Clock() #create an object to help track time

space = pymunk.Space()
space.gravity = 0, 100
draw_options = pymunk.pygame_util.DrawOptions(screen)
 
#---------바닥------------
ground = pymunk.Body(body_type=pymunk.Body.STATIC)
ground.position = 50, 350
space.add(ground)

ground_shape = pymunk.Segment(ground, (-50, 0), (50, 0), 10)
space.add(ground_shape)
 
 #-------------떨어지는 상자------------
body = pymunk.Body(1, 1666)
body.position = 50, 200
  
poly = pymunk.Poly.create_box(body, (20, 20))

space.add(body, poly)
 
timeStep = 1.0 / 60
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            continue
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            continue

    screen.fill((0, 0, 0, 0))
 
    space.debug_draw(draw_options)
    space.step(timeStep)
 
    pygame.display.flip()
    clock.tick(TARGET_FPS)

 
pygame.quit()
print("done")