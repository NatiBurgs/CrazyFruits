import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet
pygame.mixer.init()

class Live:
    '''
        Representa la vida del player. Posee una posición dentro de la pantalla del juego. 
        Cuando el player es destruido, se elimina la vida. 

    '''
    def __init__(self,x,y,width,height,type=0):
    
        self.image = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/heart.png",1,1)[type]
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.activa = True
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

    def update(self,screen):
        '''
            Actualización de la clase Live.

            Parámetro: screen.
            Retorno: None
        '''
        if self.activa == True:
            self.draw(screen)

    def draw(self,screen):
        '''
            Dibuja la clase Live dentro de la pantalla de juego.

            Parámetro: screen.
            Retorno: None 
        '''
        screen.blit(self.image,self.rect)




class Player:
    '''
        Representa al jugador que posee tres vidas. Éste puede realizar diferentes acciones: caminar, saltar, caer, ser golpeado,
        estar ocioso, ser destruido. 
        Comienza en una posición inicial al comienzo del juego, y cada vez que pierde una vida vuelve a esa
        posición inicial.
    
    '''
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
       
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Run.png",12,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Run.png",12,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Idle.png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Idle.png",11,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Jump.png",1,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Jump.png",1,1,True)
        self.fall = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Fall.png",1,1)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Hit.png",7,1)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Hit.png",7,1,True)
        self.wall_jump_r = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Jump.png",6,1) 
        self.wall_jump_l =  Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Pink/Jump.png",6,1,True)
        
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 0
        self.move_y = 0

        self.lives = 3
        self.hp = 100
        self.cadencia = 250
        self.ultimo_disparo = pygame.time.get_ticks()
        
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.posicion_inicial_x = x
        self.posicion_inicial_y = y
        self.player_destroyer = False
        
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.collition_rect.height = 10
        self.collition_rect.width = 30
        self.collition_rect.x = self.rect.x
        self.collition_rect.y = y 

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = 2
        self.ground_collition_rect.y = y + self.rect.height - 2
        
        self.saltar_efecto = pygame.mixer.Sound("../Project2/recursos/sonidos/saltar.wav")
        self.laser_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/assets_laser5.ogg")
        self.explosion_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/assets_explosion.wav")
        self.posicion_inicial_sound = pygame.mixer.Sound("../Project2/recursos/sonidos/pierdevida.wav")
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

    def barra_hp(self,screen,x,y):
        """
        Crea una barra de health point (hp) del player. La cual se mostrará en la parte superior izquierda del juego.
        Dicha barra disminuye -10 con los impactos de las balas de los enemigos.

        Parámetro: screen, x, y 
        Retorno: True si la barra es menor a 10
        """
        retorno = False
        largo = 200 
        ancho = 20 
        calculo_barra = int((self.hp /100) * largo)
        if calculo_barra < 10:
            retorno = True
        borde = pygame.Rect(x,y,largo,ancho)
        rectangulo = pygame.Rect( x,y,calculo_barra,ancho)
        pygame.draw.rect(screen,(176,196,222),rectangulo)#rojo
        pygame.draw.rect(screen,(0,0,255),borde,3)#azul
        
        
        warning = pygame.image.load("../Project2/recursos/50.png").convert_alpha()
        if self.hp < 0 :
            self.hp = 0
            
        if self.hp < 30:
            screen.blit(pygame.transform.scale(warning,(25,25)),(570,3))
        return retorno
    
    def posicion_inicio(self,x=0,y=400):
        """
        Devuelve al player a una posición de inicio

        Parámetro: x , y 
        Retorno: Player en una posición inicial, con la animación en stay()
        """
        self.lives -= 1 
         
        self.rect.x = x
        self.rect.y = y

        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.collition_rect.height = 10
        self.collition_rect.width = 30
        self.collition_rect.x = self.rect.x
        self.collition_rect.y = y 

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = 2
        self.ground_collition_rect.y = y + self.rect.height - 2
        self.stay()
        

    def shoot(self,bullet_list):
        """
        Acción de disparar del player.
        Los disparos se agregan a la bullet_list del juego.

        Parámetro: bullet_list
        Retorno: True, si dispara
        """
        retorno = False
        if(self.animation != self.hit_r and self.animation != self.hit_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.hit_r
                self.laser_sound.play()
                bullet = Bullet(self.rect.x+15,self.rect.y+15,"../Project2/recursos/bullet.png",0,0,5)
                bullet_list.append(bullet)
                retorno =  True
            else:
                self.animation = self.hit_l
                self.laser_sound.play()
                bullet = Bullet(self.rect.x+15,self.rect.y+15,"../Project2/recursos/bullet.png",0,0,-5)
                bullet_list.append(bullet)
                retorno =  True
            
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        return retorno
        
    def walk(self,direction):
        """
        Acción de caminar. 

        Parámetro: dirección del player.
        Retorno: animacion.
        """
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
    
    def hit(self,direction):
        """
        Acción de ser golpeado. 

        Parámetro: dirección del player.
        Retorno: animacion.
        """
        if(self.animation != self.hit_r and self.animation != self.hit_l):
            if(direction == DIRECTION_R):
                self.animation = self.hit_r
            else:
                self.animation = self.hit_l
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def jump(self,on_off = True):
        """
        Acción de saltar.

        Parámetro: on_off.
        Retorno: True, si está saltando, y una animacion.
        """
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                self.saltar_efecto.play()
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                self.saltar_efecto.play()
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        """
        Acción de estar ocioso. 

        Parámetro: None.
        Retorno: animacion.
        """
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
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
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        
    def change_y(self,delta_y):
        """
        Cambia el valor y del ente, según los movimientos dentro de la recta. 

        Parámetro: delta_y
        Retorno: None
        """
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list,movible_list,trampa_list,start):
        """
        Genera el movimiento de la animación dentro del juego,
        analizando si se encuentra sobre una plataforma, o si está saltando.

        Parametros: delta_ms, plataform_list, movible_list, trampa_list, start
        Retorno: None
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list,movible_list,trampa_list,start)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False

            

    def in_movible(self,movible_list,tramp_list):
        """
        Analiza si se encuentra sobre una plataforma movible (vertical u horizontal) o una trampa.
        Cambia el movimiento del player, mientras se encuentre sobre esos su posición será la misma.

        Parámetro: movible_list, tramp_list
        Retorno: True, si se encuentra sobre una plataforma o una trampa.
        """
        retorno = False
        for movible in movible_list:
                if(self.ground_collition_rect.colliderect(movible.collide_up)):
                    if movible.is_off:
                        self.delta_x = movible.move_x
                        self.change_x(self.delta_x) 
                        retorno = True

                    if movible.is_off_vertical:
                        self.delta_y = movible.move_y
                        self.change_y(self.delta_y) 
                        retorno = True
                        
        for tramp in tramp_list:
                if(self.ground_collition_rect.colliderect(tramp.collide_up)):
                    self.delta_x = tramp.move_x
                    self.change_x(self.delta_x)                 
                    retorno = True
        return retorno
            
    def destroyer(self,enemy_list,bird_list,tramp_list,bullet_enemy):
        """
        Analiza si se realiza una colisión con un enemigo o una trampa.
        Devolviendo al player en una posición inicial.


        Parámetros: enemy_list, bird_list, tramp_list, bullet_enemy.

        Retorno: True, si colisiona con un player con un enemigo, 
        o un player con una trampa.
        """
        retorno = False
        for bullet in bullet_enemy:
            if self.collition_rect.colliderect(bullet.collition_rect):
                self.explosion_sound.play()
                self.hp = self.hp -10

        for tramp in tramp_list:
            if self.collition_rect.colliderect(tramp.collition_rect):
                self.posicion_inicial_sound.play()
                self.posicion_inicio()
                retorno = True

        for enemy in enemy_list:
            for bird in bird_list:
                if self.collition_rect.colliderect(enemy.collition_rect) or self.collition_rect.colliderect(bird.collition_rect):
                    self.posicion_inicial_sound.play()
                    self.posicion_inicio()                                    
                    retorno = True
                                 
        return retorno

    def is_on_plataform(self,plataform_list,movible_list,trampa_list,start):
        """
        Analiza si se encuentra sobre una plataforma o una trampa.
        Cambia el movimiento del player, mientras se encuentre sobre esos su posición será la misma.

        Parámetro: plataform_list, movible_list, trampa_list, start
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
                    
            for movible in movible_list:
                if(self.ground_collition_rect.colliderect(movible.collide_up)):
                    retorno = True
                    break
            for trampa in trampa_list:
                if(self.ground_collition_rect.colliderect(trampa.collide_up)):
                    retorno = True
                    break

            if self.ground_collition_rect.colliderect(start.ground_collition_rect):
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
 
    def update(self,delta_ms,plataform_list,enemy_list,bird_list,movible_list,live_list,tramp_list,screen,start,bullet_enemy):
        """
        Actualiza al player dentro del juego.

        Parámetro: delta_ms, plataform_list, enemy_list, bird_list, 
                    movible_list, live_list, tramp_list, screen, start, bullet_enemy
        Retorno: None
        """
        self.do_movement(delta_ms,plataform_list,movible_list,tramp_list,start)
        self.do_animation(delta_ms)

        if self.destroyer(enemy_list,bird_list,tramp_list,bullet_enemy)==True:
            live_list.remove(live_list[0])

        self.in_movible(movible_list,tramp_list)
        self.barra_hp(screen,595,5)
        if self.barra_hp(screen,595,5)== True:
            for live in live_list:
                live_list.remove(live_list[0])

    def draw(self,screen):
        """
        Dibuja al ente dentro de la pantalla del juego.
        
        Parámetro: screen.
        Retorno: None
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def events(self,delta_ms,keys,bullet_list):
        '''
        Realiza las acciones del player en base a los eventos ocasionados por el teclado.

        Parámetro: delta_ms, keys, bullet_list.
        Retorno: None
        '''
        self.tiempo_transcurrido += delta_ms
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   
        if(keys[pygame.K_x]):
            ahora = pygame.time.get_ticks()
            if (ahora - self.ultimo_disparo) > self.cadencia: 
                self.shoot(bullet_list)
                self.ultimo_disparo = ahora                                                                                                                                                        
        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido




