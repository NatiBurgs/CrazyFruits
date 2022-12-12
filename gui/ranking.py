import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from const import *

class Ranking(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton_titulo = TextBox(master=self,x=100,y=0,w=500,h=200,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/rating/header.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.boton_play = Button(master=self,x=100,y=400,w=100,h=100,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/menu/play.png",on_click=self.on_click_boton1,on_click_param="select_level",text=None,font="Verdana",font_size=1,font_color=C_WHITE)
        self.boton_setting = Button(master=self,x=500,y=400,w=100,h=100,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/menu/setting.png",on_click=self.on_click_boton1,on_click_param="setting",text=None,font="Verdana",font_size=1,font_color=C_WHITE)
       
        self.boton_exit = Button(master=self,x=600,y=10,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/close_2.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.boton_play,self.boton_setting,self.boton_titulo,self.boton_exit]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()