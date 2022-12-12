import pygame
from pygame.locals import *
from gui_constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
#from gui_main import form_nivel_1




class Settings(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        self.titulo = TextBox(master=self,x=150,y=0,w=400,h=150,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/settings/92.png",on_click=None,on_click_param=None,text=None,font="Verdana",font_size=10,font_color=C_WHITE)
        
        self.boton1 = Button(master=self,x=550,y=400,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/settings/97.png",on_click=self.on_click_boton1,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=150,y=400,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/settings/98.png",on_click=self.on_click_boton2,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
 
        self.titulo_music = TextBox(master=self,x=100,y=200,w=100,h=60,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/shop/btn.png",on_click=None,on_click_param=None,text="MUSIC",font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_efectos_on = Button(master=self,x=350,y=200,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/misic.png",on_click=self.on_click_music_on,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)      
        self.boton_efectos_off = Button(master=self,x=450,y=200,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/music_off.png",on_click=self.on_click_music_off,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.titulo_sonidos = TextBox(master=self,x=100,y=300,w=100,h=60,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/shop/btn.png",on_click=None,on_click_param=None,text="SOUND",font="Verdana",font_size=20,font_color=C_WHITE)
        self.boton_sonidos_on = Button(master=self,x=350,y=300,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/misic.png",on_click=self.on_click_efect_on,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)      
        self.boton_sonidos_off = Button(master=self,x=450,y=300,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/music_off.png",on_click=self.on_click_efect_off,on_click_param=None,text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        


        self.txt1 = TextBox(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/Menu/Buttons/Play.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        
        self.pb1 = ProgressBar(master=self,x=200,y=400,w=350,h=20,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/settings/93.png",image_progress="../Project2/recursos/gui/jungle/settings/94.png",value = 3, value_max=3)
        
        self.boton_exit = Button(master=self,x=600,y=10,w=50,h=50,color_background=None,color_border=None,image_background="../Project2/recursos/gui/jungle/btn/close_2.png",on_click=self.on_click_boton3,on_click_param="menu_principal",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.boton_sonidos_off,self.boton_sonidos_on,self.titulo_sonidos,self.boton1,self.boton2, self.pb1,self.titulo,self.boton_exit,self.boton_efectos_on, self.titulo_music,self.boton_efectos_off ]

        
    
    def on_click_boton1(self, parametro):
        self.pb1.value += 1
        if pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.33)
        elif pygame.mixer.music.get_volume() == 1.0:
            pygame.mixer.music.set_volume(1.0)
            

    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
        if pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.33)
        elif pygame.mixer.music.get_volume() == 0.0:
            pygame.mixer.music.set_volume(0.0)
            
    def on_click_music_off(self,parametro):
        pygame.mixer.music.set_volume(0.0)

    def on_click_music_on(self,parametro):
        pygame.mixer.music.set_volume(1.0)

    def on_click_efect_off(self,parametro):
        pass

    def on_click_efect_on(self,parametro):
        pass
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()