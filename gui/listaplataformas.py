import pygame
from plataforma import Plataform
from constantes import *


plataform_list = []
#plataforma movible


#primer plataforma superior izq
for x in range(0,160,40):
    plataform_list.append(Plataform(x,y=200,width=50,height=50,type=2))

#segunda plataforma superior der
for x in range(640,800,40):
    plataform_list.append(Plataform(x,y=200,width=50,height=50,type=2))

#primerplataforma subinferior der
for x in range(0, 240,40):
    plataform_list.append(Plataform(x,y=300,width=50,height=40,type=2))
#segunda plat subinferior izq
for x in range(560,800,40):
    plataform_list.append(Plataform(x,y=300,width=50,height=40,type=2))

#primer plataforma central
for x in range(280,500,40):
    plataform_list.append(Plataform(x,y=250,width=50,height=50,type=2))
#segunda plataforma central
for x in range(280,500,40):
    plataform_list.append(Plataform(x,y=400,width=50,height=30,type=2))
#escalon pequeño der
plataform_list.append(Plataform(x=250,y=350,width=50,height=30,type=2))
#escalon pequeño izq
plataform_list.append(Plataform(x=500,y=350,width=50,height=30,type=2))
#escalera derc
plataform_list.append(Plataform(x=200,y=440,width=50,height=20,type=2))
#escalera izq
plataform_list.append(Plataform(x=550,y=440,width=50,height=20,type=2))
#nivel del suelo 500
for x in range(0,840,40):
    plataform_list.append(Plataform(x,y=500,width=50,height=50,type=2))
#print("la cant es {0}".format(len(plataform_list))) hasta aca tengo 57 elementos en el json





#plataforma debajo del nivel del suelo
for x in range(0,840,40):
    plataform_list.append(Plataform(x,y=530,width=50,height=50,type=13))
#segundo debajo del nivel del suelo
for x in range (0,840,40):
    plataform_list.append(Plataform(x,y=555,width=50,height=50,type=13))
#ultimo debajo del suelo 
for x in range(0,840,40):
    plataform_list.append(Plataform(x,y=570,width=50,height=50,type=13))

#borde de abajo
for x in range(0,840,20):
    plataform_list.append(Plataform(x,y=585,width=50,height=50,type=4))
#borde de arriba
#borda lateral derecho
#borde lateral izquierdo

##################################################################################################
plataform_list_2 = []

for x in range(0,850,40):
    plataform_list_2.append(Plataform(x,y=500,width=50,height=50,type=9))
#plat 2
for x in range (460,560,40):
    plataform_list_2.append(Plataform(x, y = 380, width=50,height=50,type=9))
#plat 1 
for x in range (600,740,40):
    plataform_list_2.append(Plataform(x, y = 430, width=50,height=50,type=9))
#plat 3   
for x in range (200,420,40):
    plataform_list_2.append(Plataform(x, y = 330, width=50,height=50,type=9))    
#plat 5
for x in range (200,420,40):
    plataform_list_2.append(Plataform(x, y = 180, width=50,height=50,type=9))
#plat 6
for x in range (460,560,40):
    plataform_list_2.append(Plataform(x, y = 100, width=50,height=50,type=9))
#plat 7
for x in range (600,740,40):
    plataform_list_2.append(Plataform(x, y = 430, width=50,height=50,type=9))
#plat 8
#plat 7
for x in range (700,740,40):
    plataform_list_2.append(Plataform(x, y = 230, width=50,height=50,type=9))#hasta aca el json, me dice que la lista llega a 49 en 
                                                                                #este archivo
#print("lista 2 son {0}".format(len(plataform_list_2)))
    


for x in range(0,840,40):
    plataform_list_2.append(Plataform(x,y=530,width=50,height=50,type=9))

for x in range (0,840,40):
    plataform_list_2.append(Plataform(x, y = 570, width=50,height=50,type=13))

   
    
################################################################################################









