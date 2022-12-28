import pygame, sys
import numpy as np

pygame.init()
tablero = np.array([[0,0,0,0,0,0,0,0]   #tablero [fila][columna]->inicio: tablero[0][0]
                   ,[0,0,0,0,1,6,0,0]   #En 0 se encuentran las cajas
                   ,[0,0,1,1,2,1,0,0]   #En >=1 se desplaza el personaje
                   ,[0,0,1,0,1,0,0,0]   #En 2 se encuentran los bloques movibles
                   ,[0,1,1,0,1,0,5,0]   #En 5 se encuentran los diamantes
                   ,[0,1,0,1,1,2,5,0]   #En 6 se encuentran el personaje
                   ,[0,1,2,1,1,1,5,0]
                   ,[0,0,0,0,0,0,0,0]])

#MÚSICA
#-----------------------------------------
#Función música-En PRUEBA
def makeSound(filename):
    pygame.mixer.init()
    Sonido = pygame.mixer.Sound(filename)

    return Sonido

#Para la música-CORRECTO
pygame.mixer.music.load("Música y Sonido/S.mario-bros.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
#----------------------------------------

#Definimos colores-Por se acaso
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#Caracteristica de la ventana
size = (800,600)#Largo x ancho

#Creamos ventana
screen = pygame.display.set_mode(size)
#Controlar los FPS
clock = pygame.time.Clock()

#IMAGENES
#----------------------------------------------------
#Fondo del juego
background = pygame.image.load("Imagenes/fotoFondo.jpg").convert()

#Imagenes de elementos del juego
bloque = pygame.image.load("Imagenes/Ladrillo.jpeg")
personaje = pygame.image.load("Imagenes/Personaje1.jpeg").convert_alpha()
bloque_Mov = pygame.image.load("Imagenes/LadrilloMovible.png")
Diamante = pygame.image.load("Imagenes/Diamante.jpeg")
#Icono y titulo para la ventana(Esquina superior)
pygame.display.set_icon(personaje)
pygame.display.set_caption("Sokoban")

#Imagenes de elementos del juego transformadas a deternida escala
bloque = pygame.transform.scale(bloque, (50,50))
personaje = pygame.transform.scale(personaje, (50,50))
#personaje =pygame.Surface((50,50))
#personaje = personaje.get_rect()
bloque_Mov = pygame.transform.scale(bloque_Mov, (50,50))
Diamante = pygame.transform.scale(Diamante, (50,50))
#-----------------------------------------------------

#VARIABLES
#-------------------------------------------------
#Definimos las coordenadas iniciales del personaje
x = 5
y = 1
#Velocidad de personaje
x_speed = 0
y_speed = 0
#-------------------------------------------------

#FUNCIONES
#------------------------------------------------------
#Funcion de mapa de juego-CORRECTO
def mapaJuego():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==0: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(bloque,[x_1,y_1,50,50])
                
#Función para los bloques movibles
def bloqueMovible():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==2: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(bloque_Mov,[x_1,y_1,50,50])
#Función para jugador
def jugadorMovible():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==6: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(personaje,[x_1,y_1,50,50]) 

#Función para los diamantes
def diamante():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==5: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(Diamante,[x_1,y_1,50,50])
#------------------------------------------------------  
#REALIZA JUEGO-BULCE INFINITO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         #Evento teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -1               

            if event.key == pygame.K_RIGHT:
                x_speed =1

            if event.key == pygame.K_UP:
                y_speed = -1

            if event.key == pygame.K_DOWN:
                y_speed = 1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0

            if event.key == pygame.K_RIGHT:
                x_speed = 0

            if event.key == pygame.K_UP:
                y_speed = 0

            if event.key == pygame.K_DOWN:
                y_speed = 0


    #Color de fondo
    screen.blit(background,[-10,-10])
    
    mapaJuego() 
    #Para mover personaje,cajas
    x += x_speed
    y += y_speed
    if x_speed == -1: #Izquierda
        if tablero[y][x]!=0:
            if tablero[y][x]==1 or tablero[y][x]==5: #Para mover por 1y5(Los diamantes)
                tablero[y][x]=6
                tablero[y][x+1]=1
            elif tablero[y][x]==2: #Para mover bloque(Estamos en 2)
                if tablero[y][x-1]!=0:
                    if tablero[y][x-1]!=2:
                        tablero[y][x-1]=2
                        tablero[y][x]=6
                        tablero[y][x+1]=1
                    else:#Caso,cuando se chocan 2 bloques movibles
                        tablero[y][x]=2
                        tablero[y][x+1]=6
                        tablero[y][x-1]=2 
                        x=x+1

                else:
                    tablero[y][x]=2
                    tablero[y][x+1]=6
                    x =x+1
                    #O tambien podemos colocar:
                    #x -= x_speed
                    #y -= y_speed
        else:
            x -= x_speed
            y -= y_speed
                                 
    elif y_speed == 1: #Abajo
        if tablero[y][x]!=0:
            if tablero[y][x]==1 or tablero[y][x]==5: #Para mover por 1y5(Los diamantes)
                tablero[y][x]=6
                tablero[y-1][x]=1
            elif tablero[y][x]==2: #Para mover bloque(Estamos en 2)
                if tablero[y+1][x]!=0:
                    if tablero[y+1][x]!=2:
                        tablero[y+1][x]=2
                        tablero[y][x]=6
                        tablero[y-1][x]=1
                    else:#Caso,cuando se chocan 2 bloques movibles
                        tablero[y][x]=2
                        tablero[y-1][x]=6
                        tablero[y+1][x]=2
                        y=y-1

                else:
                    tablero[y][x]=2
                    tablero[y-1][x]=6
                    y =y-1
                    #O tambien podemos colocar:
                    #x -= x_speed
                    #y -= y_speed
        else:
            x -= x_speed
            y -= y_speed
        
    elif y_speed == -1: #Arriba
        if tablero[y][x]!=0:
            if tablero[y][x]==1 or tablero[y][x]==5: #Para mover por 1y5(Los diamantes)
                tablero[y][x]=6
                tablero[y+1][x]=1
            elif tablero[y][x]==2: #Para mover bloque(Estamos en 2)
                if tablero[y-1][x]!=0:
                    if tablero[y-1][x]!=2:
                        tablero[y-1][x]=2
                        tablero[y][x]=6
                        tablero[y+1][x]=1
                    else:#Caso,cuando se chocan 2 bloques movibles
                        tablero[y][x]=2
                        tablero[y+1][x]=6
                        tablero[y-1][x]=2
                        y=y+1

                else:
                    tablero[y][x]=2
                    tablero[y+1][x]=6
                    y =y+1
                    #O tambien podemos colocar:
                    #x -= x_speed
                    #y -= y_speed
        else:
            x -= x_speed
            y -= y_speed
        
    elif x_speed == 1: #Derecha
        if tablero[y][x]!=0:
            if tablero[y][x]==1 or tablero[y][x]==5: #Para mover por 1y5(Los diamantes)
                tablero[y][x]=6
                tablero[y][x-1]=1
            elif tablero[y][x]==2: #Para mover bloque(Estamos en 2)
                if tablero[y][x+1]!=0:
                    if tablero[y][x+1]!=2:
                        tablero[y][x+1]=2
                        tablero[y][x]=6
                        tablero[y][x-1]=1 
                    else:#Caso,cuando se chocan 2 bloques movibles
                        tablero[y][x]=2
                        tablero[y][x-1]=6
                        tablero[y][x+1]=2 
                        x=x-1
                else:
                    tablero[y][x]=2
                    tablero[y][x-1]=6
                    x =x-1
                    #O tambien podemos colocar:
                    #x -= x_speed
                    #y -= y_speed                    
        else:
            x -= x_speed
            y -= y_speed
    #Para monitoriar juego:
    print(tablero)
    print(x,y)
            #Colocando sonido, cuando el personaje choque en el muro
            #pygame.mixer.music.load("Música y Sonido/SaltosoMovi.mpeg")
            #pygame.mixer.music.play()
            
                       
    #mapaJuego() #Llamamos función del mapa
    #Jugador Movible
    jugadorMovible()
    #Bloques movibles      
    bloqueMovible()

    #Diamantes
    diamante()
    #Actualizar pantalla
    pygame.display.flip()
    
    #Para la rapidez de movilidad del jugador
    clock.tick(6)#Con valor 6, funciona bien.Probar con otros valores