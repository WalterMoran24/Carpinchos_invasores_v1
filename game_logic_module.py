# game_logic_module.py
"""
Lógica principal del juego: movimiento, colisiones, balas
"""
import math
import random
from config_module import (
    VELOCIDAD_BALA, LIMITE_JUGADOR_X, LIMITE_JUGADOR_Y, 
    VELOCIDAD_ENEMIGO, DISTANCIA_COLISION_BALA, 
    DISTANCIA_COLISION_JUGADOR, ESTADO_GAME_OVER, CANTIDAD_ENEMIGOS,
    ESTADO_INGRESO_NOMBRE
)
import game_state_module
import puntajes_module

def crear_bala(x, y):
    """Crea una nueva bala en la posición especificada"""
    return {'x': x + 16, 'y': y + 10, 'activa': True}

def actualizar_balas():
    """Actualiza la posición de todas las balas y elimina las que salen de pantalla"""
    balas_a_eliminar = []
    
    for i, bala in enumerate(game_state_module.balas):
        bala['y'] -= VELOCIDAD_BALA
        if bala['y'] < -10:
            balas_a_eliminar.append(i)
    
    # Eliminar balas fuera de pantalla (en orden inverso para evitar problemas de índices)
    for i in reversed(balas_a_eliminar):
        game_state_module.balas.pop(i)

def detectar_colision(x1, y1, x2, y2, distancia_minima=DISTANCIA_COLISION_BALA):
    """Detecta si hay colisión entre dos objetos usando distancia euclidiana"""
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return distancia < distancia_minima

def actualizar_jugador():
    """Actualiza la posición del jugador y mantiene límites de pantalla"""
    game_state_module.jugador_x += game_state_module.jugador_x_cambio
    game_state_module.jugador_y += game_state_module.jugador_y_cambio
    
    # Mantener jugador dentro de los límites de pantalla
    if game_state_module.jugador_x <= 0:
        game_state_module.jugador_x = 0
    elif game_state_module.jugador_x >= LIMITE_JUGADOR_X:
        game_state_module.jugador_x = LIMITE_JUGADOR_X
    
    if game_state_module.jugador_y <= 0:
        game_state_module.jugador_y = 0
    elif game_state_module.jugador_y >= LIMITE_JUGADOR_Y:
        game_state_module.jugador_y = LIMITE_JUGADOR_Y

def manejar_colision_jugador(recursos):
    """Maneja cuando el jugador pierde una vida"""
    vidas_restantes = game_state_module.perder_vida()
    
    # Reproducir sonido de vida perdida si está disponible
    if 'sonido_vida_perdida' in recursos:
        recursos['sonido_vida_perdida'].play()
    else:
        recursos['sonido_colision'].play()
    
    # Si no quedan vidas, verificar si califica para top puntajes
    if vidas_restantes <= 0:
        # Verificar si el puntaje califica para el ranking
        if puntajes_module.es_top_puntaje(game_state_module.puntaje):
            game_state_module.cambiar_estado(ESTADO_INGRESO_NOMBRE)
        else:
            game_state_module.cambiar_estado(ESTADO_GAME_OVER)
        game_state_module.jugador_x_cambio = 0
        game_state_module.jugador_y_cambio = 0
    else:
        # Si quedan vidas, resetear posición del jugador
        game_state_module.resetear_posicion_jugador()
        # Limpiar balas para dar un momento de respiro
        game_state_module.balas.clear()

def actualizar_enemigos(recursos):
    """Actualiza la posición de todos los enemigos y maneja colisiones"""
    for i in range(CANTIDAD_ENEMIGOS):
        # Si el enemigo llega abajo, el jugador pierde una vida
        if game_state_module.enemigo_y[i] > 500:
            manejar_colision_jugador(recursos)
            # Reposicionar el enemigo
            game_state_module.enemigo_x[i] = random.randint(0, 736)
            game_state_module.enemigo_y[i] = random.randint(50, 200)
            # Si el juego terminó, no continuar procesando
            if game_state_module.obtener_estado() in [ESTADO_GAME_OVER, ESTADO_INGRESO_NOMBRE]:
                break
            continue
        
        # Mover enemigo horizontalmente
        game_state_module.enemigo_x[i] += game_state_module.enemigo_x_cambio[i]
        
        # Cambiar dirección y descender cuando toca los bordes
        if game_state_module.enemigo_x[i] <= 0:
            game_state_module.enemigo_x_cambio[i] = VELOCIDAD_ENEMIGO
            game_state_module.enemigo_y[i] += game_state_module.enemigo_y_cambio[i]
        elif game_state_module.enemigo_x[i] >= 736:
            game_state_module.enemigo_x_cambio[i] = -VELOCIDAD_ENEMIGO
            game_state_module.enemigo_y[i] += game_state_module.enemigo_y_cambio[i]
        
        # Verificar colisión con balas
        balas_a_eliminar = []
        for j, bala in enumerate(game_state_module.balas):
            if detectar_colision(game_state_module.enemigo_x[i], game_state_module.enemigo_y[i], bala['x'], bala['y']):
                recursos['sonido_colision'].play()
                balas_a_eliminar.append(j)
                game_state_module.puntaje += 1
                game_state_module.enemigo_x[i] = random.randint(0, 736)
                game_state_module.enemigo_y[i] = random.randint(50, 200)
                break
        
        # Eliminar balas que colisionaron
        for j in reversed(balas_a_eliminar):
            game_state_module.balas.pop(j)
        
        # Verificar colisión con jugador
        if detectar_colision(
            game_state_module.enemigo_x[i], game_state_module.enemigo_y[i], 
            game_state_module.jugador_x, game_state_module.jugador_y, 
            DISTANCIA_COLISION_JUGADOR
        ):
            manejar_colision_jugador(recursos)
            # Reposicionar el enemigo que colisionó
            game_state_module.enemigo_x[i] = random.randint(0, 736)
            game_state_module.enemigo_y[i] = random.randint(50, 200)
            # Si el juego terminó, salir del bucle
            if game_state_module.obtener_estado() in [ESTADO_GAME_OVER, ESTADO_INGRESO_NOMBRE]:
                break

def actualizar_juego(recursos):
    """Actualiza toda la lógica del juego cuando está en estado JUGANDO"""
    actualizar_jugador()
    actualizar_enemigos(recursos)
    actualizar_balas()