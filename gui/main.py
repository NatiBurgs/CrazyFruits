import pygame, random
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



BLACK = (0,0,0)
WHITE = (255,255,255)

DIRECTION_L = 0
DIRECTION_R = 1

flags = DOUBLEBUF

#pygame.init()

#dibujo la pantalla
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("CRAZY FRUITS :D")
imagen_fondo = pygame.image.load("./../project2/recursos/Background/background4.png").convert_alpha()

#sistema de puntuaciones
fuente30 = pygame.font.SysFont("Arial",30,True,False)
courier = pygame.font.match_font("courier") 

def muestra_texto(screen,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,False,color)
    rect_text = superficie.get_rect()
    rect_text.x = x
    rect_text.y = y
    screen.blit(superficie,rect_text)


#carga de sonidos 
pygame.mixer.init()
ambiente = pygame.mixer.Sound("../Project2/recursos/sonidos/tambor.mp3")
laser_sound = pygame.mixer.Sound("../Project2/recursos/assets_laser5.ogg")
recoleccion = pygame.mixer.Sound("../Project2/recursos/sonidos/recolecta.wav")


clock = pygame.time.Clock()

FPS = 150

#plataform movible
movible_list = []
movible_1 = Movible(100,150,790,20,790,20,2,50,25)
movible_list.append(movible_1)
start = Movible_Start(0,440,2,0,0)

#creacion del jugador
player_list=[]
player_1 = Player(x=30,y=400,speed_walk=6,speed_run=12,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=1,interval_time_jump=300)
player_list.append(player_1)

#creacion de enemigo
enemy_list = []
enemy_1 = Enemy(500,350,"Bunny",12,8,5,1,1,1,3,3,10,0,0,0,0)
enemy_2 = Enemy(50,270,"Bunny",12,8,5,1,1,1,3,3,10,0,0,0,0)
enemy_3 = Enemy(760,150,"Bunny",12,8,5,1,1,1,3,3,10,0,0,0,0)

enemy_list.append(enemy_1)
enemy_list.append(enemy_2)
enemy_list.append(enemy_3)

bird_list = []
bird_1 = Bird(400,100,2,5,0,0)
bird_2 = Bird(30,50,5,5,0,0)
bird_list.append(bird_1)
bird_list.append(bird_2)


#creacion de vidas
live_list = []
live_1 = Live(x=435,y=5,width=30,height=30)
live_2 = Live(x=485,y=5,width=30,height=30)
live_3 = Live(x=535,y=5,width=30,height=30)
live_list.append(live_1)
live_list.append(live_2)
live_list.append(live_3)

#crecion de scrore
score_total = 0
#creacion de trampas
tramp_list = []
tramp_1 = Trampa(5,265,"RockHead",4,4,205,10,1,8,0,0)
tramp_2 = Trampa(500,265,"RockHead",4,4,770,550,1,8,0,0)
tramp_list.append(tramp_1)
tramp_list.append(tramp_2)

bullet_list = []
bullet_enemy = []

running =True
while running:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    delta_ms = clock.tick(FPS)

    tiempo_juego = 60
    tiempo_cronometro = int(pygame.time.get_ticks() / 1000)
    tiempo_cronometro = str(tiempo_juego - tiempo_cronometro)
    
    contador = fuente30.render("00:{0}".format(tiempo_cronometro),0,WHITE)
    muestra_texto(screen,courier,(("Time: 00:{0}").format(str(tiempo_cronometro).zfill(2))),BLACK,25,45,5)

    
    for plataforma in plataform_list:
        plataforma.draw(screen)

    for player in player_list:
        score_total = player.score
        high_score = fuente30.render("SCORE: {0}".format(score_total),0,WHITE)
        player.events(delta_ms,keys,bullet_list)
        player.update(delta_ms,plataform_list,enemy_list,bird_list,movible_list,live_list,tramp_list,screen,start,bullet_enemy)
        player.draw(screen)
        muestra_texto(screen,courier,str(player.score).zfill(7),BLACK,30,300,5)
        
    for enemy in enemy_list:
        if enemy.destroyer(player_list,bullet_list):
            enemy_list.remove(enemy)
            break
        enemy.movimiento_aleatorio()
        enemy.update(delta_ms,plataform_list,player_list,bullet_list)
        enemy.draw(screen)
 
    for bullet in bullet_list:
        if bullet.destroyer(enemy_list,bullet_list):
            bullet_list.remove(bullet)
            break
        bullet.update(delta_ms,enemy_list,bullet_list)
        bullet.draw(screen)
        
 
    for bird in bird_list:
        if bird.destroyer(player_list,bullet_list):
            bird_list.remove(bird)
            break
        bird.update(delta_ms,player_list,bullet_list)
        bird.draw(screen)

        
    for fruit in fruit_list:
        if fruit.animation == fruit.collected:
            fruit_list.remove(fruit)
            fruit.draw(screen)
        fruit.update(delta_ms,player_list)
        fruit.draw(screen)
        
    for movible in movible_list:
        movible.update(delta_ms,player_list)
        movible.draw(screen)
    
    for live in live_list:
        live.update(screen)
        

    for tramp in tramp_list:
        tramp.update(delta_ms)
        tramp.draw(screen)

    start.update(delta_ms)
    start.draw(screen)


    
   


    pygame.display.flip()
    




    


  



