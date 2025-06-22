import pygame #Esto importa la librería Pygame, que se usa para crear juegos y gráficos interactivos.
import random
import math
from pygame import mixer

#Inicializa pygame
pygame.init()

#agregar musica

mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)
#Crea la pantalla
pantalla = pygame.display.set_mode((800,600))# el argumento es una tupla

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10

#mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}',True, (255,255,255))
    pantalla.blit(texto,(x,y))


#Titulo e icono:
pygame.display.set_caption("Carpinchos invasores") #titulo ventana
icono = pygame.image.load("capybara.png") #cargar icono
pygame.display.set_icon(icono) #mostrar icono


# Cargar la imagen de fondo
fondo = pygame.image.load("Fondo.jpg")


#Variables jugador:
img_jugador = pygame.image.load("happy.png")
jugador_x = 268
jugador_y = 536
jugador_x_cambio = 0



#Variables enemigo:
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

#Variables enemigo:
for i in range (cantidad_enemigos):
    img_enemigo.append(pygame.image.load("carpincho.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)



#Variables de la bala:
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True, (255,255,255))
    pantalla.blit(mi_fuente_final,(60, 200))

#detectar colisiones:
def colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else:
        return False

def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x +16 ,y + 10))
#Loop del juego
se_ejecuta = True
while se_ejecuta: #Este bucle mantiene el juego en ejecución hasta que el usuario lo cierre.
    pantalla.blit(fondo, (0, 0))



    #iterar eventos:
    for evento in pygame.event.get():
        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)


        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    # Dibujar la imagen de fondo


    #Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    #Mantener jugador dentro de los bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    #Modificar ubicacion del enemigo
    for i in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[i] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[i] += enemigo_x_cambio[i]

        #Mantener dentro de los bordes
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.3
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -0.3
            enemigo_y[i] += enemigo_y_cambio[i]

        colision = colisiones(enemigo_x[i], enemigo_y[i] ,bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[i] = random.randint(0,736)
            enemigo_y[i] = random.randint(50,200)
        enemigo(enemigo_x[i],enemigo_y[i],i)


    #Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)
    #actualizar
    pygame.display.flip()