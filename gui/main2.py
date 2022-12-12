import pygame, random
from pygame.locals import *
import sys
from constantes import *
from player import Player,Live
from plataforma import Plataform
from listaplataformas import plataform_list_2
from enemies import Enemy
from fruits import Fruits
from bullet import Bullet
from bluebird import Bird
from movible import Movible
from listafrutas import fruit_list_2
from trampas import Trampa
from start import Movible_Start


flags = DOUBLEBUF
#pygame.init()

#dibujo la pantalla
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("CRAZY FRUITS :D")
imagen_fondo = pygame.image.load("../Project2/recursos/Background/background4.png").convert_alpha()

#sonidos
ambiente = pygame.mixer.Sound("../Project2/recursos/sonidos/tambor.mp3")
ambiente.play(100)


fuente30 = pygame.font.SysFont("Arial",30,True,False)
courier = pygame.font.match_font("courier") 
def muestra_texto(screen,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,False,color)
    rect_text = superficie.get_rect()
    rect_text.x = x
    rect_text.y = y
    screen.blit(superficie,rect_text)

#creacion de vidas
live_list = []
live_1 = Live(x=435,y=5,width=30,height=30)
live_2 = Live(x=485,y=5,width=30,height=30)
live_3 = Live(x=535,y=5,width=30,height=30)
live_list.append(live_1)
live_list.append(live_2)
live_list.append(live_3)
#score
score_total = 0
#cronometro
tiempo_juego = 60
tiempo_cronometro = int(pygame.time.get_ticks() / 1000)
tiempo_cronometro = str(tiempo_juego - tiempo_cronometro)
if tiempo_cronometro == 60:
    running = False
contador = fuente30.render("00:{0}".format(tiempo_cronometro),0,WHITE)
muestra_texto(screen,courier,(("Time: 00:{0}").format(str(tiempo_cronometro).zfill(2))),BLACK,25,45,5)

#plataform movible
movible_list_2 = []
movible_2 = Movible(150,110,450,150,450,150,2,0,0)
movible_3 = Movible(50,110,450,150,450,150,2,0,0)
movible_list_2.append(movible_2)
movible_list_2.append(movible_3)

start = Movible_Start(0,440,1,0,0)

#establecer velocidad de fotogramas
clock = pygame.time.Clock()
FPS = 150

#creacion de pajaros
bird_list_2 = []
#creacion de movables

#crecioni de start 
start = Movible_Start(0,440,2,0,0)
#creacion del jugador
player_list_2 = []
player_2 = Player(x=30,y=400,speed_walk=6,speed_run=12,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=1,interval_time_jump=300)
player_list_2.append(player_2)
#creacion de enemigo
enemy_list_2 = []
enemy_2_1 = Enemy(600,350,"Plant",11,11,5,5,5,8,1,1,10,1,0,0,0)
enemy_2_3 = Enemy(200,200,"Plant",11,11,5,5,5,8,1,1,10,1,0,0,0)
enemy_list_2.append(enemy_2_1)
enemy_list_2.append(enemy_2_3)

rino_list = []
rino_1 = Enemy(500,400,"Rino",6,11,5,5,4,5,2,2,8,0,0,0,0)
rino_list.append(rino_1)

#crecion de scrore
score_total = 0
#creacion de trampas
tramp_list_2 =[]
tramp_1 = Trampa(300,140,"SpikeHead",4,4,400,180,2,0,0,0)
tramp_list_2.append(tramp_1)
#creacion de bullets
bullet_list_2 = []
bullet_enemy = []

while True:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    delta_ms = clock.tick(FPS)

    tiempo_cronometro = int(pygame.time.get_ticks() / 1000)
    tiempo_cronometro = str(tiempo_juego - tiempo_cronometro)
    if tiempo_cronometro == 60:
        running = False
    contador = fuente30.render("00:{0}".format(tiempo_cronometro),0,WHITE)
    muestra_texto(screen,courier,(("Time: 00:{0}").format(str(tiempo_cronometro).zfill(2))),WHITE,25,45,5)


    for plataforma in plataform_list_2:
        plataforma.draw(screen)

    
    for player in player_list_2:
        score_total = player.score
        high_score = fuente30.render("SCORE: {0}".format(score_total),0,WHITE)
        player.events(delta_ms,keys,bullet_list_2)
        player.update(delta_ms,plataform_list_2,enemy_list_2,bird_list_2,movible_list_2,live_list,tramp_list_2,screen,start,bullet_enemy)
        player.draw(screen)
        muestra_texto(screen,courier,str(player.score).zfill(7),WHITE,30,300,5)

    for enemy in enemy_list_2:
            enemy.movimiento_estatico(player_list_2)
            enemy.shoot(bullet_enemy,player_list_2)
            enemy.update(delta_ms,plataform_list_2,player_list_2,bullet_list_2)
            enemy.draw(screen)
            
    for bullet in bullet_list_2:
        if bullet.destroyer(player_list_2,bullet_list_2):#para el player 
            bullet_list_2.remove(bullet)
            break
        bullet.update(delta_ms,player_list_2,bullet_list_2)
        bullet.draw(screen)

    for live in live_list:
        live.update(screen)

    for movible in movible_list_2:
        movible.update_vertical(delta_ms,player_list_2)
        movible.draw(screen)
                                                            
    for fruit in fruit_list_2:
        if fruit.animation == fruit.collected:
            fruit_list_2.remove(fruit)
            fruit.draw(screen)
        fruit.update(delta_ms,player_list_2)
        fruit.draw(screen)

    for bullet in bullet_enemy:
        if bullet.destroyer_player(bullet_enemy,player_list_2):#para el enemugo
            bullet_enemy.remove(bullet)
            break
        bullet.update_bullet_enemy(delta_ms,player_list_2,bullet_enemy)
        bullet.draw(screen)

    for tramp in tramp_list_2:
        tramp.update(delta_ms)
        tramp.draw(screen)

    start.update(delta_ms)
    start.draw(screen)

    pygame.display.flip()