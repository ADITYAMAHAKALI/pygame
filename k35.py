import time
from player import player
import sys, pygame
import random

SIZE = WIDTH,HEIGHT = 800,800
BLACK = (0,0,0)
WHITE = (255,255,255)
greed_surface = pygame.image.load("background.jpeg")
greed_surface = pygame.transform.scale(greed_surface, (WIDTH ,HEIGHT))
FPS = 60


def initialize_grid(m,n):
    # here m,n Indicate the dimension of the m X n grid
    cell_width = WIDTH/n
    cell_height = HEIGHT/m
    grid = []
    for y in range(0,m):
        for x in range(0,n):
            temp_rect = pygame.Rect(x*cell_width,y*cell_height,cell_width,cell_height)
            grid.append(temp_rect)
    return grid
            
def select_random_movement(cell_width):
    c = random.randrange(0,4) 
    x = 0 
    y = 0
    # right
    if (c==0):
        x+= cell_width
    # left
    elif(c==1):
        x-=cell_width
    # down
    elif(c==2):
        y+=cell_width
    # up
    elif(c==3):
        y-=cell_width
    return x,y

def check(p1,p2):
    return (p1 == p2)

def play_k35_random(*args,**kwargs):
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    run = True
    p1= player(0,0,"red.png",80)
    p2= player(WIDTH - 80,HEIGHT - 80,"purple.png",80)
    p3= player(WIDTH - 80 ,0,"yellow.png",80)
    trail_p1 = []
    trail_p2 = []
    trail_p3 = []
    red = (255,0,0)
    purple  = (128,0,128)
    yellow = (0,255,255)
    ellipse_size = (0,0,10,10)
    while run:
        dt = CLOCK.tick(10)
        SCREEN.blit(greed_surface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # drawing all rects 
        grid = initialize_grid(10,10)
        for cell in grid:
            pygame.draw.rect(SCREEN,WHITE,cell,1)
        
        x1,y1 = select_random_movement(80)
        x2,y2 = select_random_movement(80)
        x3,y3 = select_random_movement(80)
        p1.move(x1,y1,600,600,dt)
        p2.move(x2,y2,600,600,dt)
        p3.move(x3,y3,600,600,dt)
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        SCREEN.blit(p3.image,p3.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        trail_p3.append((p3.image_loc.centerx,p3.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-2,trail[1]-2,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+2,trail[1]+2,10,10))  
        for trail in trail_p3:
            pygame.draw.ellipse(greed_surface,yellow,(trail[0]-2,trail[1]+2,10,10))  
        pygame.display.update()
        if(check(p1.image_loc.center,p2.image_loc.center) or  check(p1.image_loc.center,p3.image_loc.center) or check(p3.image_loc.center,p2.image_loc.center)):
            time.sleep(2)
            run = False
    return