# game_state.py
"""
Variables globales del estado del juego
"""
import random
from config_module import CANTIDAD_ENEMIGOS, VELOCIDAD_ENEMIGO, DESCENSO_ENEMIGO, ESTADO_INTRO, VIDAS_INICIALES, ANCHO_PANTALLA, ALTO_PANTALLA

# Variables globales del estado del juego
puntaje = 0
vidas = VIDAS_INICIALES  # Nueva variable para el sistema de vidas
estado_actual = ESTADO_INTRO  # Cambiar de ESTADO_MENU a ESTADO_INTRO
jugador_x = 268
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0
balas = []

# Nueva variable global para el nombre del jugador
nombre_jugador_actual = ""

# Variables de enemigos
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []

def inicializar_enemigos():
    """Inicializa las posiciones y velocidades de los enemigos"""
    global enemigo_x, enemigo_y, enemigo_x_cambio, enemigo_y_cambio

    enemigo_x.clear()
    enemigo_y.clear()
    enemigo_x_cambio.clear()
    enemigo_y_cambio.clear()

    for i in range(CANTIDAD_ENEMIGOS):
        enemigo_x.append(random.randint(0, ANCHO_PANTALLA - 64)) # Usar ANCHO_PANTALLA para límites correctos
        enemigo_y.append(random.randint(50, 200))
        enemigo_x_cambio.append(VELOCIDAD_ENEMIGO)
        enemigo_y_cambio.append(DESCENSO_ENEMIGO)

def reiniciar_juego():
    """Reinicia todas las variables del juego a su estado inicial"""
    global puntaje, vidas, jugador_x, jugador_y, jugador_x_cambio, jugador_y_cambio, balas, nombre_jugador_actual

    puntaje = 0
    vidas = VIDAS_INICIALES  # Reiniciar vidas
    jugador_x = 268
    jugador_y = 500
    jugador_x_cambio = 0
    jugador_y_cambio = 0
    balas.clear()
    inicializar_enemigos()
    nombre_jugador_actual = "" # Reiniciar el nombre del jugador al reiniciar el juego


def perder_vida():
    """Reduce las vidas del jugador en 1"""
    global vidas
    if vidas > 0:
        vidas -= 1
    return vidas

def obtener_vidas():
    """Obtiene las vidas actuales del jugador"""
    return vidas

def cambiar_estado(nuevo_estado):
    """Cambia el estado actual del juego"""
    global estado_actual
    estado_actual = nuevo_estado

def obtener_estado():
    """Obtiene el estado actual del juego"""
    return estado_actual

def establecer_nombre_jugador(nombre):
    """Establece el nombre del jugador actual."""
    global nombre_jugador_actual
    nombre_jugador_actual = nombre

def obtener_nombre_jugador():
    """Obtiene el nombre del jugador actual."""
    return nombre_jugador_actual

def resetear_posicion_jugador():
    """Restablece la posición del jugador a su posición inicial."""
    global jugador_x, jugador_y
    jugador_x = ANCHO_PANTALLA // 2 - 32 # Centrar el jugador (ANCHO_PANTALLA / 2 - ancho_jugador / 2)
    jugador_y = ALTO_PANTALLA - 100 # Un poco más arriba del fondo