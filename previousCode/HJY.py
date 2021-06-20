import pygame
import sys
import random

#Game Variables
pygame.init()
#2 게임창 옵션 설정
size = [1280,720]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
title = "Grow and Kill"
pygame.display.set_caption(title)
game_font = pygame.font.Font('DungGeunMo.ttf',30)
pygame.mixer.pre_init(frequency = 44100, size= 16, channels = 1, buffer =1024 )
die_sound = pygame.mixer.Sound('으악.wav')
item_sound = pygame.mixer.Sound('아삭.wav')
missile_sound = pygame.mixer.Sound('물소리.mp3')
ga_sound = pygame.mixer.Sound('마법.WAV')
hit_sound = pygame.mixer.Sound('뿅.mp3')
poison_sound = pygame.mixer.Sound('독소리.wav')
portion_sound = pygame.mixer.Sound('물소리.mp3')

def draw_bg1():
    screen.blit(bg_surface2,(bg_x_pos,0))
    screen.blit(bg_surface3,(bg_x_pos2,0))
    screen.blit(bg_surface4,(bg_x_pos,0))
    screen.blit(bg_surface5,(bg_x_pos2,0))

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,0))
    screen.blit(floor_surface,(floor_x_pos+1080,0))


def collider_check(a,b):
    if (a.x-b.sx<=b.x) and (b.x<= a.x+a.sx):
        if (a.y-b.sy<=b.y) and (b.y <=a.y+a.sy):
            return True

    return False

def update_score(ps,hs):
    if ps>hs:
        hs = ps
    return hs


class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0
        self.speed = 0
        self.hp = 100
        self.limit = 10
        self.power = 1
        self.score = 0

    def put_img(self,address):
        self.img = pygame.image.load(address).convert_alpha()
        #이미지 크기 가져오기
        self.sx, self.sy = self.img.get_size()

    def resize(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy))
        self.sx,self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img,(self.x,self.y))
        #screen.blit(self.img,(100,100))
        #print(player.x,player.y)
    
    def hp_display(self,x_pos,y_pos):
        hp_surface = game_font.render("HP : "+str(int(self.hp)),True,(255,0,0))
        screen.blit(hp_surface,(x_pos,y_pos))

    #player를 위한 함수들
    #HS => high socre
    def score_display(self,x_pos,ACTIVATION,HS):
        if(ACTIVATION == 0):
            score_surface = game_font.render("Score : "+str(int(self.score)),True,(255,0,0))
            screen.blit(score_surface,(x_pos,40))
        if(ACTIVATION == 1):
            score_surface = game_font.render("Score : "+str(int(self.score)),True,(255,0,0))
            screen.blit(score_surface,(x_pos,40))
            
            high_score_surface = game_font.render("high_Score : "+str(int(HS)),True,(255,255,255))
            screen.blit(high_score_surface,(x_pos-25,600))

    def missile_display(self,x_pos):
        miss_sur = game_font.render("Missile : "+str(int(self.limit)),True,(0,0,0))
        screen.blit(miss_sur,(x_pos,80))
    
    def speedapower(self,x_pos):
        sp = game_font.render("speed : "+str(int(self.speed)),True,(0,0,0))
        po = game_font.render("power: "+str(int(self.power)),True,(0,0,0))
        screen.blit(sp,(x_pos,80))
        screen.blit(po,(x_pos,110))

#배경 불러오기


#bg_sound = pygame.mixer.Sound('리리에(RiRie)-목적지는 저 길 너머야.mp3')

bg_x_pos = 0
bg_x_pos2 = 0
bg1 = obj()
bg1.put_img('0.png')
bg1.resize(1280,720)
bg_surface1 = pygame.image.load('0.png').convert()
bg_surface2 = pygame.image.load('1.png').convert_alpha()
bg_surface2 = pygame.transform.scale(bg_surface2,(2560,720))
bg_surface3 = pygame.image.load('2.png').convert_alpha()
bg_surface3 = pygame.transform.scale(bg_surface3,(2560,720))
bg_surface4 = pygame.image.load('4.png').convert_alpha()
bg_surface4 = pygame.transform.scale(bg_surface4,(2560,720))
bg_surface5 = pygame.image.load('5.png').convert_alpha()
bg_surface5 = pygame.transform.scale(bg_surface5,(2560,720))

floor_surface = pygame.image.load('6.png').convert_alpha()
floor_surface = pygame.transform.scale(floor_surface,(2560,720))
floor_x_pos = 0

player = obj()
player.put_img('Frame_4.png')
player.resize(60,75)
player.x = round(size[0]/7)
player.y = round(size[1]-200)
player.speed = 1
#player.hp = 10000000000000

#print(player.sx,player.sy)

# enemy = obj()
# index = random.randint(0,4)
# enemy.put_img(enemyimg_list[index])
# enemy.resize(60,75)
# enemy.x = round(size[0]/7)
# enemy.y = round(size[1]-200)
# enemy.speed = 0.25

k=0
spawntime = 0
hpd = 0.01
high_score = 0
makeindex0 = 0


m_list = [] #생긴 미사일
em_list = []#enemy missile
e_list = [] #enemy리스트
item_list = []
ga_list = []
hp_list = []
speed_list = []
power_list = []
spawn_pos = [350,400,450,500]

index = random.randint(0,3)

iseixst = False
enemyimg_list = ['Frame_0.png','Frame_1.png','Frame_2.png','Frame_3.png']
portion_img = ['hp.png','speed.png','power.png']
up_go = False
down_go = False
space_go = False
enemy_time = 0

font = pygame.font.Font("DungGeunMo.ttf",80)
text = font.render("GAME OVER",True,(255,0,0))
re_font = pygame.font.Font("DungGeunMo.ttf",40)
text2 = re_font.render("Press 'R' to restart the game",True,(255,0,0))
#시작 대기 화면

Information = False
ACTIVATION = 0
while ACTIVATION == 0:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ACTIVATION = 1
            if event.key == ord('z'):
                Information = True
        if event.type == pygame.KEYUP:
            if event.key == ord('z'):
                Information = False

    #bg_sound.play()
    screen.fill((0,0,0))
    font = pygame.font.Font("DungGeunMo.ttf",40)
    font1 = pygame.font.Font("DungGeunMo.ttf",20)
    if(Information == False):
        start = font.render("Press the Space To Start the Game",True,(255,255,255))
        screen.blit(start,(310,300))
        info = font1.render("Item Information(Z key)",True,(0,255,255))
        screen.blit(info,(510,400))
    
    if(Information == True):
        screen.fill((215,200,200))
        hp = pygame.image.load('hp.png').convert_alpha()
        screen.blit(hp,(size[0]/3,size[1]/4))
        hps = hp.get_size()
        hpi = font1.render("Heals your hp by 10",True,(255,0,0))
        screen.blit(hpi,(size[0]/3+hps[0]*2, size[1]/4))
        
        sp = pygame.image.load('speed.png').convert_alpha()
        screen.blit(sp,(size[0]/3,size[1]/4+50))
        sps = sp.get_size()
        spi = font1.render("Size up by 0.25", True,(0,0,255))
        screen.blit(spi,(size[0]/3+sps[0]*2, size[1]/4+50))

        po = pygame.image.load('power.png').convert_alpha()
        screen.blit(po,(size[0]/3,size[1]/4+100))
        pos = po.get_size()
        poi = font1.render("Power up by 2",True,(139,0,225))
        screen.blit(poi,((size[0]/3+pos[0]*2,size[1]/4+100)))

        ap = pygame.image.load('apple_item.png').convert_alpha()
        screen.blit(ap,(size[0]/3,size[1]/4+150))
        aps = ap.get_size()
        api = font1.render("Can get 3 missiles",True,(255,50,50))
        screen.blit(api,(size[0]/3+aps[0]*2,size[1]/4+150))

        pa = pygame.image.load('poisonapple.png').convert_alpha()
        screen.blit(pa,(size[0]/3+4,size[1]/4+200))
        pas = pa.get_size()
        api = font1.render("Will cut down your blood faster",True,(200,0,225))
        screen.blit(api,((size[0]/3+4+pas[0]*2,size[1]/4+200)))

        
        ga = pygame.image.load('goldenapple.png').convert_alpha()
        screen.blit(ga,(size[0]/3+4,size[1]/4+250))
        pas = ga.get_size()
        api = font1.render("Becomes invincible",True,(220,150,0))
        screen.blit(api,((size[0]/3+4+pas[0]*2,size[1]/4+250)))

        

    pygame.display.flip()



#무적상태
#크기커짐
#시간제한
invincibility = False
ga_respawn = False
ic_time = 15
#무적상태 전 player상태 저장변수
player_speed =0
player_power = 1
player_limit = 10
GO = 0 
ACTIVATION = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0

            if event.key == ord('r') and ACTIVATION == 1:
                m_list.clear()
                em_list.clear()
                e_list.clear()
                item_list.clear()
                ga_list.clear()
                hp_list.clear()
                speed_list.clear()
                power_list.clear()
                player.hp = 100
                player.limit = 10
                player.score = 0
                player.x = 183
                player.y = 520
                player.speed = 1
                player.power = 1
                ACTIVATION = 0
                k=0
                spawntime = 0
                hpd = 0.01
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False
                


    #print(ACTIVATION)
    if ACTIVATION == 0:
    #배경
        screen.blit(bg_surface1,(0,0))
        bg_x_pos-=0.4
        bg_x_pos2-= 0.3

        draw_bg1()
        if(bg_x_pos<=-1280):
            bg_x_pos = 0
        if(bg_x_pos2<=-1280):
            bg_x_pos2 = 0
    #바닥
        floor_x_pos -=1
        draw_floor()
        if(floor_x_pos <= -1280):
            floor_x_pos =0
        #입력,시간에 따른 변화
        if(index != 2 or invincibility == True):
            if up_go == True and player.y>250:
                player.y -= player.speed
            elif down_go == True and player.y<500:      
                player.y += player.speed
        if(index == 2 and invincibility == False):
            if up_go==True and player.y<500:
                player.y += player.speed
            elif down_go == True and player.y>250:
                player.y -= player.speed

        player.hp -= hpd
        if player.hp <=0:
            high_score = update_score(player.score,high_score)
            screen.blit(text,(450,300))
            screen.blit(text2,(350,420))
            
            #GO = 1
            ACTIVATION = 1
            
        #미사일 생성
        k+=1
        if space_go == True and k%10 == 0 and player.limit!=0:
            missile_sound.play()
            missile = obj()
            missile.put_img('ball.png')
            missile.resize(10,10)
            missile.x = player.x + missile.sx + 50
            missile.y = player.y +missile.sy +10
            missile.speed = 5
            player.limit -=1
            #print(player.limit)
            m_list.append(missile)
        
        d_list = []
        for i in range(len(m_list)):
            m = m_list[i]
            m.x += m.speed
            if(m.x>1280):
                d_list.append(i)
        
        #미사일 제거
        for d in d_list:
            del m_list[d]

        spawntime +=1

        if(spawntime%random.randint(200,500)==0):
            em = obj()
            em.put_img('poisonapple.png')
            if(index == 1):
                em.resize(40,40)
            else:
                em.resize(30,30)
            em.x = 1280
            em.y = spawn_pos[random.randint(0,2)]
            if(index == 1):
                em.speed = 4
            else:
                em.speed = 2
            #print(em.speed)
            em_list.append(em)
        
        dem_list = []
        for i in range(len(em_list)):
            emm = em_list[i]
            emm.x -= emm.speed
            if(emm.x<0):
                dem_list.append(i)
        
        for d in dem_list:
            del em_list[d]


        #아이템 생성
        if(spawntime%(random.randint(30,120)) == 0):
            '''
            random.random()>0.88이면 포션 3개중 하나, 아니면 apple
            if random.random()<=0.88:
            '''
            if random.random()<=0.88:
                apple = obj()
                apple.put_img('apple_item.png')
                apple.resize(30,30)
                apple.x = 1280
                apple.y = spawn_pos[random.randint(0,2)]
                apple.speed = 3
                item_list.append(apple)
            else:
                num = random.randint(0,2)
                if(num == 0):
                    hp_portion = obj()
                    hp_portion.put_img(portion_img[num])
                    hp_portion.resize(30,30)
                    hp_portion.x = 1280
                    hp_portion.y = spawn_pos[random.randint(0,2)]
                    hp_portion.speed = 5
                    hp_list.append(hp_portion)
                    #print(hp_list)
                elif(num == 1):
                    speed_portion = obj()
                    speed_portion.put_img(portion_img[num])
                    speed_portion.resize(30,30)
                    speed_portion.x = 1280
                    speed_portion.y = spawn_pos[random.randint(0,2)]
                    speed_portion.speed = 5
                    speed_list.append(speed_portion)
                elif(num == 2):
                    power_portion = obj()
                    power_portion.put_img(portion_img[num])
                    power_portion.resize(30,30)
                    power_portion.x = 1280
                    power_portion.y = spawn_pos[random.randint(0,2)]
                    power_portion.speed = 5
                    power_list.append(power_portion)
                    #print(power_list)
            if random.random()<0.05 and ga_respawn == False:
                ga = obj() #goldenapple
                ga.put_img('goldenapple.png')
                ga.resize(40,40)
                ga.x = 1280
                ga.y = spawn_pos[random.randint(0,2)]
                ga.speed = 3.5
                ga_list.append(ga)

        

    #사과
        di_list = []
        for i in range(len(item_list)):
            item = item_list[i]
            item.x -= item.speed
            if(item.x<0):
                di_list.append(i)

        for di in di_list:
            del item_list[di]

    #황금사과
        dg_list= []
        for i in range(len(ga_list)):
            gaa = ga_list[i]
            gaa.x -= gaa.speed
            if(gaa.x<0):
                dg_list.append(i)

        for dg in dg_list:
            del ga_list[dg]

    #hp
        dp_list = []
        for i in range(len(hp_list)):
            hp = hp_list[i]
            hp.x -= hp.speed
            if(hp.x<0):
                dp_list.append(i)
        for dp in dp_list:
            del hp_list[dp]
    #speed
        ds_list = []
        for i in range(len(speed_list)):
            sp = speed_list[i]
            sp.x -= sp.speed
            if(sp.x<0):
                ds_list.append(i)
        
        for s in ds_list:
            del speed_list[s]

    #power
        dr_list = []
        for i in range(len(power_list)):
            power = power_list[i]
            power.x -= power.speed
            if(power.x<0):
                dr_list.append(i)

        for dr in dr_list:
            del power_list[dr]



        if iseixst == False and len(e_list) ==0:

            isexist = True
            index = random.randint(0,3)
            if(index ==0):
                makeindex0+=1
            enemy = obj()
            enemy.put_img(enemyimg_list[index])
            enemy.resize(60,75)
            enemy.x = 1280-round(size[0]/random.randint(4,9))
            enemy.y = round(size[1]-220)
            if(index != 3):
                enemy.speed = 0.25
            elif(index == 3):
                enemy.speed = 0.6
            enemy.hp = random.randint(20,100)
            enemy.score = enemy.hp
            e_list.append(enemy)
            
            #print(index,"   ",player.speed,"   ",player_speed,"    ",invincibility)
            #print(index)

        #enemy별 특성1
        if(makeindex0>0):
            if(index == 0):
                if(enemy_time<1):
                    player_speed = player.speed
                    enemy_time += 1
                player.speed =  0.5
            else:
                player.speed = player_speed
                enemy_time = 0

        # if(makeindex0>0):
        #     if (index == 0):
        #         #현재 speed 저장
        #         if(enemy_time<1):
        #             player_speed = player.speed
        #         enemy_time += 1
        #         player.speed = 0.5
        #     elif (index != 0):
        #         player.speed = player_speed
        #         enemy_time = 0


        for i in range(len(e_list)):
            en = e_list[i]
            en.y -=en.speed
            if(en.y<=360):
                en.y -=en.speed
                en.y = 500

        #충돌처리(미사일&적)
        dm_list = []
        for i in range(len(m_list)):
            m = m_list[i]
            for j in range(len(e_list)):
                e= e_list[j]
                if(collider_check(m,e) == True):
                    hit_sound.play()
                    dm_list.append(i)
                    e.hp -= player.power
                    if(e.hp <= 0):
                        die_sound.play()
                        e_list.remove(e)
                        isexist = False
                        player.score+=enemy.score

        #오류방지
        dm_list = list(set(dm_list))
        for dm in dm_list:
            del m_list[dm]

        #충돌처리2(독사과& 나)
        dem_list = []
        for i in range(len(em_list)):
            em = em_list[i]
            if collider_check(em,player) == True:
                dem_list.append(i)
                poison_sound.play()
                if(invincibility == True):
                    hpd = 0
                else:
                    if(index!=1):
                        hpd += 0.01
                    elif(index == 1):
                        hpd +=0.05
        
        dem_list = list(set(dem_list))
        
        for dem in dem_list:
            del em_list[dem]

        #충처3(사과&플레이어)
        di_list = []
        for i in range(len(item_list)):
            item = item_list[i]
            if collider_check(item,player)==True:
                di_list.append(i)
                item_sound.play()
                if(invincibility == True):
                    player_limit +=3
                elif(invincibility == False):
                    player.limit+=3
        di_list = list(set(di_list))
                            
        for di in di_list:
            del item_list[di]
        #황금사과 & 플레이어
        dga_list = []
        for i in range(len(ga_list)):
            gaa = ga_list[i]
            if collider_check(player,gaa)==True and invincibility == False:
        
                player_limit = player.limit
                player_power = player.power
                '''
                index == 0일때, 0.5인 스피드가 저장되면 안되기 때문에 조건을 달아준다.
                '''
                if(player.speed>0.9):
                    player_speed = player.speed
                    print("2  ",index,"   ",player.speed,"   ",player_speed,"    ",invincibility)
                ga_sound.play()
                dga_list.append(i)
                #skill
                hpd = 0.01
                invincibility = True
                ga_respawn = True
        
        
        if invincibility == True:
            ic_time -= 0.01
            #print(ic_time)
            player.put_img('goldenplayer.png')
            hpd = 0
            player.power = 5
            player.resize(100,120)
            player.speed = 3.5 #황금사과를 먹었을 때, 스피드는 3.5가 된다
            player.limit = 10000
            if(ic_time<=0):
                player.put_img('Frame_4.png')
                ic_time = 15
                player.resize(60,75)
                player.speed = player_speed #황금사과 시간이 끝나면 황금사과를 먹기 전, 스피드로 돌아간다.
                                            #황금사과 기간동안 스피드 물약을 먹은것도 다 적용이 된다.
                hpd = 0.01
                player.limit = player_limit
                player.power = player_power
                
                invincibility = False
                ga_respawn = False
            
        dga_list = list(set(dga_list))
        
        for dga in dga_list:
            del ga_list[dga]
        
        #플레이어&hp
        
        dh_list = []
        for i in range(len(hp_list)):
            hp = hp_list[i]
            if collider_check(hp,player)==True:
                portion_sound.play()
                dh_list.append(i)
                player.hp += 10
        dh_list = list(set(dh_list))                    
        for dh in dh_list:
            del hp_list[dh]
        
        #플레이어&speed
        
        ds_list = []
        for i in range(len(speed_list)):
            speed = speed_list[i]
            if collider_check(speed,player)==True:
                portion_sound.play()
                ds_list.append(i)
                if(invincibility == True):
                    player_speed +=0.25
                    print(player_speed,"    ",player.speed)
                elif(invincibility == False):
                    if(index == 0):
                        player_speed +=0.25
                        print(player_speed,"    ",player.speed)
                    elif(index !=0):
                        player.speed+=0.25
            
        ds_list = list(set(ds_list))                    
        for ds in ds_list:
            del speed_list[ds]

        #플레이어&power
        
        dr_list = []
        for i in range(len(power_list)):
            power = power_list[i]
            if collider_check(power,player)==True:
                portion_sound.play()
                dr_list.append(i)
                if(invincibility == False):
                    player.power += 1
                elif(invincibility == True):
                    player_power += 1
        
        dr_list = list(set(dr_list))
        
        for dr in dr_list:
            del power_list[dr]
        
        

        #화면에 그리기
        player.show()
        for m in m_list:
            m.show()

        for item in item_list:
            item.show()
            
        for ga in ga_list:
            ga.show()

        for hp in hp_list:
            hp.show()

        for speed in speed_list:
            speed.show()
            
        for power in power_list:
            power.show()


        enemy.show()

        for em in em_list:
            em.show()

        #hud_요소
        player.hp_display(player.x,player.y-20)
        player.score_display(size[0]/2-70,ACTIVATION,high_score)
        player.speedapower(300)
        player.missile_display(50)
        enemy.hp_display(enemy.x,enemy.y-20)
    
        pygame.display.update()
        clock.tick(500)

# #게임 종료
# while GO == 1:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#             GO = 0
        

#     pygame.display.flip()

pygame.quit()