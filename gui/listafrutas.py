import pygame
from fruits import Fruits


fruit_list= []

fruit_1 =Fruits(120,170,0,0)
fruit_2 =Fruits(80,140,0,0)
fruit_3 =Fruits(40,110,0,0)
fruit_4 =Fruits(0,80,0,0)
fruit_list.append(fruit_1) 
fruit_list.append(fruit_2)
fruit_list.append(fruit_3)
fruit_list.append(fruit_4)


fruit_8 =Fruits(640,170,0,0)
fruit_9 =Fruits(680,140,0,0)
fruit_10 =Fruits(720,110,0,0)
fruit_11 =Fruits(760,80,0,0)
fruit_list.append(fruit_8) 
fruit_list.append(fruit_9)
fruit_list.append(fruit_10)
fruit_list.append(fruit_11)



fruit_12 =Fruits(60,450,0,0)
fruit_13 =Fruits(120,450,0,0)
fruit_14 =Fruits(180,450,0,0)
fruit_15 =Fruits(250,450,0,0)
fruit_list.append(fruit_12) 
fruit_list.append(fruit_13)
fruit_list.append(fruit_14)
fruit_list.append(fruit_15)

fruit_16 =Fruits(500,450,0,0)
fruit_17 =Fruits(550,450,0,0)
fruit_18 =Fruits(600,450,0,0)
fruit_19 =Fruits(650,450,0,0)
fruit_list.append(fruit_16) 
fruit_list.append(fruit_17)
fruit_list.append(fruit_18)
fruit_list.append(fruit_19)

fruit_20 =Fruits(300,350,0,0)
fruit_21 =Fruits(350,350,0,0)
fruit_22 =Fruits(400,350,0,0)
fruit_23 =Fruits(450,350,0,0)
fruit_list.append(fruit_20) 
fruit_list.append(fruit_21)
fruit_list.append(fruit_22)
fruit_list.append(fruit_23)

fruit_24 =Fruits(50,250,0,0)
fruit_25 =Fruits(100,250,0,0)
fruit_26 =Fruits(150,250,0,0)
fruit_27 =Fruits(200,250,0,0)
fruit_list.append(fruit_24) 
fruit_list.append(fruit_25)
fruit_list.append(fruit_26)
fruit_list.append(fruit_27)

fruit_28 =Fruits(300,50,0,0)
fruit_29 =Fruits(350,50,0,0)
fruit_30 =Fruits(400,50,0,0)
fruit_31 =Fruits(450,50,0,0)
fruit_list.append(fruit_28) 
fruit_list.append(fruit_29)
fruit_list.append(fruit_30)
fruit_list.append(fruit_31)

fruit_32 =Fruits(300,150,0,0)
fruit_33 =Fruits(350,150,0,0)
fruit_34 =Fruits(400,150,0,0)
fruit_35 =Fruits(450,150,0,0)
fruit_list.append(fruit_32) 
fruit_list.append(fruit_33)
fruit_list.append(fruit_34)
fruit_list.append(fruit_35)


fruit_36 =Fruits(550,250,0,0)
fruit_37 =Fruits(600,250,0,0)
fruit_38 =Fruits(650,250,0,0)
fruit_39 =Fruits(700,250,0,0)
fruit_list.append(fruit_36) 
fruit_list.append(fruit_37)
fruit_list.append(fruit_38)
fruit_list.append(fruit_39)

fruit_40 =Fruits(300,100,0,0)
fruit_41 =Fruits(350,100,0,0)
fruit_42 =Fruits(400,100,0,0)
fruit_43 =Fruits(450,100,0,0)
fruit_list.append(fruit_40) 
fruit_list.append(fruit_41)
fruit_list.append(fruit_42)
fruit_list.append(fruit_43)



###############################################################################################
        
fruit_list_2 = []
fruit_2_1 = Fruits(100,480)
fruit_list_2.append(fruit_2_1)

for x in range(100,800,100):
    for y in range(480,510,30):
        fruit_list_2.append(Fruits(x,y))#nivel del suelo

for x in range(650,850,50):
    for y in range(410,440,30):
        fruit_list_2.append(Fruits(x,y))#primer plataforma

for x in range(50,160,100):
    for y in range(50,450,100):
        fruit_list_2.append(Fruits(x,y))#movibles

for x in range(700,750,50):
    for y in range(100,250,50):
        fruit_list_2.append(Fruits(x,y,path_fruit="../Project2/recursos/Fruits/Melon.png"))

for x in range(450,600,50):
    y=350
    fruit_list_2.append(Fruits(x,y,path_fruit="../Project2/recursos/Fruits/Kiwi.png"))
for x in range(270,420,50):
    y=300
    fruit_list_2.append(Fruits(x,y,path_fruit="../Project2/recursos/Fruits/Cherries.png"))





for x in range(450,600,50):
    y=60
    fruit_list_2.append(Fruits(x,y,path_fruit="../Project2/recursos/Fruits/Orange.png"))

#################################################################################################

fruit_list_3 = []
for x in range(10,300,60):
    fruit_list_3.append(Fruits(x,y=270,path_fruit="../Project2/recursos/Fruits/Melon.png"))

for x in range(300,800,100):
    fruit_list_3.append(Fruits(x,y=370,path_fruit="../Project2/recursos/Fruits/Pineapple.png"))

for x in range(500,800,100):
    fruit_list_3.append(Fruits(x,y=270,path_fruit="../Project2/recursos/Fruits/Strawberry.png"))

for x in range(0,500,100):
    fruit_list_3.append(Fruits(x,y=170,path_fruit="../Project2/recursos/Fruits/Orange.png"))




for x in range(50,600,150):
    fruit_list_3.append(Fruits(x,y=70,path_fruit="../Project2/recursos/Fruits/Orange.png"))

fruit_3_1 = Fruits(650,50)
fruit_3_2 = Fruits(550,150)
fruit_3_3 = Fruits(350,250)
fruit_list_3.append(fruit_3_1)
fruit_list_3.append(fruit_3_2)
fruit_list_3.append(fruit_3_3)