#Módulo para manejar la introducción/historia del juego Carpinchos Invasores

import pygame
from config_module import (
    TIEMPO_INTRO, VELOCIDAD_TEXTO_INTRO, HISTORIA_INTRO, 
    ANCHO_PANTALLA, ALTO_PANTALLA, ESTADO_MENU, ARCHIVOS
)
import game_state_module

# Estado de la introducción
tiempo_total = 0
texto_mostrado = ""
completada = False

def cargar_imagen_intro():
    """Carga solo la imagen de intro y retorna un diccionario simple"""
    return {'img_intro': pygame.image.load(ARCHIVOS['img_intro'])}

def inicializar_intro():
    """Prepara la introducción desde el inicio"""
    global tiempo_total, texto_mostrado, completada
    tiempo_total = 0
    texto_mostrado = ""
    completada = False

def actualizar_intro(delta_time):
    """Actualiza cuánto texto mostrar según el tiempo que pasó"""
    global tiempo_total, texto_mostrado, completada
    
    if completada:
        return
    
    tiempo_total += delta_time
    todo_el_texto = "\n".join(HISTORIA_INTRO)
    caracteres_a_mostrar = int(tiempo_total / VELOCIDAD_TEXTO_INTRO)
    
    if caracteres_a_mostrar < len(todo_el_texto):
        texto_mostrado = todo_el_texto[:caracteres_a_mostrar]
    else:
        texto_mostrado = todo_el_texto
        if tiempo_total >= TIEMPO_INTRO + 4000:
            completada = True

def manejar_evento_intro(evento):
    """Detecta si el usuario quiere saltar la introducción"""
    global completada
    if evento.type == pygame.KEYDOWN:
        completada = True
        return True
    return False

def renderizar_intro(pantalla, recursos):
    """Dibuja la introducción en pantalla"""
    if 'img_intro' in recursos:
        pantalla.blit(recursos['img_intro'], (0, 0))
    else:
        pantalla.fill((0, 0, 0))
    
    # Texto con saltos de línea después de puntos
    lineas = [linea.strip() for linea in texto_mostrado.replace(';', '.\n').split('\n') if linea.strip()]
    
    #ALTO_PANTALLA // 2 = centro vertical de la pantalla
    #(len(lineas) * 20) = espacio total que ocuparán todas las líneas (20 píxeles por línea)
    #Al restar, el texto queda centrado verticalmente en la pantalla
    # Centrar texto verticalmente
    y_inicio = ALTO_PANTALLA // 2 - (len(lineas) * 20)
    for i, linea in enumerate(lineas): #Recorre cada línea de texto con su índice (i = 0, 1, 2...)
        texto_surface = recursos['fuente_menu'].render(linea, True, (0, 0, 0))
        #Convierte el texto en una imagen (surface) usando la fuente del menú
        #True = texto suavizado (antialiasing)
        #(0, 0, 0) = color negro
        texto_rect = texto_surface.get_rect(center=(ANCHO_PANTALLA // 2, y_inicio + i * 40))
        #Crea un rectángulo para posicionar el texto
        #center= = centra horizontalmente en el medio de la pantalla
        #y_inicio + i * 40 = cada línea se dibuja 40 píxeles más abajo que la anterior
        pantalla.blit(texto_surface, texto_rect)
        #Dibuja el texto en la pantalla en la posición calculada


    
    # Instrucciones para continuar
    if tiempo_total > 2000: #Verifica si han pasado más de 2000 milisegundos (2 segundos) desde que comenzó la introducción
        instruccion = recursos['fuente_controles'].render("Presiona cualquier tecla para continuar", True, (0, 0, 0))
        #Convierte el texto de instrucción en una imagen (surface)
        #Usa la fuente fuente_controles (probablemente más pequeña que la del texto principal)
        #True = texto suavizado
        #(0, 0, 0) = color negro
        rect_instruccion = instruccion.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA - 50))
        #Crea un rectángulo para posicionar las instrucciones
        #center=(ANCHO_PANTALLA // 2, ...) = centra horizontalmente
        #ALTO_PANTALLA - 50 = posiciona a 50 píxeles del borde inferior de la pantalla
        pantalla.blit(instruccion, rect_instruccion)
        #Dibuja las instrucciones en la pantalla



def intro_completada():
    """Dice si la introducción ya terminó"""
    return completada

def finalizar_intro():
    """Termina la introducción y va al menú"""
    game_state_module.cambiar_estado(ESTADO_MENU)

def debe_cambiar_a_menu():
    """Dice si hay que cambiar al menú principal"""
    return completada
#debe_cambiar_a_menu() SÍ se usa - verifica si hay que cambiar al menú
#finalizar_intro() SÍ se usa - ejecuta el cambio de estado al menú
#intro_completada() NO se usa directamente en main, pero es funcionalmente idéntica a debe_cambiar_a_menu()

#Observación: Las funciones intro_completada() y debe_cambiar_a_menu()
#hacen exactamente lo mismo (ambas retornan completada).
#Podrías eliminar una de ellas para simplificar el código.
#O si las mantienes por claridad semántica, está bien también.