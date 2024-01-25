import time

import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from model.robot import Robot, Lava
import random

pygame.init()
ejex= 50
ejey=50
ventana = pygame.display.set_mode((990, 780))

fondo = pygame.image.load("imagenes/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (990, 780))
#x=random.uniform(0,690)
#y=random.uniform(0,480)

lava = pygame.image.load("imagenes/lava.png")
lava = pygame.transform.scale(lava,(ejex,ejey))
lava1 = Lava(ejex,ejey)

mi_robot = Robot(300, 300, 990, 780)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (50, 50))
font = pygame.font.Font(None, 36)  # Tamaño de la fuente

game_running = True
while game_running:
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        mi_robot.move(-10,0)  # mover a la izquierda

    if keys[K_RIGHT]:
        mi_robot.move(10, 0)  # mover a la derecha

    if keys[K_UP]:
        mi_robot.move(0, -10)  # mover hacia arriba
    if keys[K_DOWN]:
        mi_robot.move(0, 10)  # mover hacia abajo

    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    #si el robot tiene 0 de vida se cierra el juego
    if mi_robot.salud == 0:
        game_running = False
    #esto ajusta el fondo de pantalla
    ventana.blit(fondo, (0, 0))


    for i in range(100,250):
        ventana.blit(lava,(i,250))
    lava1.colision(mi_robot)
    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    #esto muestra el texto de la ventana donde se ve la vida del robot
    vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (255, 0, 0))
    #esto es donde esta situado el marcador de la vida
    ventana.blit(vida_texto, (10, 10))

    pygame.display.flip()

pygame.quit()
