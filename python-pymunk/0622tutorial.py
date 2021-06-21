import pygame,sys
import pymunk

pygame.init()
display = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
FPS = 50

space = pymunk.Space() #physics world called by "space"
space.gravity = 0,1000
'''
pymunk body : rigid body
Dynamic, kinematic, static
parameter : (mass,moment,body_type)
'''

body = pymunk.Body()
body.position = 400,400
shape = pymunk.Circle(body,10)
shape.density = 1
shape.elasticity = 1
space.add(body, shape)

segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape = pymunk.Segment(segment_body,(0,550),(800,700),5)
segment_shape.elasticity = 1
space.add(segment_body,segment_shape) 


def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() #or break
                sys.exit()
        
        display.fill((255,255,255))
        pygame.draw.circle(display,(255,0,0),body.position,10)
        pygame.draw.line(display,(0,0,0),(0,550),(800,700),5)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS) 

game()
