import sqlite3
import re
from pygame.locals import *


def crear_tabla():
    import sqlite3
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        try:
            sentencia = ''' create  table Puntajes
                            (
                                    ID integer primary key autoincrement,
                                    nivel text,
                                    highscore numeric,
                                    name text
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla personajes")                       
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")    


def insertar(highscore, nivel,name):
    import sqlite3
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        try:
            conexion.execute("insert into Puntajes(name, highscore, nivel) values (?,?,?)", (name, highscore, nivel))
            
            conexion.commit()# Actualiza los datos realmente en la tabla

        except:
            print("Error")

def select():
    '''
    Selecciona los cinco mejores de la tabla Puntajes.

    Parámetro: None.
    Retorno: list.
    '''
    import sqlite3
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        conexion.commit()
        cursor=conexion.execute("SELECT name, highscore, nivel FROM Puntajes ORDER BY highscore DESC LIMIT 5;")
        
        lista_de_posiciones = []
        for fila in cursor:
            fila_mensaje= "{0}|HighScore:{1}|Nivel:{2} ".format(fila[0],fila[1],fila[2])
             
            lista_de_posiciones.append(fila_mensaje)
           
        return lista_de_posiciones


def comparate_name(nombre):
    '''
    Recorre los nombres de la tabla Puntajes y retorna True si tengo dos nombres iguales.

    Parámetro: nombre.
    Retorno: True or False.
    '''
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        cursor =  conexion.execute("SELECT name FROM Puntajes ")
        
        for fila in cursor: 
            if (fila[0].upper() == nombre): 
                return True
            
        return False
                
def comparete_highscore(nombre,score,nivel):
    '''
    Recorre la lista de la tabla Puntajes y compara el highscore nuevo con el que ya se encuentra
    registrado en dicha tabla, y tambien compara el nivel de éstos. 
    Retorna True si el highscore nuevo es mayor que el registrado anteriormente y si el nivel de ambos
    es igual.

    Parámetro: nombre, score, nivel.
    Retorno: True or False. 
    '''
    
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        cursor= conexion.execute("SELECT highscore, nivel FROM Puntajes WHERE name=? and nivel=?",(nombre,nivel,))
        for fila in cursor:
            if (score > fila[0] ):
                return True
            
        return False

def comparete_nivel(nombre,nivel):
    '''
    Compara si el nivel ingresado es igual a uno ya existente con el nombre tambien ingresado, 
    retornando True de ser así.

    Parámetro: nombre,nivel.
    Retorno: True or False. 
    '''
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        cursor= conexion.execute("SELECT nivel FROM Puntajes WHERE name=?",(nombre,))
        
        for fila in cursor:
            if (int(nivel) == int(fila[0])):
                return True
            
        return False


def register_name(nombre,score,nivel):
    '''
    Registra los nuevos datos del jugador que posea el mismo nombre que uno ya ingresado,
    y tenga un mayor score que el que se encuentra registrado.

    Parámetro: nombre, score, nivel.
    Retorno: None.
    '''
    nombre = nombre.upper()         
    nombre_registrado = comparate_name(nombre)
    
    if(nombre_registrado):
        nivel_comparado = comparete_nivel(nombre,nivel)
        if(nivel_comparado):
            high_score_comparado = comparete_highscore(nombre,score,nivel) 
            if (high_score_comparado):
                update_highscore(nombre,score,nivel)
                   
        else:
            insertar(score, nivel, nombre)
    else: 
        insertar(score,nivel,nombre)
              

def update_highscore(nombre,score,nivel):
    '''
    Actualiza la tabla de Puntajes con el nuevo registro, habiendo hecho la comparación de datos. 

    Parámetros: nombre, score.
    Retorno: None.
    '''
    with sqlite3.connect("../Project2/gui/base_datos_game.db") as conexion:
        update = conexion.execute("UPDATE Puntajes SET highscore =? WHERE name=? and nivel=?",(score,nombre,nivel,))
        players = update.fetchall()
        for player in players:
            print(player)


