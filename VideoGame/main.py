import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from model.robot import Robot
from model.Muros import Muros  # Asegúrate de que la clase Muros esté en un archivo llamado muros.py
import os


pygame.init()
ventana = pygame.display.set_mode((1330, 680))


mi_robot = Robot(300, 240, 1330, 680)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))

font = pygame.font.Font(None, 36)  # Tamaño de la fuente

# Crea una instancia de la clase Muros
muros = Muros()

# Abre el archivo del mapa
with open('C:/Users/mgaan/OneDrive/Documentos/robotgame/mapa.txt', 'r') as f:
    next(f)
    mapa = f.readlines()



game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mi_robot.move(-10, 0)#mover a la izquierda
            elif event.key == K_RIGHT:
                mi_robot.move(10, 0)  #mover a la derecha
            elif event.key == K_UP:
                mi_robot.move(0, -10)  #mover hacia arriba
            elif event.key == K_DOWN:
                mi_robot.move(0, 10)  #mover hacia abajo

    #si el robot tiene 0 de vida se cierra el juego
    if mi_robot.salud == 0:
        game_running = False

    #esto ajusta el fondo de pantalla


    # Dibuja los muros
    muros.dibujar(ventana, mapa)

    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    #esto muestra el texto de la ventana donde se ve la vida del robot
    vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255, 0, 0))
    #esto es donde esta situado el marcador de la vida
    ventana.blit(vida_texto, (10, 10))

    pygame.display.flip()

pygame.quit()
