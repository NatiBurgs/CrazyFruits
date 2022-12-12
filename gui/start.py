import pygame,random
from constantes import *
from auxiliar import Auxiliar



class Movible_Start:
    def __init__(self,x,y,speed,frame_rate_ms,move_rate_ms):

        self.stay  = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Start/start.png",17,1)
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

        self.collition_rect = pygame.Rect(self.rect)

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = 5
        self.ground_collition_rect.y = y + 56
        
        self.collide_up = pygame.Rect(self.collition_rect)
        self.collide_up.height = 10
        self.collide_up.width = 30
        self.collide_up.x = self.rect.x
        self.collide_up.y = y

        self.direction = 1
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0

    def start(self):
        """
        Acción de estar ocioso. 

        Parámetro: None.
        Retorno: animacion.
        """
        self.animation = self.stay
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def change_x(self,delta_x):
        """
        Cambia el valor x del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_x
        Retorno: None
        """
        self.rect.x += delta_x
        self.collide_up.x += delta_x
        self.collition_rect.x += delta_x

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
        
    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.ground_collition_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)




