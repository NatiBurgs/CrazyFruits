import pygame, random
from constantes import *
from auxiliar import Auxiliar
from player import Player
from bullet import Bullet

class Enemy:
    '''
    Representa al enemigo del juego. El mismo puede poseer movimientos estáticos o movimientos aleatorios.
    '''
    def __init__(self,x,y,personaje,colum_walk,colum_idle,colum_hit,colum_jump,colum_fall,colum_attack,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
       
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}/Run.png".format(personaje),colum_walk,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Run.png".format(personaje),colum_walk,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Idle.png".format(personaje),colum_idle,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Idle.png".format(personaje),colum_idle,1,True)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Hit.png".format(personaje),colum_hit,1)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Hit.png".format(personaje),colum_hit,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Jump.png".format(personaje),colum_jump,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Jump.png".format(personaje),colum_jump,1,True)
        self.fall = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Fall.png".format(personaje),colum_fall,1)
        self.fall = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Fall.png".format(personaje),colum_fall,1,True)
        self.attack_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Attack.png".format(personaje),colum_attack,1,True)
        self.attack_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/{0}\\Attack.png".format(personaje),colum_attack,1)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.orientacion = 0

        self.cadencia = 250
        self.ultimo_disparo = pygame.time.get_ticks()

        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r

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

        self.laser_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/assets_laser5.ogg")
        self.explosion_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/assets_explosion.wav")
              
        self.is_jump = False
        self.is_fall = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump


    def walk(self,direction):
        '''
        Acción de caminar.

        Parámetro: direction.
        Retorno: None.
        '''
        if(direction == 1):
            self.animation = self.walk_l
            self.move_x = self.speed_walk
        elif(direction == 0):
            self.animation = self.walk_r
            self.move_x = -self.speed_walk

    def hit(self,direction):
        '''
        Acción pegar.

        Parámetro: direction.
        Retorno: None.
        '''
        if(direction == 1):
            self.animation = self.hit_r
        elif(direction == 0):
            self.animation = self.hit_l
        self.move_x = 0
        self.move_y = 0
        self.frame = 0        

    def jump(self,on_off = True):
        '''
        Acción saltar.

        Parámetro: on_off.
        Retorno: True si está saltando.
        '''
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        '''
        Acción estar ocioso.

        Parámetro: None.
        Retorno: None.
        '''
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def movimiento_estatico(self,player_list):
        '''
        Genera un movimiento estático al enemigo, cambiando de dirección
        según la posición del player.

        Parámetro: player_list.
        Retorno: None.
        '''
        for player in player_list:    
            if self.rect.x <= player.rect.x:
                self.orientacion = 1
                self.animation = self.stay_l
            elif self.rect.x > player.rect.x:
                self.orientacion = 0
                self.animation = self.stay_r
        
    def movimiento_aleatorio(self):
        '''
        Movimiento horizontal aleatorio (der/izq) teniendo en cuenta
        los límites la pantalla de juego.

        Parámetro: None.
        Retorno: None.
        '''
        if(self.direction == 1):
            self.walk(self.direction)
            if (self.rect.x >=(ANCHO_VENTANA -20)):
                self.hit(self.direction)
                self.direction = 0
            
        elif(self.direction == 0):
            self.walk(self.direction)
            if(self.rect.x == 60):
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
        
    def change_y(self,delta_y):
        """
        Cambia el valor y del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_y
        Retorno: None
        """
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.collide_up.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        """
        Genera el movimiento de la animación dentro del juego,
        analizando si se encuentra sobre una plataforma, o si está saltando.

        Parametros: delta_ms, plataform_list
        Retorno: None.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False
        
    def is_on_plataform(self,plataform_list):
        """
        Analiza si se encuentra sobre una plataforma o una trampa.
        Cambia el movimiento del enemigo, mientras se encuentre sobre esos su posición será la misma.

        Parámetro: plataform_list.
        Retorno: True, si se encuentra sobre una plataforma o una trampa.
        """
        retorno = False
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break       
        return retorno
    
    def shoot(self,bullet_enemy,player_list):
        '''
        Acción de disparar. 
        El enemigo dispara si se encuentran en el mismo valor de y ambos. 

        Parámetros: bullet_enemy, player_list.
        Retorno: True, si dispara.
        '''
        retorno = False
        for player in player_list:
            if self.collition_rect.y == player.collition_rect.y:
                ahora = pygame.time.get_ticks()
                if self.orientacion == 1:
                    self.animation = self.attack_l
                    if (ahora - self.ultimo_disparo) > self.cadencia: 
                        self.laser_sound.play()
                        bullet = Bullet(self.rect.x+15,self.rect.y+15,"C:\\Users\\rocio\\Desktop\\Project2\\recursos\\Plant\\Bullet.png",0,0,3)
                        bullet_enemy.append(bullet)
                        self.ultimo_disparo = ahora   
                else:
                    self.animation = self.attack_r
                    if (ahora - self.ultimo_disparo) > self.cadencia:
                        self.laser_sound.play()
                        bullet = Bullet(self.rect.x+15,self.rect.y+15,"C:\\Users\\rocio\\Desktop\\Project2\\recursos\\Plant\\Bullet.png",0,0,-3)
                        bullet_enemy.append(bullet)
                        self.ultimo_disparo = ahora
                self.move_x = 0
                self.move_y = 0
                self.frame = 0
                retorno= True
        return retorno
                 
    def destroyer(self,player_list,bullet_list):
        """
        Analiza si se realiza una colisión con un player o una bala de éste.
        
        Parámetros: player_list, bullet_list.
        Retorno: True, si colisiona con la parte inferior del player o
        con una bala del mismo.
        """
        retorno = False
        for player in player_list:
            for bullet in bullet_list:
                if self.collition_rect.colliderect(bullet.collition_rect):
                    if(self.direction == 1):
                        self.hit(self.direction)
                        self.explosion_sound.play()
                    else:
                        self.hit(self.direction)
                    player.score = player.score + 30
                    retorno = True
        
        for player in player_list:
            if self.collide_up.colliderect(player.ground_collition_rect):
                if(self.direction == 1):
                    self.hit(self.direction)
                else:
                    self.hit(self.direction)
                player.score = player.score + 50
                retorno = True
        return retorno

    def do_animation(self,delta_ms):
        """
        Genera la animación del ente.

        Parámetro: delta_ms.
        Retorno: animación en movimiento.
        """
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self,delta_ms,plataform_list,player_list,bullet_list):
        """
        Actualiza al ente dentro del juego.

        Parámetro: delta_ms, plataform_list, player_list, bullet_list.
        Retorno: None.
        """
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.destroyer(player_list,bullet_list)
            
    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            #pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            #pygame.draw.rect(screen,color=(0,0,0),rect=self.collide_up)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)