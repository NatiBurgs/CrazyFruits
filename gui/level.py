import pygame, random, time
from pygame.locals import *
import sys
from constantes import *
from player import Player,Live
from plataforma import Plataform
from listaplataformas import plataform_list
from enemies import Enemy
from fruits import Fruits
from bullet import Bullet
from bluebird import Bird
from movible import Movible
from listafrutas import fruit_list
from trampas import Trampa
from start import Movible_Start
from auxiliar import Auxiliar
from sql_data import *

pygame.mixer.init()

#######################################################################################################################################
class Level:
    '''
    Representa un nivel del juego.
    '''
    def __init__(self,screen,nivel):

        self.hs = 0
        self.lives = 3
        self.tiempo_cronometro=0
        self.tiempo_transcurrido =0
        self.game_lose = False
        self.game_win = False
        self.game_reset=False
        self.active = False

        self.nivel_num = nivel
        nivel_todos= Auxiliar.lector_json("./../project2/gui/Niveles.json")
        nivel_data=nivel_todos[nivel]
        
        self.fuente30 = pygame.font.SysFont("Arial",30,True,False)
        self.courier = pygame.font.match_font("courier") 

        self.imagen_fondo = pygame.image.load(nivel_data["imagen_fondo"]).convert_alpha()
        self.screen = screen
    
        self.player_data= nivel_data["player"]
        self.enemy_data= nivel_data["enemy_list"]
        self.plataform_data = nivel_data["platform_list"]
        self.movible_data= nivel_data["movible_list"]
        self.bird_data= nivel_data["bird_list"]
        self.live_data= nivel_data["live_list"]
        self.tramp_data= nivel_data["tramp_list"]
        self.bullet_data= nivel_data["bullet_list"]
        self.bullet_enemy_data= nivel_data["bullet_enemy_list"]
        self.fruit_data= nivel_data["fruit_list"]

        self.imagen_fondo = pygame.image.load(nivel_data["imagen_fondo"])
        
        self.player_list = []
        for n in range(len(self.player_data)):
            self.player_list.append(Player(x=self.player_data[n]["x"],y=self.player_data[n]["y"],speed_walk=self.player_data[n]["speed_walk"],speed_run=self.player_data[n]["speed_run"],gravity=self.player_data[n]["gravity"],jump_power=self.player_data[n]["jump_power"],frame_rate_ms=100,
            move_rate_ms=50,jump_height=self.player_data[n]["jump_height"],p_scale=self.player_data[n]["p_scale"],interval_time_jump= self.player_data[n]["interval_time_jump"]
            ))

        self.enemy_list =[]
        for n in range(len(self.enemy_data)):
            self.enemy_list.append(Enemy(x=self.enemy_data[n]["x"],y=self.enemy_data[n]["y"],personaje=self.enemy_data[n]["personaje"],colum_walk=self.enemy_data[n]["colum_walk"],
                colum_idle=self.enemy_data[n]["colum_idle"],colum_hit=self.enemy_data[n]["colum_hit"],colum_jump=self.enemy_data[n]["colum_jump"],
                colum_fall=self.enemy_data[n]["colum_fall"],colum_attack=self.enemy_data[n]["colum_attack"],speed_walk=self.enemy_data[n]["speed_walk"],
                speed_run=self.enemy_data[n]["speed_run"],gravity= self.enemy_data[n]["gravity"],jump_power=self.enemy_data[n]["jump_power"],
                frame_rate_ms=self.enemy_data[n]["frame_rate_ms"],move_rate_ms=self.enemy_data[n]["move_rate_ms"],jump_height=self.enemy_data[n]["jump_height"],
                p_scale=1,interval_time_jump=100))

        self.platform_list = []
        for n in range(len(self.plataform_data)):
            self.platform_list.append(Plataform(x=self.plataform_data[n]["x"],y=self.plataform_data[n]["y"],width=self.plataform_data[n]["width"],
            height=self.plataform_data[n]["height"],type=self.plataform_data[n]["type"]))

        self.movible_list = []
        for n in range(len(self.movible_data)):
            self.movible_list.append(Movible(x=self.movible_data[n]["x"],y=self.movible_data[n]["y"],max_x=self.movible_data[n]["max_x"],
                min_x=self.movible_data[n]["min_x"],max_y=self.movible_data[n]["max_y"],min_y=self.movible_data[n]["min_y"],speed=self.movible_data[n]["speed"]))
        
        self.bird_list = []
        for n in range(len(self.bird_data)):
            self.bird_list.append(Bird(x=self.bird_data[n]["x"],y=self.bird_data[n]["y"]))

        self.live_list = []
        for n in range(len(self.live_data)):
            self.live_list.append(Live(x=self.live_data[n]["x"],y=self.live_data[n]["y"],width=self.live_data[n]["width"],height=self.live_data[n]["height"],))

        self.tramp_list = []
        for n in range(len(self.tramp_data)):
            self.tramp_list.append(Trampa(x=self.tramp_data[n]["x"],y=self.tramp_data[n]["y"],personaje=self.tramp_data[n]["personaje"],
                colum_idle=self.tramp_data[n]["colum_idle"],colum_hit=self.tramp_data[n]["colum_hit"],maximo_x=self.tramp_data[n]["maximo_x"],
                minimo_x=self.tramp_data[n]["minimo_x"],speed=self.tramp_data[n]["speed"],gravity=self.tramp_data[n]["gravity"],
                frame_rate_ms=self.tramp_data[n]["frame_rate_ms"],move_rate_ms=self.tramp_data[n]["move_rate_ms"]))
            
        self.bullet_enemy_list = []
        self.bullet_list = []

        self.fruit_list=[]
        for n in range(len(self.fruit_data)):
            self.fruit_list.append(Fruits(x=self.fruit_data[n]["x"],y=self.fruit_data[n]["y"]))
        
        self.start = Movible_Start(0,440,2,0,0)
        
            
    def run_level(self,delta_ms,lista_eventos,keys):
        for event in lista_eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())

        #self.tiempo_cronometro = int(pygame.time.get_ticks() / 1000)
        self.tiempo_transcurrido += (delta_ms)
        self.tiempo_cronometro = int(self.tiempo_transcurrido/1000)

        if self.tiempo_cronometro == 60:
            self.game_lose = True
            

        self.tiempo_cronometro_str = str(self.tiempo_cronometro)
        self.contador = self.fuente30.render("00:{0}".format(self.tiempo_cronometro),0,WHITE)
        Auxiliar.muestra_texto(self.screen,self.courier,(("Time: 00:{0}").format(str(self.tiempo_cronometro_str).zfill(2))),WHITE,25,45,5)
        
        self.hs_texto = self.fuente30.render("SCORE: {0}".format(self.hs),0,WHITE)
        Auxiliar.muestra_texto(self.screen,self.courier,str(self.hs).zfill(7),WHITE,30,300,5)

        

        for plataforma in self.platform_list:
            plataforma.draw(self.screen)

        for player in self.player_list:
            if player.lives == 0:
                self.game_lose=True
                
            if player.hp == 0:
                self.game_lose = True
                
            player.events(delta_ms,keys,self.bullet_list)
            player.update(delta_ms,self.platform_list,self.enemy_list,self.bird_list,self.movible_list,self.live_list,self.tramp_list,self.screen,self.start,self.bullet_enemy_list)
            player.draw(self.screen)
            
            
        for bullet in self.bullet_list:
            if bullet.destroyer(self.enemy_list,self.bullet_list):
                self.bullet_list.remove(bullet)
                break
            bullet.update(delta_ms,self.enemy_list,self.bullet_list)
            bullet.draw(self.screen)


        for enemy in self.enemy_list:
            if self.nivel_num=="Nivel_1":
                if enemy.destroyer(self.player_list,self.bullet_list):
                    self.hs = self.hs + 100
                    self.enemy_list.remove(enemy)
                    break
                enemy.movimiento_aleatorio()
                enemy.update(delta_ms,self.platform_list,self.player_list,self.bullet_list)
                enemy.draw(self.screen)        
                    
            else:
                enemy.movimiento_estatico(self.player_list)
                enemy.shoot(self.bullet_enemy_list,self.player_list)
                enemy.update(delta_ms,self.platform_list,self.player_list,self.bullet_list)
                enemy.draw(self.screen)
            
                
        for bird in self.bird_list:
            if bird.destroyer(self.player_list,self.bullet_list):
                self.hs = self.hs + 100
                self.bird_list.remove(bird)
                break
            bird.update(delta_ms,self.player_list,self.bullet_list)
            bird.draw(self.screen)

                    
        for fruit in self.fruit_list:
            fruit.update(delta_ms,self.player_list)
            fruit.draw(self.screen)
            if fruit.flag_collition:
                self.hs = self.hs + 50
                self.fruit_list.remove(fruit)
            if len(self.fruit_list) == 0:
                self.game_win = True
                

        for bullet in self.bullet_enemy_list:
            if bullet.destroyer_player(self.bullet_enemy_list,self.player_list):
                self.hs = self.hs - 10
                
                self.bullet_enemy_list.remove(bullet)
                break
            bullet.update_bullet_enemy(delta_ms,self.player_list,self.bullet_enemy_list)
            bullet.draw(self.screen)
                    
        for movible in self.movible_list:
            if self.nivel_num=="Nivel_2":
                movible.update_vertical(delta_ms,self.player_list)
                movible.draw(self.screen)
            else:
                movible.update(delta_ms,self.player_list)
                movible.draw(self.screen)
                
        for live in self.live_list:
            live.update(self.screen)
         
        for n in range(len(self.live_list)):
            if len(self.live_list)==0:
                self.game_lose==True

        for tramp in self.tramp_list:
            tramp.update(delta_ms)
            tramp.draw(self.screen)

        self.start.update(delta_ms)
        self.start.draw(self.screen)

        
        
        pygame.display.flip()

          
    
        

        
        
    

            
        


        