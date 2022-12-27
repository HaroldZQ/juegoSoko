import pygame, sys
import numpy as np

pygame.init()
tablero = np.array([[0,0,0,0,0,0,0,0]   #tablero [fila][columna]->inicio: tablero[0][0]
                   ,[0,0,0,0,1,1,0,0]   #En 0 se encuentran las cajas
                   ,[0,0,1,1,2,1,0,0]   #En 1,2,3 y 4 se desplaza el personaje
                   ,[0,0,1,0,1,0,0,0]   #En 2,3,4 se encuentran los bloques movibles
                   ,[0,1,1,0,1,0,5,0]
                   ,[0,1,0,1,1,2,5,0]
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
personaje = pygame.image.load("Imagenes/Personaje1.jpeg")
bloque_Mov = pygame.image.load("Imagenes/LadrilloMovible.png")
Diamante = pygame.image.load("Imagenes/Diamante.jpeg")
#Icono y titulo para la ventana(Esquina superior)
pygame.display.set_icon(personaje)
pygame.display.set_caption("Sokoban")

#Imagenes de elementos del juego transformadas a deternida escala
bloque = pygame.transform.scale(bloque, (50,50))
personaje = pygame.transform.scale(personaje, (50,50))
bloque_Mov = pygame.transform.scale(bloque_Mov, (50,50))
Diamante = pygame.transform.scale(Diamante, (50,50))
#-----------------------------------------------------

#VARIABLES
#-------------------------------------------------
#Definimos las coordenadas iniciales del personaje
cord_x = 465
cord_y = 125
#cajas Movibles:
cordC_x = 405
cordC_y = 185 
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
                

#Funcion de mapa movilidad-EN PRUEBA
def pos_inicial():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]>=1: #tablero[fila][columna]
                #cord_x = 465  
                #cord_y = 125
                screen.blit(personaje,[cord_x,cord_y,50,50])

#[1]Funcion de mapa movilidad-EN PRUEBA-BUSCAR SOLUCIÓN
def mov_personaje(cordx,cordy,xspeed,yspeed):
    if (165<=cordx and cordx<=585)and(65<=cordy and cordy<=485): 
        cordx += xspeed
        cordy += yspeed
        x = int((cordx-165)/60)
        y = int((cordy-65)/60)
        print(x,y)
        if tablero[y][x]>=1:
            screen.blit(personaje,[cordx,cordy,50,50])
        else:
            cordx -= xspeed
            cordy -= yspeed
            screen.blit(personaje,[cordx,cordy,50,50])

#Función para los bloques movibles
def bloqueMovible():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==2: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(bloque_Mov,[x_1,y_1,50,50])
#------------------------------------------------------    

#Función para los bloques movibles
def diamante():
    for x in range(0,8): #x:columna
        for y in range(0,8): #y:fila
            if tablero[y][x]==5: #tablero[fila][columna]
                x_1 = 165+60*x
                y_1 = 65+60*y
                screen.blit(Diamante,[x_1,y_1,50,50])
#REALIZA JUEGO-BULCE INFINITO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         #Evento teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -60
                #izquierda = True

            if event.key == pygame.K_RIGHT:
                x_speed =60
                #derecha = True

            if event.key == pygame.K_UP:
                y_speed = -60
                #arriba = True

            if event.key == pygame.K_DOWN:
                y_speed = 60
                #abajo = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
                #izquierda = False
            if event.key == pygame.K_RIGHT:
                x_speed = 0
                #derecha = False
            if event.key == pygame.K_UP:
                y_speed = 0
                #arriba = False
            if event.key == pygame.K_DOWN:
                y_speed = 0
                #abajo = False


    #Color de fondo
    screen.blit(background,[-10,-10])
    
    #mapaJuego() 
    #bloqueMovible()
    #Para mover personaje-CONVERTIRLO EN UNA FUNCIÓN[1]
    if (165<=cord_x and cord_x<=585)and(65<=cord_y and cord_y<=485):
        cord_x += x_speed
        cord_y += y_speed
        #cordC_x += x_speed
        #cordC_y += y_speed
        x = int((cord_x-165)/60)
        y = int((cord_y-65)/60)
        print(x,y) #Para ver coordenada de la M.Bidimensional
        if tablero[y][x]>=1 :
            print(tablero)
            screen.blit(personaje,[cord_x,cord_y,50,50])
            if tablero[y][x]==2:
                cordC_x += x_speed #Izquierda->cordC_x=405-60
                cordC_y += y_speed #Izquierda->cordC_y=185
                #screen.blit(bloque_Mov,[cord_x+x_speed,cordC_y+y_speed,50,50])
                screen.blit(personaje,[cord_x,cord_y,50,50])
                if x_speed == -60:
                    tablero[y][x]=1
                    tablero[y][x-1]=2
                elif y_speed == 60:
                    tablero[y][x]=1
                    tablero[y+1][x]=2
                elif y_speed == -60:
                    tablero[y][x]=1
                    tablero[y-1][x]=2
                elif x_speed == 60:
                    tablero[y][x]=1
                    tablero[y][x+1]=2
               
        else:
            cord_x -= x_speed
            cord_y -= y_speed
            print(tablero)
            screen.blit(personaje,[cord_x,cord_y,50,50])
            #Colocando sonido, cuando el personaje choque en el muro
            #pygame.mixer.music.load("Música y Sonido/SaltosoMovi.mpeg")
            #pygame.mixer.music.play()
            
                       
    mapaJuego() #Llamamos función del mapa
    #mov_personaje(cord_x,cord_y,x_speed,y_speed)
    
    #Bloques movibles      
    bloqueMovible()

    #Diamantes
    diamante()
    #Actualizar pantalla
    pygame.display.flip()
    
    #Para la rapidez de movilidad del jugador
    clock.tick(6)#Con valor 6, funciona bien.Probar con otros valores 
    