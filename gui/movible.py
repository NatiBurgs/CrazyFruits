import pygame,random
from constantes import *
from auxiliar import Auxiliar



class Movible:
    def __init__(self,x,y,max_x,min_x,max_y,min_y,speed,frame_rate_ms=0,move_rate_ms=0):

        self.on = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Fan/On.png",4,1)
        self.off = Auxiliar.getSurfaceFromSpriteSheet("../Project2/recursos/Fan/Off.png",1,1)
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y

        self.animation = self.on
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

        self.collition_rect = pygame.Rect(self.rect)
        
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

    def move_on(self,direction):
        if(direction == 1):
            self.animation = self.on
            self.move_x = self.speed
        elif(direction == 0):
            self.animation = self.on
            self.move_x = -self.speed
    def move_off(self,direction):
        if(direction == 1):
            self.animation = self.off
            self.move_x = self.speed
            self.frame = 0
        elif(direction == 0):
            self.animation = self.off
            self.move_x = -self.speed
            self.frame = 0

    def move_on_vertical(self,direction):
        if(direction == 1):
            self.animation = self.on
            self.move_y = self.speed
        elif(direction == 0):
            self.animation = self.on
            self.move_y = -self.speed
    def move_off_vertical(self,direction):
        if(direction == 1):
            self.animation = self.off
            self.move_y = self.speed
            self.frame = 0
        elif(direction == 0):
            self.animation = self.off
            self.move_y = -self.speed
            self.frame = 0


        
    def movimiento_aleatorio(self):
        if(self.direction == 1):
            self.move_on(self.direction)
            if (self.rect.x >=(self.max_x -20)):
                self.move_off(self.direction)
                self.direction = 0
            
        elif(self.direction == 0):
            self.move_on(self.direction)
            if(self.rect.x == self.min_x):
                self.move_off(self.direction)
                self.direction = 1

    def is_off(self,player_list):
        retorno = False
        for player in player_list:
            if self.collide_up.colliderect(player.ground_collition_rect):
                self.move_off(self.direction)
            retorno = True
        return retorno
    
    def is_off_vertical(self,player_list):
        retorno = False
        for player in player_list:
            if self.collide_up.colliderect(player.ground_collition_rect):
                self.move_off_vertical(self.direction)
            retorno = True
        return retorno
    
    def movimiento_vertical(self):
        if(self.direction == 1):
            self.move_on_vertical(self.direction)
            if (self.rect.y >= self.max_y):
                self.move_off_vertical(self.direction)
                self.direction = 0          
        elif(self.direction == 0):
            self.move_on_vertical(self.direction)
            if(self.rect.y == self.min_y):
                self.move_off_vertical(self.direction)
                self.direction = 1

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collide_up.y += delta_y
        self.collition_rect.y += delta_y

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collide_up.x += delta_x
        self.collition_rect.x += delta_x

    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.change_x(self.move_x)

    def do_movement_vertical(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            
            self.change_y(self.move_y)
            


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
 
    def update(self,delta_ms,player_list):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.is_off(player_list)
        self.movimiento_aleatorio()
    
    def update_vertical(self,delta_ms,player_list):
        self.do_movement_vertical(delta_ms)
        self.do_animation(delta_ms)
        self.is_off_vertical(player_list)
        self.movimiento_vertical()
        
        
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collide_up)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)