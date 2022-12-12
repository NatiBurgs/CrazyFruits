import pygame, random
from constantes import *
from auxiliar import Auxiliar

class Plataform:
    '''
    Representa al objeto plataforma del juego.
    '''
    def __init__(self,x,y,width,height,type=0):
    
        self.image = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Terrain/Terrain (16x16).png",7,3)[type]
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w,2)


    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect = self.rect_ground_collition)


    


        