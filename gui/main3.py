import pygame, random
from pygame.locals import *
import sys
from constantes import *
from player import Player,Live
from plataforma import Plataform
from listaplataforma3 import plataform_list_3
from enemies import Enemy
from fruits import Fruits
from bullet import Bullet
from bluebird import Bird
from movible import Movible
from listafrutas import fruit_list_3
from trampas import Trampa
from start import Movible_Start



flags = DOUBLEBUF
#pygame.init()

#dibujo la pantalla
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("CRAZY FRUITS :D")
imagen_fondo = pygame.image.load("../Project2/recursos/Background/background3.png").convert_alpha()

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
explosion_sound = pygame.mixer.Sound("../Project2/recursos/assets_explosion.wav")

ambiente.play(100)    

   #cronometro
tiempo_juego = 60
tiempo_cronometro = int(pygame.time.get_ticks() / 1000)
tiempo_cronometro = str(tiempo_juego - tiempo_cronometro)
if tiempo_cronometro == 60:
    running = False
contador = fuente30.render("00:{0}".format(tiempo_cronometro),0,WHITE)
muestra_texto(screen,courier,(("Time: 00:{0}").format(str(tiempo_cronometro).zfill(2))),BLACK,25,45,5)    
clock = pygame.time.Clock()
FPS = 150

    #carga de sonidos 
    #establecer velocidad de fotogramas
    #player
player_list_3=[]
player_3 = Player(x=30,y=400,speed_walk=6,speed_run=12,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=1,interval_time_jump=300)
player_list_3.append(player_3)
    #enemies
enemy_list_3 = []

enemy_3_2 = Enemy(230,300,"Plant",11,11,5,5,5,8,1,1,10,1,0,0,0)
enemy_3_3 = Enemy(630,100,"Plant",11,11,5,5,5,8,1,1,10,1,0,0,0)
enemy_3_4 = Enemy(730,50,"Plant",11,11,5,5,5,8,1,1,10,1,0,0,0)

enemy_list_3.append(enemy_3_2)
enemy_list_3.append(enemy_3_3)
enemy_list_3.append(enemy_3_4)

bird_list_3 = []
bird_2 = Bird(30,250,5,5,0,0)
bird_list_3.append(bird_2)
    #plataformas
    #plataform movible
movible_list_3 = []
movible_1 = Movible(250,300,300,10,0,0,2)
movible_2 = Movible(250,200,480,10,0,0,2)
movible_3 = Movible(250,100,580,10,0,0,2)
movible_4 = Movible(500,300,790,480,0,0,2)
movible_5 = Movible(500,400,790,280,0,0,2)
movible_list_3.append(movible_1)
movible_list_3.append(movible_2)
movible_list_3.append(movible_3)
movible_list_3.append(movible_4)
movible_list_3.append(movible_5)
    #balas
bullet_list_3 = []
    #balas enemigas
bullet_enemy = []
    #start
start = Movible_Start(0,440,2,0,0)

    #vidas
live_list = []
live_1 = Live(x=435,y=5,width=30,height=30)
live_2 = Live(x=485,y=5,width=30,height=30)
live_3 = Live(x=535,y=5,width=30,height=30)
live_list.append(live_1)
live_list.append(live_2)
live_list.append(live_3)


tramp_list_3= []



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

    for plataforma in plataform_list_3:
        plataforma.draw(screen)

    for player in player_list_3:
        score_total = player.score
        high_score = fuente30.render("SCORE: {0}".format(score_total),0,WHITE)
        player.events(delta_ms,keys,bullet_list_3)
        player.update(delta_ms,plataform_list_3,enemy_list_3,bird_list_3,movible_list_3,live_list,tramp_list_3,screen,start,bullet_enemy)
        player.draw(screen)
        muestra_texto(screen,courier,str(player.score).zfill(7),WHITE,30,300,5)

    for enemy in enemy_list_3:
        enemy.movimiento_estatico(player_list_3)
        enemy.shoot(bullet_enemy,player_list_3)
        enemy.update(delta_ms,plataform_list_3,player_list_3,bullet_list_3)
        enemy.draw(screen)

    for bullet in bullet_list_3:
        if bullet.destroyer(enemy_list_3,bullet_list_3):
            bullet_list_3.remove(bullet)
            break
        bullet.update(delta_ms,enemy_list_3,bullet_list_3)
        bullet.draw(screen)

    for bird in bird_list_3:
            if bird.destroyer(player_list_3,bullet_list_3):
                bird_list_3.remove(bird)
                break
            bird.update(delta_ms,player_list_3,bullet_list_3)
            bird.draw(screen)
            
    for fruit in fruit_list_3:
        if fruit.animation == fruit.collected:
            fruit_list_3.remove(fruit)
            fruit.draw(screen)
        fruit.update(delta_ms,player_list_3)
        fruit.draw(screen)


    

    for bullet in bullet_enemy:
        if bullet.destroyer_player(bullet_enemy,player_list_3):
            bullet_enemy.remove(bullet)
            break
        bullet.update_bullet_enemy(delta_ms,player_list_3,bullet_enemy)
        bullet.draw(screen)

        
    for movible in movible_list_3:
        movible.update(delta_ms,player_list_3)
        movible.draw(screen)

    

    start.update(delta_ms)
    start.draw(screen)

    for live in live_list:
        live.update(screen)
    
    pygame.display.flip()
    