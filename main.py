import pygame,random
from sys import exit
pygame.display.init()
pygame.font.init()
pygame.display.set_caption('Snake Game')
highscore =0
Screen=[680,680] 
new = True
font = pygame.font.SysFont(' Monospace',70)
font2 = pygame.font.SysFont(' Mono',30)
clock = pygame.time.Clock()             
screen = pygame.display.set_mode((Screen[0],Screen[1]+100))
font1 = pygame.font.SysFont('Comic Sans',43)
def gameover():
    time =0
    while True:
        key = pygame.key.get_pressed()
        if time > 500:
            text1 = font1.render('PRESS SPACE TO PLAY AGAIN',1,(0,0,0))
            screen.blit(text1,(25,Screen[1]//2-100))
            if key[pygame.K_SPACE]:
                Game_Over = False
                return Game_Over
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        text = font.render('GAME  OVER',1,(0,0,0))
        screen.blit(text,(Screen[0]//2-200,Screen[1]//2-200))
        clock.tick(60)
        time+=clock.tick(60)
        pygame.display.update()
def Score():
    score_text = font2.render(f'Score:{score}',1,(0,0,0))
    highscore_text = font2.render(f'HScore:{highscore}',1,(0,0,0))
    
    screen.blit(highscore_text,(350,690))
    screen.blit(score_text,(0,690))
def SetUP():
    global Game_Over,new,direction,snake,snake_pos,snake_quantaty,t_p,vel,vel_y,snake_tail_list,Screen,tiles,VEL,t_p,apple_pos,border
    VEL = 20
    vel = VEL
    vel_y = VEL
    Game_Over = False
    new = True
    snake_pos = [(Screen[0]//VEL)*(VEL//2),(Screen[1]//VEL)*(VEL//2)]#[x,y]
    snake_quantaty= -1
    direction = 'N'
    #U-UP,N-Neutral,D-DOWN,L-LEFT,R-RIGHT
    apple_pos =[]
    pygame.mouse.set_visible(False)
    tiles=[]
    snake_tail_list =[]
    snake = pygame.Rect(snake_pos[0],snake_pos[1],VEL,VEL)
    for h in range(Screen[0]//VEL):
        for w in range(Screen[1]//VEL):
                p =[VEL*(h),VEL*w]
                p1 =[VEL*(h),VEL*w]
                tiles.append(p)
                apple_pos.append(p1)
    t_p = []
    border = pygame.Rect(0,740,Screen[0],100)
def main(): 
    global Game_Over,direction,snake,new,snake_quantaty,snake_pos,vel,vel_y,border,highscore,score
    SetUP()
    while True:
        key = pygame.key.get_pressed()
        FPS = 11
        if Game_Over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if key[pygame.K_UP]:
                if not direction == 'D':
                            direction = 'U'
            if key[pygame.K_DOWN]:
                if not direction == 'U':
                            direction = 'D'
            if key[pygame.K_RIGHT]:
                if not direction == 'L':
                            direction = 'R'
            if key[pygame.K_LEFT]:
                if not direction == 'R':
                            direction = 'L'
            for p in tiles[:]:
                pygame.draw.rect(screen,('WHITE'),pygame.Rect(p[0],p[1],20,20),)
                pygame.draw.rect(screen,(00,0,0),pygame.Rect(p[0],p[1],20,20),1)
            border = pygame.Rect(0,680,Screen[0],100)
            borderleft = pygame.Rect(Screen[0],0,VEL,Screen[1])
            if direction=='U':
                snake_pos[1]-=vel_y
            if direction=='D':
                snake_pos[1]+=vel_y
            if direction=='R':
                snake_pos[0]+=vel
            if direction=='L':
                snake_pos[0]-=vel
            if snake_pos[0]<0 or snake_pos[0]>Screen[0]:
                vel = 0
                if snake_pos[0]<0:
                    snake_pos[0]=0
                if snake_pos[0]>Screen[0]:
                    snake_pos[0]=Screen[0]-VEL
                vel_y=0
                t_p.clear()
                Game_Over = True
                
            if snake.y<0:
                snake.y=0
                vel =0
                vel_y=0 
                t_p.clear()
                Game_Over = True
            if new == True:
                random.shuffle(apple_pos)
                for p1 in apple_pos[:]:
                    apple = pygame.Rect(p1[0],p1[1],VEL,VEL)
                    new = False
            snake_pos2 = [snake.x,snake.y]
            t_p.append(snake_pos2)
            pygame.draw.rect(screen,(100,0,0),apple)
            if snake.colliderect(apple):
                new = True
                snake_quantaty += 1
            score = snake_quantaty+1
            if len(t_p)-1 > snake_quantaty:
                del t_p[0]
            for x in t_p:
                pygame.draw.rect(screen,(0,100,0),(x[0],x[1],VEL,VEL))
                if snake_quantaty >0:
                    if x == snake_pos:
                        vel = 0
                        vel_y = 0
                        Game_Over = True
            if score>=3 and score<6:
                FPS=12
            if score>=6 and score<8:
                FPS=16
            if score>=8 and snake_quantaty<12:
                FPS=18
            if snake_quantaty>=12 and snake_quantaty<18:
                FPS=20
            if snake_quantaty>=18 and snake_quantaty<23:
                FPS=22
            if snake_quantaty>=23 and snake_quantaty<25:
                FPS=24
            if snake_quantaty>=25 and snake_quantaty<26:
                FPS=25
            if snake_quantaty>=26 and snake_quantaty<27:
                FPS=26
            if snake_quantaty>=28:
                FPS=30
            if snake.y>border.y and snake.colliderect(border):
                snake_pos[1] = border.y-VEL
                vel =0
                vel_y =0
                t_p.clear()
                Game_Over=True
            if snake.x>borderleft.x and snake.colliderect(borderleft):
                snake_pos[0] = border.x-VEL
                vel =0
                vel_y =0
                t_p.clear()
                Game_Over=True
            snake = pygame.Rect(snake_pos[0],snake_pos[1],VEL,VEL)
            if score>highscore:
                highscore = score
            pygame.draw.rect(screen,(0,60,0),snake)
            pygame.draw.rect(screen,('GRAY'),border)
            pygame.draw.rect(screen,('WHITE'),borderleft)
            clock.tick(FPS)
            Score()
            pygame.display.update()
        if Game_Over == True:
            pygame.time.delay(500)
            SetUP()
            Game_Over = gameover()
main()
