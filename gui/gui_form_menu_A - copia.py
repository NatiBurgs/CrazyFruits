import pygame
from pygame.locals import *
from gui_constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/Menu/Buttons/Play.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="SUMA +",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=0,y=60,w=140,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/Menu/Buttons/Play.png",on_click=self.on_click_boton2,on_click_param="form_menu_B",text="RESTA -",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=0,y=120,w=140,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/Menu/Buttons/Play.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="MENU",font="Verdana",font_size=30,font_color=C_WHITE)
              
        self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/Menu/Buttons/Play.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        self.pb1 = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/bubble/load.png",image_progress="../Project2/recursos/Menu/Buttons/Next.png",value = 3, value_max=8)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.txt1,self.pb1]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1

    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()