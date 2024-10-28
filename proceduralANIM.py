import pygame
import math
import random

many = 15

pygame.init()

window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("SNEK")
speed = 100
dir = [0,0]
game_loop = True
rect1 = pygame.rect.FRect
mouse_pos = list(pygame.mouse.get_pos())
prev_pos = list((100,100))
finale = (100,100)

strength = pygame.image.load("dumbell.png").convert_alpha()
haha_1 = pygame.image.load("lmao.jpg").convert()
haha_2 = pygame.image.load("hahahahha.jpg").convert()

class circle:
    def __init__(self,r,val,color="blue"):
        self.r = r
        self.prev_pos = (100+val,100+val)
        self.finale = (100,100)
        self.pip = 100
        self.pop = 100
        self.color = color
    def follow(self,top_poss):
        self.top_pos = top_poss

        self.k = self.top_pos[0] - self.prev_pos[0]
        self.m = self.top_pos[1] - self.prev_pos[1]
        self.lala = self.k**2 + self.m**2

        if self.lala!=0 and math.dist(self.finale,self.top_pos)>self.r:
            self.test = (math.sqrt(self.lala))
            self.I = (self.k/self.test)*-self.r
            self.J = (self.m/self.test)*-self.r
            self.pip = self.top_pos[0] + self.I
            self.pop = self.top_pos[1] + self.J
        
        self.finale = (self.pip,self.pop)
        
        self.c = pygame.draw.circle(window,self.color,self.finale,self.r,30)
        self.prev_pos = list(self.top_pos)

font = pygame.font.Font('freesansbold.ttf', 32)


circles = []
score = 0
pick_rand = True
game_state = "game"
while game_loop:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            game_loop = False
        if keys[pygame.K_SPACE]:
            print("real")
        
    
    if game_state == "game":
        if pick_rand == True:
            xi,yj = random.randint(60,940),random.randint(60,540)
            pick_rand = False

        window.fill((40,40,40))

        for _ in range(many):
            circles.append(circle(10, _*40))
        
        r = 30
        mouse_pos = pygame.mouse.get_pos()
        c1 = pygame.draw.circle(window,(250,0,0),mouse_pos,10,10)
        
        for i in range(many):
            if i != 0:
                circles[i].follow(circles[i-1].finale)
            else:
                circles[i].follow(mouse_pos)

        k = mouse_pos[0] - prev_pos[0]
        m = mouse_pos[1] - prev_pos[1]

        if k<=3 and k>=-3 and m>=3 and m<-3:
            speed =1000
        else:
            speed = 40

        text = font.render(f"score : {score}", True, (250,250,250))
        window.blit(strength,(xi,yj))
        window.blit(text,(20,20))

        if math.dist(mouse_pos,(xi+16,yj+16)) <=12:
            many+=7
            pick_rand = True
            score+=5
        for i in range(len(circles)):
            if circles[i] != 0:
                if math.dist(mouse_pos,circles[i].finale)<=7:
                    print("gameover")
                    circles[i].color = "red"
                    game_state = "lose"
                    break

        c1 = pygame.draw.circle(window,(250,0,0),mouse_pos,10,10)
        prev_pos = list(mouse_pos)

    elif game_state == "lose":
        window.fill((255,255,255))
        window.blit(haha_1,(200,100))
        window.blit(haha_2,(600,100))
        text2 = font.render(f"LMAO imagine scoring only {score}, can't be me hahahahhaa", True, (0,0,0))
        window.blit(text2,(100,400))

    pygame.time.delay(speed)
    pygame.display.flip()

    #todo make snake face rotate towards mouse
    #kill snake if it touches body