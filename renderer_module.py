import pygame
import input_nombre_module  # Importación del módulo funcional
from config_module import ANCHO_PANTALLA, ALTO_PANTALLA, CANTIDAD_ENEMIGOS
import game_state_module
import puntajes_module


def mostrar_puntaje(pantalla, recursos, x, y):
    """Muestra el puntaje actual en pantalla"""
    texto = recursos['fuente'].render(f'Puntaje: {game_state_module.puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def mostrar_vidas(pantalla, recursos, x, y):
    """Muestra las vidas actuales en pantalla"""
    vidas = game_state_module.obtener_vidas()
    texto = recursos['fuente'].render(f'Vidas: {vidas}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def dibujar_enemigo(pantalla, recursos, x, y):
    """Dibuja un enemigo en la posición especificada"""
    # Verificar que existan imágenes de enemigo y usar índice seguro
    if 'img_enemigo' in recursos and len(recursos['img_enemigo']) > 0:
        pantalla.blit(recursos['img_enemigo'][0], (x, y))

def dibujar_bala(pantalla, recursos, x, y):
    """Dibuja una bala en la posición especificada"""
    if 'img_bala' in recursos:
        pantalla.blit(recursos['img_bala'], (x, y))

def mostrar_menu(pantalla, recursos):
    """Muestra el menú principal del juego"""
    if 'fondo_menu' in recursos:
        pantalla.blit(recursos['fondo_menu'], (0, 0))

    # Título
    if 'fuente_titulo' in recursos:
        titulo = recursos['fuente_titulo'].render("Carpinchos Invasores", True, (255, 255, 255))
        titulo_rect = titulo.get_rect(center=(ANCHO_PANTALLA//2, 100))
        pantalla.blit(titulo, titulo_rect)

    # Opciones del menú
    if 'fuente_menu' in recursos:
        opciones = [
            ("PRESIONA ENTER PARA JUGAR", 300),
            ("PRESIONA 'R' PARA VER RANKING", 360),
            ("PRESIONA ESC PARA SALIR", 420)
        ]
        
        for texto, y_pos in opciones:
            opcion = recursos['fuente_menu'].render(texto, True, (255, 255, 255))
            opcion_rect = opcion.get_rect(center=(ANCHO_PANTALLA//2, y_pos))
            pantalla.blit(opcion, opcion_rect)

    # Controles
    if 'fuente_controles' in recursos:
        controles_titulo = recursos['fuente_controles'].render("Controles:", True, (255, 255, 255))
        controles_titulo_rect = controles_titulo.get_rect(center=(ANCHO_PANTALLA//2, 500))
        pantalla.blit(controles_titulo, controles_titulo_rect)

        controles = recursos['fuente_controles'].render("Flechas: Mover, Espacio: Disparar", True, (255, 255, 255))
        controles_rect = controles.get_rect(center=(ANCHO_PANTALLA//2, 530))
        pantalla.blit(controles, controles_rect)

def mostrar_game_over(pantalla, recursos):
    """Muestra la pantalla de Game Over"""
    if 'img_game_over' in recursos:
        pantalla.blit(recursos['img_game_over'], (0, 0))

    # Mensaje principal
    if 'fuente_titulo' in recursos:
        mensaje = recursos['fuente_titulo'].render("¡GAME OVER!", True, (255, 0, 0))
        mensaje_rect = mensaje.get_rect(center=(ANCHO_PANTALLA//2, ALTO_PANTALLA//2 - 50))
        pantalla.blit(mensaje, mensaje_rect)

    # Puntaje final
    if 'fuente_menu' in recursos:
        puntaje_final = recursos['fuente_menu'].render(f"Puntaje Final: {game_state_module.puntaje}", True, (255, 255, 255))
        puntaje_final_rect = puntaje_final.get_rect(center=(ANCHO_PANTALLA//2, ALTO_PANTALLA//2 + 20))
        pantalla.blit(puntaje_final, puntaje_final_rect)

        # Opciones
        opciones_texto = [
            ("ENTER - Jugar de nuevo", 440),
            ("ESC - Menú principal", 480)
        ]
        
        for texto, y_pos in opciones_texto:
            opcion = recursos['fuente_menu'].render(texto, True, (255, 255, 255))
            opcion_rect = opcion.get_rect(center=(ANCHO_PANTALLA//2, y_pos))
            pantalla.blit(opcion, opcion_rect)

    # Mensaje sobre vidas
    if 'fuente_controles' in recursos:
        texto_vidas = recursos['fuente_controles'].render("Te quedaste sin vidas!", True, (255, 100, 100))
        vidas_rect = texto_vidas.get_rect(center=(ANCHO_PANTALLA//2, 380))
        pantalla.blit(texto_vidas, vidas_rect)

def mostrar_ingreso_nombre(pantalla, recursos):
    """Muestra la pantalla para que el jugador ingrese su nombre"""
    if 'img_game_over' in recursos:
        pantalla.blit(recursos['img_game_over'], (0, 0))

    # Título
    if 'fuente_titulo' in recursos:
        titulo = recursos['fuente_titulo'].render("¡Nuevo Record!", True, (255, 255, 0))
        titulo_rect = titulo.get_rect(center=(ANCHO_PANTALLA // 2, 100))
        pantalla.blit(titulo, titulo_rect)

    # Instrucción y nombre
    if 'fuente_menu' in recursos:
        instruccion = recursos['fuente_menu'].render("Ingresa tu nombre:", True, (255, 255, 255))
        instruccion_rect = instruccion.get_rect(center=(ANCHO_PANTALLA // 2, 200))
        pantalla.blit(instruccion, instruccion_rect)

        # Obtener el nombre actual
        nombre_actual = input_nombre_module.obtener_nombre()
        texto_nombre = recursos['fuente_menu'].render(nombre_actual, True, (0, 255, 0))
        texto_nombre_rect = texto_nombre.get_rect(center=(ANCHO_PANTALLA // 2, 280))
        pantalla.blit(texto_nombre, texto_nombre_rect)

        # Cursor parpadeante
        nombre_con_cursor = input_nombre_module.obtener_nombre_con_cursor()
        if "|" in nombre_con_cursor:
            cursor_pos_x = texto_nombre_rect.x + texto_nombre.get_width() + 5
            pygame.draw.line(pantalla, (255, 255, 255), 
                           (cursor_pos_x, texto_nombre_rect.y),
                           (cursor_pos_x, texto_nombre_rect.y + texto_nombre_rect.height), 2)

    # Mensaje de confirmación
    if 'fuente_controles' in recursos:
        mensaje_confirmar = recursos['fuente_controles'].render("ENTER para confirmar / ESC para cancelar", True, (200, 200, 200))
        mensaje_confirmar_rect = mensaje_confirmar.get_rect(center=(ANCHO_PANTALLA // 2, 400))
        pantalla.blit(mensaje_confirmar, mensaje_confirmar_rect)

def mostrar_ranking(pantalla, recursos):
    """Muestra la pantalla de ranking de puntajes"""
    if 'fondo_menu' in recursos:
        pantalla.blit(recursos['fondo_menu'], (0, 0))

    # Título
    if 'fuente_titulo' in recursos:
        titulo = recursos['fuente_titulo'].render("RANKING TOP 5", True, (255, 255, 255))
        titulo_rect = titulo.get_rect(center=(ANCHO_PANTALLA // 2, 80))
        pantalla.blit(titulo, titulo_rect)

    # Mostrar puntajes
    if 'fuente_menu' in recursos:
        top_puntajes = puntajes_module.obtener_top_puntajes()
        y_offset = 180
        
        if not top_puntajes:
            no_scores_text = recursos['fuente_menu'].render("No hay puntajes registrados.", True, (255, 255, 0))
            no_scores_rect = no_scores_text.get_rect(center=(ANCHO_PANTALLA // 2, y_offset))
            pantalla.blit(no_scores_text, no_scores_rect)
        else:
            for i, (nombre, puntaje) in enumerate(top_puntajes):
                texto_ranking = recursos['fuente_menu'].render(f"{i+1}. {nombre}: {puntaje}", True, (255, 255, 255))
                ranking_rect = texto_ranking.get_rect(center=(ANCHO_PANTALLA // 2, y_offset + i * 50))
                pantalla.blit(texto_ranking, ranking_rect)

        # Opciones
        opcion_regresar = recursos['fuente_menu'].render("ENTER para jugar / ESC para volver al Menú", True, (255, 255, 255))
        regresar_rect = opcion_regresar.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA - 80))
        pantalla.blit(opcion_regresar, regresar_rect)

def renderizar_juego(pantalla, recursos):
    """Renderiza el juego cuando está en estado JUGANDO"""
    # Fondo
    if 'fondo' in recursos:
        pantalla.blit(recursos['fondo'], (0, 0))

    # Dibujar enemigos
    for i in range(CANTIDAD_ENEMIGOS):
        dibujar_enemigo(pantalla, recursos, game_state_module.enemigo_x[i], game_state_module.enemigo_y[i])

    # Dibujar balas
    for bala in game_state_module.balas:
        dibujar_bala(pantalla, recursos, bala['x'], bala['y'])

    # Dibujar jugador
    if 'img_jugador' in recursos:
        pantalla.blit(recursos['img_jugador'], (game_state_module.jugador_x, game_state_module.jugador_y))

    # Mostrar UI
    mostrar_puntaje(pantalla, recursos, 10, 10)
    mostrar_vidas(pantalla, recursos, ANCHO_PANTALLA - 150, 10)