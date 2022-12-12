import pygame
from pygame.locals import *
import sys
from gui_form_menu_A import Settings
from gui_form_menu_B import MenuPrincipal
from gui_select_level import SelectLevel
from gui_pausa import Pause
from gui_ranking import Ranking
from gui_constantes import *
from gui_game import Nivel
from gui_win import Win
from gui_lose import Lose
from sql_data import *
from gui_nivel import Nivel

FPS=150
flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()


loser= Lose(name="lose",master_surface= screen, x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
win = Win(name="win",master_surface= screen, x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
ranking = Ranking(name="ranking",master_surface= screen, x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
pause_game = Pause(name="pause",master_surface= screen, x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
selec_level = SelectLevel(name="select_level",master_surface= screen, x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
menu_principal = MenuPrincipal(name="menu_principal",master_surface = screen,x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=True)
settings = Settings(name="setting",master_surface = screen,x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)

form_nivel_1 = Nivel(name="Nivel_1",master_surface = screen,x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
form_nivel_2 = Nivel(name="Nivel_2",master_surface = screen,x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)
form_nivel_3 = Nivel(name="Nivel_3",master_surface = screen,x=50,y=50,w=700,h=500,color_background=C_BLUE,color_border=C_BLUE,active=False)


pygame.mixer.music.load("../Project2/recursos/sonidos/musica_fondo.mp3")
pygame.mixer.music.play(-1)


while True:     

    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
              
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
        
    if(menu_principal.active):
          
        menu_principal.update(lista_eventos)
        menu_principal.draw()

    elif(settings.active):    
        settings.update(lista_eventos)
        settings.draw()

    elif(selec_level.active):    
        selec_level.update(lista_eventos)
        selec_level.draw()
            
    elif(pause_game.active):
        pause_game.update(lista_eventos)
        pause_game.draw()


    elif(form_nivel_1.active):#########################################nivel 1
        form_nivel_1.nivel.run_level(delta_ms,lista_eventos,keys)
        form_nivel_1.update(lista_eventos)
        
        if form_nivel_1.nivel.game_lose:
            loser.nivel_hs = form_nivel_1.nivel.hs
            loser.nivel = 1
            form_nivel_1.on_click_boton1("lose")
            form_nivel_1.reset(screen,"Nivel_1")
                

        elif form_nivel_1.nivel.game_win:
            win.nivel_hs = form_nivel_1.nivel.hs
            win.nivel = 1
            form_nivel_1.on_click_boton1("win")
            form_nivel_1.reset(screen,"Nivel_1")  

    elif(form_nivel_2.active):##############################################nivel2  
        form_nivel_2.nivel.run_level(delta_ms,lista_eventos,keys)
        form_nivel_2.update(lista_eventos)
            
        if form_nivel_2.nivel.game_lose:
            loser.nivel_hs = form_nivel_2.nivel.hs
            loser.nivel = 2
            form_nivel_2.on_click_boton1("lose")
            form_nivel_2.reset(screen,"Nivel_2")
               
                
        elif form_nivel_2.nivel.game_win:
            win.nivel_hs = form_nivel_2.nivel.hs
            win.nivel = 2
            form_nivel_2.on_click_boton1("win")
            form_nivel_2.reset(screen,"Nivel_2")    

    elif(form_nivel_3.active):#############################################nivel3
        form_nivel_3.nivel.run_level(delta_ms,lista_eventos,keys)
        form_nivel_3.update(lista_eventos)
            
        if form_nivel_3.nivel.game_lose:
            loser.nivel_hs = form_nivel_3.nivel.hs
            loser.nivel = 2
            form_nivel_3.on_click_boton1("lose")
            form_nivel_3.reset(screen,"Nivel_3")    

        elif form_nivel_3.nivel.game_win:
            loser.nivel_hs = form_nivel_3.nivel.hs
            loser.nivel = 2
            form_nivel_3.on_click_boton1("win")      
            form_nivel_3.reset(screen,"Nivel_3") 

    elif(ranking.active):
        ranking.reset_select()
        ranking.update(lista_eventos)
        ranking.draw()

    elif(win.active):
        win.update(lista_eventos)
        win.draw()

    elif(loser.active):    
        loser.update(lista_eventos)
        loser.draw()

    pygame.display.flip()




    


  



