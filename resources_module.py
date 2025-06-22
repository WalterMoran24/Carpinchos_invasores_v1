# resources.py
"""
Carga y manejo de recursos del juego (imágenes, sonidos, fuentes)
"""
import pygame
from pygame import mixer
from config_module import ANCHO_PANTALLA, ALTO_PANTALLA, CANTIDAD_ENEMIGOS, ARCHIVOS, VOLUMEN_MUSICA
import os

def cargar_recursos():
    """Carga todas las imágenes, sonidos y fuentes del juego"""
    recursos = {}
    
    # Imágenes
    recursos['img_intro'] = pygame.image.load(ARCHIVOS['img_intro'])
    recursos['icono'] = pygame.image.load(ARCHIVOS['icono'])
    recursos['fondo'] = pygame.image.load(ARCHIVOS['fondo'])
    recursos['fondo_menu'] = pygame.transform.scale(
        pygame.image.load(ARCHIVOS['fondo_menu']), (ANCHO_PANTALLA, ALTO_PANTALLA)
    )
    recursos['img_game_over'] = pygame.transform.scale(
        pygame.image.load(ARCHIVOS['img_game_over']), (ANCHO_PANTALLA, ALTO_PANTALLA)
    )
    recursos['img_jugador'] = pygame.image.load(ARCHIVOS['img_jugador'])
    recursos['img_bala'] = pygame.image.load(ARCHIVOS['img_bala'])
    
    # Imágenes de enemigos
    recursos['img_enemigo'] = []
    for i in range(CANTIDAD_ENEMIGOS):
        recursos['img_enemigo'].append(pygame.image.load(ARCHIVOS['img_enemigo']))
    
    # Sonidos
    recursos['sonido_bala'] = mixer.Sound(ARCHIVOS['sonido_bala'])
    recursos['sonido_colision'] = mixer.Sound(ARCHIVOS['sonido_colision'])
    
    # Sonido de vida perdida (opcional - si no existe el archivo, se usará el de colisión)
    if os.path.exists(ARCHIVOS['sonido_vida_perdida']):
        recursos['sonido_vida_perdida'] = mixer.Sound(ARCHIVOS['sonido_vida_perdida'])
    else:
        print("Archivo de sonido 'vida_perdida.mp3' no encontrado. Se usará el sonido de colisión.")
    
    # Fuentes
    recursos['fuente'] = pygame.font.Font(ARCHIVOS['fuente'], 32)
    recursos['fuente_titulo'] = pygame.font.Font(ARCHIVOS['fuente'], 48)
    recursos['fuente_menu'] = pygame.font.Font(ARCHIVOS['fuente'], 32)
    recursos['fuente_final'] = pygame.font.Font(ARCHIVOS['fuente'], 40)
    recursos['fuente_controles'] = pygame.font.Font(ARCHIVOS['fuente'], 24)
    
    return recursos

def configurar_audio():
    """Configura la música de fondo"""
    mixer.music.load(ARCHIVOS['musica'])
    mixer.music.set_volume(VOLUMEN_MUSICA)
    mixer.music.play(-1)