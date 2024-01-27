import pygame

class Muros:
    def __init__(self):
        # Carga las imágenes
        self.muro = pygame.transform.scale(pygame.image.load("imagenes/lava.png"), (50, 50))
        self.agua = pygame.transform.scale(pygame.image.load("imagenes/corazon.png"), (50, 50))
        self.bomba = pygame.transform.scale(pygame.image.load("imagenes/corazon.png"), (50, 50))
        self.diamante = pygame.transform.scale(pygame.image.load("imagenes/corazon.png"), (50, 50))
        self.traje_agua = pygame.transform.scale(pygame.image.load("imagenes/corazon.png"), (50, 50))
        self.camino = pygame.transform.scale(pygame.image.load("imagenes/camino.png"), (50, 50))  # Imagen para los espacios vacíos

        # Crea un diccionario para mapear los caracteres a las imágenes
        self.imagenes = {'M': self.muro, 'A': self.agua, 'B': self.bomba, 'D': self.diamante, 'T': self.traje_agua, ' ': self.camino}

    def dibujar(self, pantalla, mapa):
        # Recorre el mapa y dibuja las imágenes correspondientes
        for y, linea in enumerate(mapa):
            for x, caracter in enumerate(linea.strip()):
                if caracter in self.imagenes:
                    pantalla.blit(self.imagenes[caracter], (x*50, y*50))  # Ajusta el tamaño de las celdas del mapa a 50x50
