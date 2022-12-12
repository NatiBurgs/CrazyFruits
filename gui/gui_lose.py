import pygame
from pygame.locals import *
from gui_constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from sql_data import *



class Lose(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.nivel_hs= None
        self.nivel= None

        self.boton_exit = Button(master=self,x=300,y=400,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/next.png",on_click=self.on_click_boton3,on_click_param="ranking",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.name_player = TextBox(master=self,x=150,y=300,w=400,h=50,color_background=C_YELLOW_2,color_border=C_RED,image_background=None,on_click=None,on_click_param=None,text="Name",font="Verdana",font_size=50,font_color=C_BLACK)

        self.titulo = TextBox(master=self,x=100,y=0,w=500,h=200,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/you_lose/header.png",text=None,font="Verdana",font_size=30,font_color=C_BLACK)
        
        
        self.lista_widget = [self.titulo,self.boton_exit,self.name_player]

    def on_click_boton3(self, parametro):
        self.set_active(parametro)
        register_name(self.name_player._text,self.nivel_hs,self.nivel)
        #insertar(self.nivel_hs,self.nivel,self.name_player._text)


    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

    