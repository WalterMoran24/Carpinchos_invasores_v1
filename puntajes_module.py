# puntajes_module.py
"""
Módulo para manejar puntajes del juego Carpinchos Invasores
Maneja la carga, guardado y ordenamiento de puntajes sin usar clases ni try/except
"""
import os

ARCHIVO_PUNTAJES = "puntajes.txt"

def cargar_puntajes():
    """Carga los puntajes desde el archivo. Si no existe, retorna lista vacía"""
    puntajes = []
    
    if os.path.exists(ARCHIVO_PUNTAJES):
        archivo = open(ARCHIVO_PUNTAJES, 'r', encoding='utf-8')
        lineas = archivo.readlines()
        archivo.close()
        
        for linea in lineas:
            linea = linea.strip()
            if linea and ',' in linea:
                partes = linea.split(',')
                if len(partes) == 2:
                    nombre = partes[0].strip()
                    puntaje_str = partes[1].strip()
                    # Verificar que el puntaje sea un número válido
                    if puntaje_str.isdigit():
                        puntaje = int(puntaje_str)
                        puntajes.append([nombre, puntaje])
    
    return puntajes

def guardar_puntajes(puntajes):
    """Guarda la lista de puntajes en el archivo"""
    archivo = open(ARCHIVO_PUNTAJES, 'w', encoding='utf-8')
    for entrada in puntajes:
        nombre = entrada[0]
        puntaje = entrada[1]
        archivo.write(f"{nombre},{puntaje}\n")
    archivo.close()

def ordenar_puntajes(puntajes):
    """Ordena los puntajes de mayor a menor usando bubble sort (sin usar sorted())"""
    n = len(puntajes)
    
    # Bubble sort - ordenar por puntaje (índice 1) de mayor a menor
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntajes[j][1] < puntajes[j + 1][1]:
                # Intercambiar
                temp = puntajes[j]
                puntajes[j] = puntajes[j + 1]
                puntajes[j + 1] = temp
    
    return puntajes

def agregar_puntaje(nombre, puntaje):
    """Agrega un nuevo puntaje y mantiene solo los top 5"""
    # Cargar puntajes existentes
    puntajes = cargar_puntajes()
    
    # Agregar el nuevo puntaje
    puntajes.append([nombre, puntaje])
    
    # Ordenar de mayor a menor
    puntajes = ordenar_puntajes(puntajes)
    
    # Mantener solo los top 5
    if len(puntajes) > 5:
        puntajes = puntajes[:5]
    
    # Guardar los puntajes actualizados
    guardar_puntajes(puntajes)
    
    return puntajes

def obtener_top_puntajes():
    """Obtiene los top 5 puntajes ordenados"""
    puntajes = cargar_puntajes()
    puntajes = ordenar_puntajes(puntajes)
    
    # Retornar solo los top 5
    if len(puntajes) > 5:
        return puntajes[:5]
    return puntajes

def limpiar_nombre(nombre):
    """Limpia y valida el nombre del jugador"""
    nombre = nombre.strip()
    
    # Si está vacío, usar nombre por defecto
    if not nombre:
        return "ANONIMO"
    
    # Limitar longitud
    if len(nombre) > 15:
        nombre = nombre[:15]
    
    # Eliminar caracteres problemáticos (comas y saltos de línea)
    nombre = nombre.replace(',', '').replace('\n', '').replace('\r', '')
    
    # Convertir a mayúsculas para consistencia
    return nombre.upper()

def es_top_puntaje(puntaje):
    """Verifica si un puntaje califica para el top 5"""
    puntajes = obtener_top_puntajes()
    
    # Si tenemos menos de 5 puntajes, siempre califica
    if len(puntajes) < 5:
        return True
    
    # Si el puntaje es mayor que el más bajo del top 5, califica
    puntaje_mas_bajo = puntajes[-1][1]  # El último después de ordenar
    return puntaje > puntaje_mas_bajo