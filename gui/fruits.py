import pygame, random
from constantes import *
from auxiliar import Auxiliar
from player import Player

pygame.mixer.init()
Banana = "../Project2/recursos/Fruits/Bananas.png"
class Fruits():
    def __init__(self,x,y,frame_rate_ms=0,move_rate_ms=0,path_fruit =Banana,p_scale=1):
       
    
        self.stay= Auxiliar.getSurfaceFromSpriteSheet(path_fruit,17,1,True)
        self.collected = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Fruits/Collected.png",4,1,True)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
       
        self.animation = self.stay
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flag_collition= False

        self.collition_rect = pygame.Rect(self.rect)
        self.collition_rect.height = 30
        self.collition_rect.width = 30
        self.collition_rect.x = self.rect.x
        self.collition_rect.y = y

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

                
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
    
        self.collected_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/recolecta.wav")
    
    def is_collected(self):
        '''
        Animación de ser recolectado. 

        Parámetro: None.
        Retorno: True.
        '''
        self.flag_collition = True
        self.collected_sound.play()
        self.animation = self.collected
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        
        
    def is_stay(self):
        '''
        Animación de estar ocioso. 

        Parámetro: None.
        Retorno: True.
        '''
        if(self.direction == DIRECTION_R):
            self.animation = self.stay
        else:                
            self.animation = self.stay
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def do_movement(self,delta_ms,player_list):
        """
        Genera el movimiento de la animación dentro del juego,
        analizando si se recolecta por el player.

        Parametros: delta_ms, player_list
        Retorno: None.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
        
            for player in player_list:
                if(self.collition_rect.colliderect(player.collition_rect) or self.collition_rect.colliderect(player.ground_collition_rect)):
                    self.is_collected()
                    #player.score = player.score + 10

    def do_animation(self,delta_ms):
        """
        Genera la animación del ente.

        Parámetro: delta_ms.
        Retorno: None.
        """
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self,delta_ms,player_list):
        """
        Actualiza al ente dentro del juego.

        Parámetro: delta_ms, player_list.
        Retorno: None.
        """
        self.do_movement(delta_ms,player_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)




        
    

