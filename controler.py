from grafo_ciudad import Grafo_ciudad

class Controler:
    def __init__(self, ruta_imagen):
        self.grafo_ciudad = Grafo_ciudad([], [], [], [])
        self.ruta_imagen = ruta_imagen

    def dibujar_grafo(self):
        self.grafo_ciudad.dibujar_grafo(self.ruta_imagen)

grafo = Controler('resources/imagenes/WhatsApp Image 2024-05-25 at 6.38.07 PM.jpeg')
grafo.dibujar_grafo()