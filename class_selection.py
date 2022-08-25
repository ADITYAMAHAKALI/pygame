from pickle import TRUE
import time
from player import player
import sys, pygame
import random
SIZE = WIDTH,HEIGHT = 1000,800
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
PURPLE  = (128,0,128)
FPS = 60
def main():
    pygame.init()
    pygame.display.set_caption('Lost in the Woods')
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render('Select_level', True, WHITE,PURPLE)
    textRect= text.get_rect()
    textRect.center = 500,200
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    bg = pygame.image.load("class_selection_bg.jpeg")
    bg = pygame.transform.scale(bg, (1000 ,800))
    SCREEN.blit(bg,(0,00))
    SCREEN.blit(text,textRect)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        

if __name__ == '__main__':
    main()