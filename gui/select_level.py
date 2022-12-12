import pygame
from pygame.locals import *
from gui_constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_widget import Widget



class SelectLevel(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.titulo = TextBox(master=self,x=100,y=0,w=500,h=200,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/level_select/header.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.boton1 = Button(master=self,x=100,y=290,w=100,h=100,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/menu/play.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=300,y=290,w=100,h=100,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/menu/play.png",on_click=self.on_click_boton3,on_click_param="pause",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=500,y=290,w=100,h=100,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/menu/play.png",on_click=self.on_click_boton3,on_click_param="setting",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.text_boton_1 = TextBox(master=self,x=90,y=400,w=100,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/level.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        self.text_boton_2 = TextBox(master=self,x=290,y=400,w=100,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/level.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        self.text_boton_3 = TextBox(master=self,x=490,y=400,w=100,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/level.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.num_boton_1 =TextBox(master=self,x=200,y=400,w=20,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/1.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        self.num_boton_2 =TextBox(master=self,x=400,y=400,w=20,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/2.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        self.num_boton_3 =TextBox(master=self,x=600,y=400,w=20,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/3.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.boton_exit = Button(master=self,x=600,y=10,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/close_2.png",on_click=self.on_click_boton3,on_click_param="menu_principal",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.titulo,self.text_boton_1,self.text_boton_2 ,self.text_boton_3,self.num_boton_1,self.num_boton_2,self.num_boton_3,self.boton_exit   ]


    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
