import pygame
from constantes import *
from auxiliar import Auxiliar


class Bullet():
    '''
        Representa a las balas que se generan por los disparos del player o del enemigo.
    '''
    def __init__(self, x, y,path_bullet,frame_rate_ms,move_rate_ms,speed_x):

        self.bullet_image = Auxiliar.getSurfaceFromSpriteSheet(path_bullet,1,1)
        self.frame = 0
        self.animation = self.bullet_image
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x

        self.move_x = 0
        self.move_y = 0

        self.collition_rect = pygame.Rect(self.rect)

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        self.speed_x = speed_x
        self.rect.centerx = x
    
    def collide_enemy(self,enemy_list):
        '''
        Retorna True si se realiza una colisión con un enemigo.

        Parámetro: enemy_list. 
        Retorno: True o False.
        '''
        retorno = False
        for enemy in enemy_list:
            if self.collition_rect.colliderect(enemy.collition_rect):
                retorno = True
        return retorno
    
    def collide_pantalla(self):
        '''
        Retorna True si la posición en el eje x de la bala sobrepasa los límites de
        la pantalla.

        Parámetro: None.
        Retorno: True o False.
        '''
        retorno = False
        if (self.rect.x >=(ANCHO_VENTANA -10) or self.rect.x == 10):
            retorno = True
        return retorno

    def is_bullet(self,direction):
        '''
        Acción de movimiento de la bala en el eje x, dependiendo de la dirección.

        Parámetro: direction.
        Retorno: None.
        '''
        if(direction == 1):
            self.animation = self.bullet_image
            self.move_x = self.speed_x
        elif(direction == 0):
            self.animation = self.bullet_image
            self.move_x = -self.speed_x

    def destroyer(self,enemy_list,bullet_list):
        """
        Analiza si se realiza una colisión con un enemigo o
        los límites de la pantalla.

        Parámetros: enemy_list, bullet_list.
        Retorno: True, si colisiona con un enemigo.
        """
        retorno = False
        for bullet in bullet_list:
            for enemy in enemy_list:
                if (self.rect.x >=(ANCHO_VENTANA -10) or self.rect.x == 10) or (self.collition_rect.colliderect(enemy.collition_rect)):
                    retorno = True
        return retorno
    
    def destroyer_player(self,bullet_list,player_list):
        '''
        Retorna True si se realiza una colisión con un player o 
        los límites de la pantalla.

        Parámetro: player_list, bullet_list. 
        Retorno: True o False.
        '''
        retorno = False
        for bullet in bullet_list:
            for player in player_list:
                if (self.rect.x >=(ANCHO_VENTANA -10) or self.rect.x == 10) or (self.collition_rect.colliderect(player.collition_rect)):
                    retorno = True
        return retorno

    def change_x(self,delta_x):
        """
        Cambia el valor x del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_x
        Retorno: None
        """
        self.rect.x += delta_x 
        self.collition_rect.x += (delta_x + self.speed_x)
        
    def change_y(self,delta_y):
        """
        Cambia el valor y del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_y
        Retorno: None
        """
        self.rect.y += delta_y
        self.collition_rect.y += delta_y

    def do_animation(self,delta_ms):
        """
        Genera la animación del ente.

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
            self.change_y(self.move_y)


    def update(self,delta_ms,enemy_list,bullet_list):
        """
        Actualiza el objeto bala del player dentro del juego.

        Parámetro: delta_ms, enemy_list, bullet_list.
        Retorno: None
        """
        self.rect.x += self.speed_x
        self.do_animation(delta_ms)
        self.do_movement(delta_ms)
        self.is_bullet(self.direction)
        self.destroyer(enemy_list,bullet_list)

    def update_bullet_enemy(self,delta_ms,player_list,bullet_list):
        """
        Actualiza el objeto bala del enemigo dentro del juego.

        Parámetro: delta_ms, player_list, bullet_list.
        Retorno: None.
        """
        self.rect.x += self.speed_x
        self.do_animation(delta_ms)
        self.do_movement(delta_ms)
        self.is_bullet(self.direction)
        self.destroyer_player(player_list,bullet_list)

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