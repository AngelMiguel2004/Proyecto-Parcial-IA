# Miguel Ángel Jiménez 23-EISN-2-010
import pygame
from Scripts.constantes import *

# Clase base para objetos animados en el juego
class AnimateObj(pygame.sprite.Sprite):
    def __init__(self, callback=None):
        # Inicializa el objeto animado
        super(AnimateObj, self).__init__()
        self.index = 0
        self.image = None
        self.images = []
        self.patterndictionary = {}
        self.pattern = []
        self.rect = None
        self.cbAnimate = callback
        self.color = None
        self.patternkey = None

    # Agrega un patrón de animación al diccionario
    def addpattern(self, name, array):
        self.patterndictionary.update({name: array})

    # Establece el patrón de animación actual
    def setpattern(self, pattern):
        self.pattern = self.patterndictionary[pattern]
        if self.image is None:
            self.image = self.images[self.pattern[0]]
        self.patternkey = pattern

    # Actualiza la animación del objeto
    def update(self):
        self.index += 1
        if self.index >= len(self.pattern):
            if self.cbAnimate is not None:
                self.cbAnimate(self)
            self.index = 0
        self.image = self.images[self.pattern[self.index]]

    def draw(self):
        # Método de dibujo (no implementado)
        pass

    # Cambia el color del objeto animado
    def setcolor(self, color):
        self.color = color
        for image in self.images:
            pixelArray = pygame.PixelArray(image)
            pixelArray.replace(WHITE, color)

    # Mueve la posición del objeto animado
    def moveposition(self, x, y):
        self.rect.x += x
        self.rect.y += y
