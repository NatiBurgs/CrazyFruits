import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_constantes import *
from sql_data import *


class Ranking(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.puntajes = select()[0]
        self.puntajes_2 = select()[1]
        self.puntajes_3 = select()[2]
        self.puntajes_4 = select()[3]
        self.puntajes_5 = select()[4]
        
        self.boton_texto_1= TextBox(master=self,x=50,y=200,w=600,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/table.png",on_click=None,on_click_param=None,text=self.puntajes,font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_texto_2= TextBox(master=self,x=50,y=250,w=600,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/table.png",on_click=None,on_click_param=None,text=self.puntajes_2,font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_texto_3= TextBox(master=self,x=50,y=300,w=600,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/table.png",on_click=None,on_click_param=None,text=self.puntajes_3,font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_texto_4= TextBox(master=self,x=50,y=350,w=600,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/table.png",on_click=None,on_click_param=None,text=self.puntajes_4,font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_texto_5= TextBox(master=self,x=50,y=400,w=600,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/table.png",on_click=None,on_click_param=None,text=self.puntajes_5,font="Verdana",font_size=20,font_color=C_WHITE)

        self.boton_titulo = TextBox(master=self,x=100,y=0,w=500,h=200,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/rating/header.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.boton_exit = Button(master=self,x=600,y=10,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/close_2.png",on_click=self.on_click_boton1,on_click_param="menu_principal",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.boton_titulo,self.boton_exit,self.boton_texto_1,self.boton_texto_2,self.boton_texto_3,self.boton_texto_4,self.boton_texto_5]
        

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def reset_select(self):
        lista_puntajes = select()
        for puntaje in lista_puntajes:
            self.boton_texto_1._text = lista_puntajes[0]
            self.boton_texto_2._text = lista_puntajes[1]
            self.boton_texto_3._text = lista_puntajes[2]
            self.boton_texto_4._text = lista_puntajes[3]
            self.boton_texto_5._text = lista_puntajes[4]
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()

        for aux_boton in self.lista_widget:    
            aux_boton.draw()