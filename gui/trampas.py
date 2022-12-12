
import pygame, random
from enemies import Enemy
from constantes import *
from auxiliar import Auxiliar
from player import Player


class Trampa:
    '''
    Representa el objeto trampa del juego, los cuales se mueven horizontalmente con límites 
    pre establecidos. 
    '''
    def __init__(self,x,y,personaje,colum_idle,colum_hit,maximo_x,minimo_x,speed,gravity,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
       
        self.idle = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}/Blink.png".format(personaje),colum_idle,1)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}/righthit.png".format(personaje),colum_hit,1)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}/lefthit.png".format(personaje),colum_hit,1)
      
        self.frame = 0
        self.move_x = 0
        self.maximo_x= maximo_x
        self.minimo_x =minimo_x
        
        self.speed =  speed
        self.gravity = gravity
        self.animation = self.idle

        self.direction = 1# 0 for Right, 1 for Left
        self.speed_walk = 2

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.collition_rect.height = 30
        self.collition_rect.width = 30
        self.collition_rect.x = self.rect.x
        self.collition_rect.y = y 

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.collide_up = pygame.Rect(self.collition_rect)
        self.collide_up.height = 10
        self.collide_up.width = 30
        self.collide_up.x = self.rect.x
        self.collide_up.y = y

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0
        


    def stay(self,direction):
        """
        Acción de estar ocioso. 

        Parámetro: None.
        Retorno: animacion.
        """
        if(direction == 1):
            self.animation = self.idle
            self.move_x = self.speed
        elif(direction == 0):
            self.animation = self.idle
            self.move_x = -self.speed

    def hit(self,direction):
        """
        Acción de ser golpeado. 

        Parámetro: direction.
        Retorno: animacion.
        """
        if(direction == 1):
            self.animation = self.hit_r
        elif(direction == 0):
            self.animation = self.hit_l
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def movimiento_aleatorio(self):
        '''
        Movimiento horizontal aleatorio (der/izq) teniendo en cuenta
        el máx x y el min x.

        Parámetro: None.
        Retorno: None.
        '''
        if(self.direction == 1):
            self.stay(self.direction)
            if (self.rect.x ==self.maximo_x):
                self.hit(self.direction)
                self.direction = 0
        elif(self.direction == 0):
            self.stay(self.direction)
            if(self.rect.x == self.minimo_x):
                self.hit(self.direction)
                self.direction = 1

    def change_x(self,delta_x):
        """
        Cambia el valor x del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_x
        Retorno: None
        """
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.collide_up.x += delta_x

    def do_movement(self,delta_ms):
        """
        Genera el movimiento de la animación dentro del juego.

        Parametros: delta_ms.
        Retorno: None.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)

    def do_animation(self,delta_ms):
        """
        Genera la animacion del ente.

        Parámetro: delta_ms
        Retorno: animación en movimiento.
        """
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms):
        """
        Actualiza a la trampa en el de juego.

        Parámetro: delta_ms.
        Retorno: None
        """
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.movimiento_aleatorio()
        
    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(0,0,0),rect=self.collide_up)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)