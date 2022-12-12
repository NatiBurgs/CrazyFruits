import pygame, random
from enemies import Enemy
from constantes import *
from auxiliar import Auxiliar
from player import Player


class Bird:
    '''
       Representa un ente enemigo murciélago. El cual posee una dirección de movimiento (horizontal o vertical), 
       Se elimina al hacer colisión con la parte inferior del player o con una bala generado por el player.

    '''


    def __init__(self,x,y,speed=2,gravity=8,frame_rate_ms=0,move_rate_ms=0) -> None:
       
        self.fly_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Bat/Flying.png",7,1)
        self.fly_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Bat/Flying.png",7,1,True)
       
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Bat/Hit.png",5,1)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Bat/Hit.png",5,1,True)
      
        self.frame = 0
        self.move_x = 0
        
        self.speed =  speed
        self.gravity = gravity
        self.animation = self.fly_r

        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
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


    def fly(self,direction):
        '''
        Acción de volar. 

        Parámetro: direction.
        Retorno: animación de volar.
        '''
        if(direction == 1):
            self.animation = self.fly_l
            self.move_x = self.speed_walk
        elif(direction == 0):
            self.animation = self.fly_r
            self.move_x = -self.speed_walk


    def hit(self,direction):
        '''
        Acción de pegar. 

        Parámetro: direction.
        Retorno: animación de golpear.
        '''
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
        los límites la pantalla de juego.

        Parámetro: None.
        Retorno: None.
        '''
        if(self.direction == 1):
            self.fly(self.direction)
            if (self.rect.x >=(ANCHO_VENTANA -20)):
                self.hit(self.direction)
                self.direction = 0
                
            
        elif(self.direction == 0):
            self.fly(self.direction)
            if(self.rect.x == 20):
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
        Genera el movimiento de la animacion dentro del juego,
        analizando si se encuentra sobre una plataforma, si está saltando.

        Parametros: delta_ms.
        Retorno: None.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
          
            self.change_x(self.move_x)

    def destroyer(self,player_list,bullet_list):
        '''
        Analiza si se realiza una colisión con el player o con la balas del player.


        Parámetros: player_list, bullet_list..
        Retorno: True, si colisiona con un player o una bala.
        '''
        retorno = False
        for bullet in bullet_list:
            if self.collition_rect.colliderect(bullet.collition_rect):
                if(self.direction == 1):
                    self.hit(self.direction)
                else:
                    self.hit(self.direction)
                retorno = True
        
        for player in player_list:
            if self.collition_rect.colliderect(player.ground_collition_rect):
                if(self.direction == 1):
                    self.hit(self.direction)
                else:
                    self.hit(self.direction)

                retorno = True
        return retorno


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
 
    def update(self,delta_ms,player_list,bullet_list):
        """
        Actualiza al Bird dentro del juego.

        Parámetro: delta_ms, player_list, bullet_list.
        Retorno: None.
        """
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.destroyer(player_list,bullet_list)
        self.movimiento_aleatorio()
        
    
    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            #pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(0,0,0),rect=self.collide_up)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

            


