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

space = pymunk.Space() #simulation space
space.gravity = (0,100)

# (0, 50) 위치에 (10, 10) 크기의 박스를 생성한다.
body = pymunk.Body(1, 1666)  # 질량, 모멘트를 지정한다.
body.position = 0, 50
poly = pymunk.Poly.create_box(body,(10,10))
space.add(body,poly)

ground = pymunk.Body(body_type = pymunk.Body.STATIC)
ground.position = 0,0

ground_shape = pymunk.Segment(ground,(-50,0),(50,0),1) #두 점과 두께
space.add(ground_shape)




running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            continue
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            continue

 
pygame.quit()
print("done")