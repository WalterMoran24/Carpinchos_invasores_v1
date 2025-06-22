# input_nombre_module.py
"""
Módulo para manejar la entrada del nombre del jugador - Versión funcional corregida
"""
import pygame

# Variables globales para el estado del input
nombre_actual = ""
_cursor_visible = True
_tiempo_cursor = 0
MAX_LONGITUD_NOMBRE = 15

def inicializar_input():
    """Inicializa o resetea el input de nombre"""
    global nombre_actual, _cursor_visible, _tiempo_cursor
    nombre_actual = ""
    _cursor_visible = True
    _tiempo_cursor = 0

def manejar_evento_nombre(evento):
    """Maneja los eventos de entrada del nombre del jugador"""
    global nombre_actual
    
    if evento.type == pygame.TEXTINPUT:
        # Agregar el caracter escrito
        if len(nombre_actual) < MAX_LONGITUD_NOMBRE:
            # Solo agregar caracteres válidos (letras, números, espacios)
            if evento.text.isalnum() or evento.text == ' ':
                nombre_actual += evento.text
    
    elif evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_BACKSPACE:
            # Borrar último caracter
            nombre_actual = nombre_actual[:-1]
        elif evento.key == pygame.K_RETURN:
            # Confirmar nombre
            if len(nombre_actual.strip()) > 0:
                return True  # Nombre completado
    
    return False  # Continuar ingresando nombre

def actualizar_cursor(dt):
    """Actualiza la animación del cursor"""
    global _cursor_visible, _tiempo_cursor
    _tiempo_cursor += dt
    if _tiempo_cursor >= 500:  # Parpadear cada 500ms
        _cursor_visible = not _cursor_visible
        _tiempo_cursor = 0

def obtener_nombre():
    """Obtiene el nombre ingresado limpio"""
    nombre_limpio = nombre_actual.strip()
    return nombre_limpio if nombre_limpio else "ANONIMO"

def obtener_nombre_con_cursor():
    """Obtiene el nombre con el cursor para mostrar en pantalla"""
    cursor = "|" if _cursor_visible else " "
    return nombre_actual + cursor

def obtener_longitud_nombre():
    """Obtiene la longitud actual del nombre"""
    return len(nombre_actual)