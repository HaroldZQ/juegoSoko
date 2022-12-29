import pygame,sys
import button
import numpy as np

pygame.init()
# create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SOKOBAN')


def sokoban():
    tablero = np.array([[0, 0, 0, 0, 0, 0, 0, 0]  # tablero [fila][columna]->inicio: tablero[0][0]
                        # En 0 se encuentran las cajas
                        # En >=1 se desplaza el personaje
                        # En 2 se encuentran los bloques movibles
                        # En 5 se encuentran los diamantes
                        # En 6 se encuentran el personaje
                        , [0, 0, 0, 0, 1, 6, 0, 0], [0, 0, 1, 1, 2, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 5, 0], [0, 1, 0, 1, 1, 2, 5, 0], [0, 1, 2, 1, 1, 1, 5, 0], [0, 0, 0, 0, 0, 0, 0, 0]])

    # MÚSICA
    # -----------------------------------------
    # Función música-En PRUEBA

    def makeSound(filename):
        pygame.mixer.init()
        Sonido = pygame.mixer.Sound(filename)

        return Sonido


    # Para la música-CORRECTO
    #pygame.mixer.music.load("Musica/S.mario-bros.mp3")
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(1)
    sonidoFondo=pygame.mixer.Sound("Musica/S.mario-bros.mp3")
    sonidoFondo.play()
    # ----------------------------------------

    # Definimos colores-Por se acaso
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Caracteristica de la ventana
    size = (800, 600)  # Largo x ancho

    #Etiqueta
    fuente1 = pygame.font.SysFont("Arial",34,True,False)
    info = fuente1.render("CONTADOR",0,GREEN)
    #salir = False
    
    # Creamos ventana
    screen = pygame.display.set_mode(size)
    # Controlar los FPS
    clock = pygame.time.Clock()

    # IMAGENES
    # ----------------------------------------------------
    # Fondo del juego
    background = pygame.image.load("Imagenes/fotoFondo.jpg").convert()

    # Imagenes de elementos del juego
    bloque = pygame.image.load("Imagenes/Ladrillo.jpeg")
    personaje = pygame.image.load("Imagenes/Personaje1.jpeg").convert_alpha()
    bloque_Mov = pygame.image.load("Imagenes/LadrilloMovible.png")
    Diamante = pygame.image.load("Imagenes/Diamante.jpeg")
    # Icono y titulo para la ventana(Esquina superior)
    pygame.display.set_icon(personaje)
    pygame.display.set_caption("Sokoban")

    # Imagenes de elementos del juego transformadas a deternida escala
    bloque = pygame.transform.scale(bloque, (50, 50))
    personaje = pygame.transform.scale(personaje, (50, 50))
    # personaje =pygame.Surface((50,50))
    # personaje = personaje.get_rect()
    bloque_Mov = pygame.transform.scale(bloque_Mov, (50, 50))
    Diamante = pygame.transform.scale(Diamante, (50, 50))
    # -----------------------------------------------------

    # VARIABLES
    # -------------------------------------------------
    # Definimos las coordenadas iniciales del personaje
    #Ya no es necesario, ya que se creo una funcion para ello
    # x = 465
    # y = 125
    # Velocidad de personaje
    x_speed = 0
    y_speed = 0
    # -------------------------------------------------

    # FUNCIONES
    # ------------------------------------------------------
    # Funcion de mapa de juego-CORRECTO
    def mapaJuego():
        for x in range(0, 8):  # x:columna
            for y in range(0, 8):  # y:fila
                if tablero[y][x] == 0:  # tablero[fila][columna]
                    x_1 = 165+60*x
                    y_1 = 65+60*y
                    screen.blit(bloque, [x_1, y_1, 50, 50])

     # Función para los bloques movibles


    def bloqueMovible():
        for x in range(0, 8):  # x:columna
            for y in range(0, 8):  # y:fila
                if tablero[y][x] == 2:  # tablero[fila][columna]
                    x_1 = 165+60*x
                    y_1 = 65+60*y
                    screen.blit(bloque_Mov, [x_1, y_1, 50, 50])
    # Función para jugador


    def jugadorMovible():
        for x in range(0, 8):  # x:columna
            for y in range(0, 8):  # y:fila
                if tablero[y][x] == 6:  # tablero[fila][columna]
                   x_1 = 165+60*x
                   y_1 = 65+60*y
                   screen.blit(personaje, [x_1, y_1, 50, 50])

    
    #Función para posición inicial del jugador

    def posicionJugadorInicio():
        for x in range(0,8): #x:columna
            for y in range(0,8): #y:fila
                if tablero[y][x]==6: #tablero[fila][columna]
                      valory=y
                      valorx=x
        return valorx,valory





    # Función para los diamantes
    def diamante():
        for x in range(0, 8):  # x:columna
            for y in range(0, 8):  # y:fila
                if tablero[y][x] == 5:  # tablero[fila][columna]
                   x_1 = 165+60*x
                   y_1 = 65+60*y
                   screen.blit(Diamante, [x_1, y_1, 50, 50])
    
    #Funciones de sonidos
    
    def sonidoChoqueLadrillo():
         sonidoChoque=pygame.mixer.Sound("Musica/SaltosoMovi.mpeg")
         sonidoChoque.play()

    def musicaVictoriaJuego():
        num=0
        for x in range(0,8): #x:columna
            for y in range(0,8): #y:fila
                if tablero[y][x]!=5: #tablero[fila][columna]
                    num=num+1
        if num==64:
             musicaVictoria=pygame.mixer.Sound("Musica/Puntoextra.mpeg")
             musicaVictoria.play(-1)
             sonidoFondo.stop()

# Definiendo valores iniciales del jugador: 
#x , y = jugadorMovible() #Aplicando códigos [2]
    x , y = posicionJugadorInicio()
    

    # ------------------------------------------------------
    # REALIZA JUEGO-BULCE INFINITO
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Evento teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -1

                if event.key == pygame.K_RIGHT:
                    x_speed = 1

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

        # Color de fondo
        screen.blit(background, [-10, -10])
        
        #etiqueta contador      
        screen.blit(info,(5,5))
        segundos =int(pygame.time.get_ticks()/1000)
        segundos = str(segundos)
        contador = fuente1.render(segundos,0,GREEN)
        screen.blit(contador,(300,5))

        mapaJuego()
        # Para mover personaje,cajas
        x += x_speed
        y += y_speed
        if x_speed == -1:  # Izquierda
            if tablero[y][x] != 0:
                if tablero[y][x] == 1 or tablero[y][x] == 5:
                    tablero[y][x] = 6
                    tablero[y][x+1] = 1
                elif tablero[y][x] == 2:  # Para mover bloque(Estamos en 2)
                    if tablero[y][x-1] != 0:
                        if tablero[y][x-1] != 2:
                            tablero[y][x-1] = 2
                            tablero[y][x] = 6
                            tablero[y][x+1] = 1
                        else:  # Caso,cuando se chocan 2 bloques movibles
                            tablero[y][x] = 2
                            tablero[y][x+1] = 6
                            tablero[y][x-1] = 2
                            x = x+1
                            sonidoChoqueLadrillo()

                    else:
                        tablero[y][x] = 2
                        tablero[y][x+1] = 6
                        x = x+1
                        sonidoChoqueLadrillo()
                        # O tambien podemos colocar:
                        # x -= x_speed
                        # y -= y_speed
            else:
                x -= x_speed
                y -= y_speed
                sonidoChoqueLadrillo()

        elif y_speed == 1:  # Abajo
            if tablero[y][x] != 0:
            
                if tablero[y][x] == 1 or tablero[y][x] == 5:
                    tablero[y][x] = 6
                    tablero[y-1][x] = 1
                elif tablero[y][x] == 2:  # Para mover bloque(Estamos en 2)
                    if tablero[y+1][x] != 0:
                        if tablero[y+1][x] != 2:
                            tablero[y+1][x] = 2
                            tablero[y][x] = 6
                            tablero[y-1][x] = 1
                        else:  # Caso,cuando se chocan 2 bloques movibles
                            tablero[y][x] = 2
                            tablero[y-1][x] = 6
                            tablero[y+1][x] = 2
                            y = y-1
                            sonidoChoqueLadrillo()

                    else:
                        tablero[y][x] = 2
                        tablero[y-1][x] = 6
                        y = y-1
                        sonidoChoqueLadrillo()
                        # O tambien podemos colocar:
                        # x -= x_speed
                        # y -= y_speed
            else:
                x -= x_speed
                y -= y_speed
                sonidoChoqueLadrillo()

        elif y_speed == -1:  # Arriba
            if tablero[y][x] != 0:
               
                if tablero[y][x] == 1 or tablero[y][x] == 5:
                    tablero[y][x] = 6
                    tablero[y+1][x] = 1
                elif tablero[y][x] == 2:  # Para mover bloque(Estamos en 2)
                      if tablero[y-1][x] != 0:
                          if tablero[y-1][x] != 2:
                              tablero[y-1][x] = 2
                              tablero[y][x] = 6
                              tablero[y+1][x] = 1
                          else:  # Caso,cuando se chocan 2 bloques movibles
                              tablero[y][x] = 2
                              tablero[y+1][x] = 6
                              tablero[y-1][x] = 2
                              y = y+1
                              sonidoChoqueLadrillo()

                      else:
                          tablero[y][x] = 2
                          tablero[y+1][x] = 6
                          y = y+1
                          sonidoChoqueLadrillo()
                          # O tambien podemos colocar:
                          # x -= x_speed
                          # y -= y_speed
            else:
                x -= x_speed
                y -= y_speed
                sonidoChoqueLadrillo()

        elif x_speed == 1:  # Derecha
            if tablero[y][x] != 0:
               # Para mover por 1y5(Los diamantes)
                if tablero[y][x] == 1 or tablero[y][x] == 5:
                    tablero[y][x] = 6
                    tablero[y][x-1] = 1
                elif tablero[y][x] == 2:  # Para mover bloque(Estamos en 2)
                    if tablero[y][x+1] != 0:
                        if tablero[y][x+1] != 2:
                            tablero[y][x+1] = 2
                            tablero[y][x] = 6
                            tablero[y][x-1] = 1
                        else:  # Caso,cuando se chocan 2 bloques movibles
                            tablero[y][x] = 2
                            tablero[y][x-1] = 6
                            tablero[y][x+1] = 2
                            x = x-1
                            sonidoChoqueLadrillo()
                    else:
                        tablero[y][x] = 2
                        tablero[y][x-1] = 6
                        x = x-1
                        sonidoChoqueLadrillo()
                        # O tambien podemos colocar:
                        # x -= x_speed
                        # y -= y_speed
            else:
                x -= x_speed
                y -= y_speed
                sonidoChoqueLadrillo()
        # Para monitoriar juego:
        print(tablero)
        print(x, y)
        # Colocando sonido, cuando el personaje choque en el muro
        # pygame.mixer.music.load("Música y Sonido/SaltosoMovi.mpeg")
        # pygame.mixer.music.play()

        # mapaJuego() #Llamamos función del mapa
        # Jugador Movible
        jugadorMovible()
        # Bloques movibles
        bloqueMovible()

        # Diamantes
        diamante()
        # Actualizar pantalla
        pygame.display.flip()

        # Para la rapidez de movilidad del jugador
        clock.tick(6)  # Con valor 6, funciona bien.Probar con otros valores

# ==================================

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  pantalla.blit(img, (x, y))

# load button images
start_img = pygame.image.load('Imagenes/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Imagenes/exit_btn.png').convert_alpha()

# create button instances
start_button = button.Button(180, 300, start_img, 0.7)
exit_button = button.Button(450, 300, exit_img, 0.7)

# Bucle del juego
run = True
while run:

    pantalla.fill((202, 228, 241))
    TEXT_COL = (255, 255, 255)
    font = pygame.font.SysFont("arialblack", 40)
    font1 = pygame.font.SysFont("arialblack", 30)
    draw_text("SOKOBAN", font, TEXT_COL, 300, 80)
    draw_text("PRESIONE 'START' PARA JUGAR Y",font1,TEXT_COL,140,150)
    draw_text("PRESIONE 'EXIT' PARA SALIR ",font1,TEXT_COL,180,200)

    if start_button.draw(pantalla):
        #print('START')
        sokoban()
    if exit_button.draw(pantalla):
        #print('EXIT')
        run = False
    pygame.display.flip()
    # Controlador de eventos
    
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
                
  


