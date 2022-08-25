import pygame
class player:
    def __init__(self,start_x,start_y,image,cell_size) -> None:
         self.rad = cell_size
         self.x = start_x + cell_size /2
         self.y = start_y + cell_size /2
         self.image = pygame.image.load(image)
         self.image = pygame.transform.scale(self.image, (60 ,60))
         self.image_loc = self.image.get_rect()
         self.image_loc.center = self.x,self.y 
         
    
    def move(self,x,y,x_lim,y_lim,dt):
        
        if(x>0 and x+self.x <= x_lim ):
            self.x += x #* dt
        elif(y>0 and y+self.y <= y_lim):
            self.y += y #* dt
        elif(x<0 and self.x +x  >= 0):
            self.x += x #* dt
        elif(y<0 and self.y +y >=0):
            self.y += y #* dt
        self.image_loc.center = self.x,self.y
       
         