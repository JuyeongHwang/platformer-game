import pygame,sys
import pymunk


#6/22 볼 class 추가
#6/23 볼 image 추가
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

ball_radius = 30
body = pymunk.Body()
body.position = 400,400
shape = pymunk.Circle(body,ball_radius)
shape.density = 1
shape.elasticity = 1
space.add(body, shape)

segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape = pymunk.Segment(segment_body,(0,550),(800,700),5)
segment_shape.elasticity = 1
space.add(segment_body,segment_shape) 

image = pygame.image.load("apple_item.png")
image = pygame.transform.scale(image,(ball_radius*2,ball_radius*2))

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() #or break
                sys.exit()
        
        display.fill((255,255,255))
        #pygame.draw.circle(display,(255,0,0),body.position,10)
        display.blit(image,(body.position.x-ball_radius,body.position.y-ball_radius))
        pygame.draw.line(display,(0,0,0),(0,550),(800,700),5)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS) 

game()
