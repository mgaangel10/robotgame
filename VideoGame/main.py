import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from model.robot import Robot
import random

pygame.init()
ventana = pygame.display.set_mode((990, 780))
fondo = pygame.image.load("imagenes/fondo_cesped.jpg").convert()
fondo = pygame.transform.scale(fondo, (990, 780))
x=random.uniform(0,690)
y=random.uniform(0,480)
mi_robot = Robot(x, y, 990, 780)
mi_robot.imagen = pygame.transform.scale(mi_robot.imagen, (40, 60))
font = pygame.font.Font(None, 36)  # Tamaño de la fuente

game_running = True
while game_running:
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        mi_robot.move(-1,0)  # mover a la izquierda
        mi_robot.imagen = pygame.image.load("imagenes/steve_left.png")
        mi_robot.imagen=pygame.transform.scale(mi_robot.imagen, (30, 60))
    if keys[K_RIGHT]:
        mi_robot.move(1, 0)  # mover a la derecha
        mi_robot.imagen = pygame.image.load("imagenes/steve_right.png")
        mi_robot.imagen=pygame.transform.scale(mi_robot.imagen, (30, 60))
    if keys[K_UP]:
        mi_robot.move(0, -1)  # mover hacia arriba
        mi_robot.imagen = pygame.image.load("imagenes/steve_back.png")
        mi_robot.imagen=pygame.transform.scale(mi_robot.imagen, (40, 60))
    if keys[K_DOWN]:
        mi_robot.move(0, 1)  # mover hacia abajo
        mi_robot.imagen = pygame.image.load("imagenes/steve_front.png")
        mi_robot.imagen=pygame.transform.scale(mi_robot.imagen, (40, 60))

    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    #si el robot tiene 0 de vida se cierra el juego
    if mi_robot.salud == 0:
        game_running = False
    #esto ajusta el fondo de pantalla
    ventana.blit(fondo, (0, 0))




    ventana.blit(mi_robot.imagen, mi_robot.cuerpoRobot)

    #esto muestra el texto de la ventana donde se ve la vida del robot
    vida_texto = font.render(f'Vida: {mi_robot.salud}', True, (0, 0, 0))
    #esto es donde esta situado el marcador de la vida
    ventana.blit(vida_texto, (10, 10))

    pygame.display.flip()

pygame.quit()
