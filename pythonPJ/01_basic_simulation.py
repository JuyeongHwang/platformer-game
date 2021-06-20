import pymunk
import pygame
import time
import random


display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50

class Ball():
    def __init__(self,x,y):
        #body
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = random.uniform(-400,400) , random.uniform(-400,400)

        #shape
        self.shape = pymunk.Circle(self.body,10)
        self.shape.elasticity = 1 #탄력성
        self.shape.density = 1 #밀도

        #물리 공간에 추가
        space.add(self.body,self.shape)

    #visible
    def draw(self):
        pygame.draw.circle(display,(255,0,0),(self.body.position.x,600-self.body.position.y),10)

def game():
    ball = Ball(100,100)

    #collision handler 7:17
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            display.fill((255,255,255))
            
            ball.draw()
            pygame.display.update()
            clock.tick(FPS)
            space.step(1/FPS)

game()
