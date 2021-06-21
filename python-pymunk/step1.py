import pygame,sys,pymunk

#physical body
def create_apple(space):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)    #mass,inertia,body_type
    body.position = (400,0)
    shape = pymunk.Circle(body,80)
    space.add(body,shape)

    #to make visible
    return shape

#visible
def draw_apples(apples):
    for apple in apples:
        pygame.draw.circle(screen,(0,0,0),apple.body.position,80)#when/color/center

def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)

pygame.init() #pygame 초기화
screen = pygame.display.set_mode((800,800)) #screen 만들기
clock = pygame.time.Clock() #game time 생성

#pymunk
space = pymunk.Space() 
space.gravity = (0,100)
apples = []
apples.append(create_apple(space))

Ingame = True

while Ingame: #game loop
    for event in pygame.event.get(): #user input 확인
        if event.type == pygame.QUIT: #close game
            
            pygame.quit()
            sys.exit()

    screen.fill((217,217,217))
    draw_apples(apples)
    space.step(1/50) #??

    pygame.display.update() #rendering the fream
    clock.tick(120)    