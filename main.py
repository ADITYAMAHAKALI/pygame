import time
from player import player
import sys, pygame
import random

SIZE = WIDTH,HEIGHT = 1920,1080
BLACK = (0,0,0)
WHITE = (255,255,255)
greed_surface = pygame.image.load("background.jpeg")
greed_surface = pygame.transform.scale(greed_surface, (600 ,600))
FPS = 60

def initialize_grid(m,n):
    # here m,n Indicate the dimension of the m X n grid
    cell_width = 600/n
    cell_height = 600/m
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


               
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    run = True
    p1= player(0,0,"red.png",60)
    p2= player(600 - 60,600 - 60,"purple.png",60)
    trail_p1 = []
    trail_p2 = []
    red = (255,0,0)
    purple  = (128,0,128)
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
        
        x1,y1 = select_random_movement(60)
        x2,y2 = select_random_movement(60)
        p1.move(x1,y1,600,600,dt)
        p2.move(x2,y2,600,600,dt)
        SCREEN.blit(p1.image,p1.image_loc)
        SCREEN.blit(p2.image,p2.image_loc)
        trail_p1.append((p1.image_loc.centerx,p1.image_loc.centery))
        trail_p2.append((p2.image_loc.centerx,p2.image_loc.centery))
        for trail in trail_p1:
            pygame.draw.ellipse(greed_surface,red,(trail[0]-2,trail[1]-2,10,10))
        for trail in trail_p2:
            pygame.draw.ellipse(greed_surface,purple,(trail[0]+2,trail[1]+2,10,10))   
        pygame.display.update()
        if(check(p1.image_loc.center,p2.image_loc.center)):
            run = False
        
    time.sleep(5)
        
        
    
    
if __name__ == "__main__":
    main()