import pygame, random
from constantes import *
from auxiliar import Auxiliar

path="../Project2/recursos/Tiles/Tile2.png"
path_9="../Project2/recursos/Tiles/Tile9.png"
path_15="../Project2/recursos/Tiles/Tile15.png"

path_bones_1 = "../Project2/recursos/Tiles/Bone1.png"
path_bones_2= "../Project2/recursos/Tiles/Bone3.png"

class Plataform:
    def __init__(self,x,y,path_image,width,height,type=0):
    
        self.image = Auxiliar.getSurfaceFromSpriteSheet(path_image,1,1)[type]
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w,2)


    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect = self.rect_ground_collition)


plataform_list_3 = []

for x in range(0,800,40):
    plataform_list_3.append(Plataform(x,y=500,path_image= path,width=50,height=50))
for x in range(100,250,40):
    plataform_list_3.append(Plataform(x,y=400,path_image= path_15,width=50,height=50))
for x in range(300,450,40):
    plataform_list_3.append(Plataform(x,y=300,path_image= path_15,width=50,height=50))
for x in range(500,650,40):
    plataform_list_3.append(Plataform(x,y=200,path_image= path_15,width=50,height=50))
for x in range(600,750,40):
    plataform_list_3.append(Plataform(x,y=100,path_image= path_15,width=50,height=50))
print("platform 3:  {}".format(len(plataform_list_3)))


for x in range(0,800,40):
    plataform_list_3.append(Plataform(x,y=550,path_image= path_9,width=50,height=50))












bones_1 = Plataform(x=600,y=500,path_image= path_bones_1,width=50,height=50)
bones_2 = Plataform(x=100,y=500,path_image= path_bones_2,width=50,height=50)
plataform_list_3.append(bones_1)
plataform_list_3.append(bones_2)