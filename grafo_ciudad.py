import math
import random
import time
import numpy as np
import pygame
from math import sqrt
from vehiculos_blindados import Blindados
from vehiculos_blindados_g import Blindados_G
from control import Control

class Grafo:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    # Función para calcular la distancia entre dos puntos
    def calcular_distancia(punto1, punto2):
        return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

    @staticmethod
    def CalcDis(Dup1, Dup2):
        return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup2.y - Dup1.y), 2))  

    def dibujar_grafo(self, recorridos , ladrones):
        pygame.init()
        pygame.mixer.init()

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1250, 650))
        cantidad_paradas = 0
        cantidad_recorridos = 0

        fuente = pygame.font.Font(None, 24)
        pygame.display.set_caption("SIMULACION DE LA CIUDAD")

        # Variables
        recorrido_hecho = False
        running = True

        # Configuración de recuadros
        color_fondo = (255, 255, 255)
        color_borde = (0, 0, 0)
        radio_esquina = 20

        recuadros = [
            pygame.Rect(880, 30, 300, 140)
        ]

        ladrones_b = False

        # Imágenes
        imagen_carro_valores_pequeno = pygame.image.load('resources/imagenes/cit-768x467.png')
        imagen_carro_valores_pequeno = pygame.transform.scale(imagen_carro_valores_pequeno, (50, 30))

        imagen_motos = pygame.image.load('resources/imagenes/cdde43744808b8575781efc93f41e94a_9f4f9389eaea3928.png')
        imagen_motos = pygame.transform.scale(imagen_motos, (50, 30))

        imagen_carro_valores_grande = pygame.image.load('resources/imagenes/Brinks-Truck.png')
        imagen_carro_valores_grande = pygame.transform.scale(imagen_carro_valores_grande, (50, 30))

        imagen_ladrones = pygame.image.load('resources/imagenes/dt-125.png')
        imagen_ladrones = pygame.transform.scale(imagen_ladrones, (50, 30))

        imagen_explosion = pygame.image.load('resources/imagenes/explosion.png')
        imagen_explosion = pygame.transform.scale(imagen_explosion, (50, 50))

        imagen_ganadora = pygame.image.load('resources/imagenes/nos robaron!! (1).png')
        imagen_ganadora = pygame.transform.scale(imagen_ganadora, (200, 200))

        imagen_perdedora = pygame.image.load('resources/imagenes/nos robaron!!.png')
        imagen_perdedora = pygame.transform.scale(imagen_perdedora, (200, 200))


        sonido_explosion = pygame.mixer.Sound('resources/sounds/y2mate.com-Ametralladora-Efecto-de-Sonido-HD.wav')
        sonido_explosion.set_volume(1)

        # Configuración de aristas y nodos
        vertices_G = ['CL1', 'CO1', 'CL2', 'CL3', 'CL4', 'CL5', 'CL6', 'CL7', 'CO2', 'CL8', 'CL9']
        aristas_G = [('CL1', 'CO1', 5), ('CO1', 'CL2', 10), ('CL2', 'CL3', 5), ('CL4', 'CL1', 20), ('CL4', 'CO1', 20), ('CL4', 'CL5', 30),
                     ('CL4', 'CO2', 10), ('CL5', 'CL2', 10), ('CL3', 'CL6', 5), ('CL7', 'CL1', 40),
                     ('CL7', 'CO2', 20), ('CO2', 'CL6', 40), ('CO2', 'CL8', 10), ('CL8', 'CL9', 20), ('CL9', 'CL6', 30)]
        ubica = {'CL1': (4, 13), 'CO1': (8, 13), 'CL2': (15, 13), 'CL3': (20, 13), 'P1': (15, 11), 'P2': (20, 11),
                 'CL4': (8, 7), 'CL5': (15, 7), 'CL6': (20, 7), 'CL7': (4, 4), 'CO2': (8, 4), 'CL8': (8, 1), 'CL9': (15, 1)}

        ancho_ventana = 800
        alto_ventana = 600
        escala_x = ancho_ventana / max(x for x, y in ubica.values())
        escala_y = alto_ventana / max(y for y, y in ubica.values())
        ubica = {nodo: (int(x * escala_x), int(y * escala_y)) for nodo, (x, y) in ubica.items()}

        screen.fill((255, 255, 255))

        # Dibujar nodos y aristas
        for arista in aristas_G:
            # Extraer solo los nodos de la arista para la comparación, ignorando el peso
            nodos_arista = (arista[0], arista[1])

            # Definir el color de la arista
            if nodos_arista in [('CO1', 'CL4'), ('CO2', 'CL8'), ('CL5', 'CL6')] or nodos_arista in [('CL4', 'CO1'), ('CL8', 'CO2'), ('CL6', 'CL5')]:
                color_arista = (255, 0, 0)  # Rojo
            else:
                color_arista = (0, 0, 0)  # Negro

            # Dibujar la arista
            pygame.draw.line(screen, color_arista, ubica[arista[0]], ubica[arista[1]], 1)

        for nodo in vertices_G:
            pygame.draw.circle(screen, (0, 0, 255), ubica[nodo], 15)
            pygame.draw.circle(screen, (255, 255, 255), ubica[nodo], 13)
            texto = fuente.render(nodo, True, (0, 0, 0))
            screen.blit(texto, (ubica[nodo][0] - 15, ubica[nodo][1] - 9))
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Lista para almacenar los datos de cada vehículo
            datos_vehiculos = []
            
            # Inicializa los datos del vehículo aquí para cada recorrido
            for recorrido_actual in recorridos:
                recorrido = recorrido_actual.get_recorrido()[1]
                vehiculo_actual = recorrido_actual.get_vehiculo()

                datos_vehiculo = {
                    "nombre": vehiculo_actual.get_codigo(),
                    "ataque": vehiculo_actual.get_ataque(),
                    "defensa": vehiculo_actual.get_defensa(),
                    "dinero": vehiculo_actual.get_dinero_actual(),
                    "peso": vehiculo_actual.get_peso_actual()
                }

                datos_vehiculos.append(datos_vehiculo)

            # Dibuja los recuadros con los datos de cada vehículo
            for recuadro, datos in zip(recuadros, datos_vehiculos):
                pygame.draw.rect(screen, color_fondo, recuadro)
                pygame.draw.rect(screen, color_borde, recuadro, 2, border_radius=radio_esquina)

                textos = [
                    f"Nombre del vehículo: {datos['nombre']}",
                    f"Ataque: {datos['ataque']}",
                    f"Defensa: {datos['defensa']}",
                    f"Dinero: {datos['dinero']}",
                    f"Peso del vehiculo: {datos['peso']}",
                ]

                for i, texto in enumerate(textos):
                    texto_surface = fuente.render(texto, True, (0, 0, 0))
                    texto_x = recuadro.x + 10
                    texto_y = recuadro.y + (i * 25) + 10
                    screen.blit(texto_surface, (texto_x, texto_y))

            pygame.display.flip()

            if not recorrido_hecho:
                for recorrido_actual in recorridos:
                    recorrido = recorrido_actual.get_recorrido()[1]
                    vehiculo_actual = recorrido_actual.get_vehiculo()
                    cantidad_paradas = 0
                    for i in range(len(recorrido) - 1):
                        if i == len(recorrido)-2:
                            #sumar la plata al centro de llegada 
                            cent= Control.get_centro(Control, recorrido[len(recorrido)-1])
                            cent.set_dinero_in(cent.get_dinero_in() + vehiculo_actual.get_dinero_actual())
                            print('Este es el dinero que hay actualmente en el centro')
                            print(cent.get_dinero_in())
                        inicio = np.array(ubica[recorrido[i]])
                        fin = np.array(ubica[recorrido[i + 1]])
                        for j in range(1, 6):
                            screen_copy = screen.copy()
                            punto_intermedio = inicio + (fin - inicio) * (j / 6)

                            if isinstance(vehiculo_actual, Blindados):
                                time.sleep(0.2)
                                screen.blit(imagen_carro_valores_pequeno, (punto_intermedio[0] - 15, punto_intermedio[1] - 8))
                            if isinstance(vehiculo_actual, Blindados_G):
                                screen.blit(imagen_carro_valores_grande, (punto_intermedio[0] - 15, punto_intermedio[1] - 8))
                                time.sleep(0.4)

                            if isinstance(vehiculo_actual, Blindados):
                                num_escoltas = 1
                                for k in range(num_escoltas):
                                    angulo = 2 * math.pi * k / num_escoltas
                                    dx = 60 * math.cos(angulo)
                                    dy = 60 * math.sin(angulo)
                                    screen.blit(imagen_motos, (punto_intermedio[0] + dx - 5, punto_intermedio[1] + dy - 5))

                            if isinstance(vehiculo_actual, Blindados_G):
                                num_escoltas = 2
                                for k in range(num_escoltas):
                                    angulo = 2 * math.pi * k / num_escoltas
                                    dx = 60 * math.cos(angulo)
                                    dy = 60 * math.sin(angulo)
                                    
                                    screen.blit(imagen_motos, (punto_intermedio[0] + dx - 5, punto_intermedio[1] + dy - 5))
                            
                            pygame.display.flip()
                            screen.blit(screen_copy, (0, 0))
                        
                        if vehiculo_actual == self.vehiculo_robo(recorridos):
                            if not ladrones_b:
                                if recorrido[i+1] == self.lugarRobo(recorrido_actual.get_paradas()):
                                    time.sleep(5)
                                    sonido_explosion.play()
                                    num_escoltas = 3
                                    for k in range(num_escoltas):
                                        angulo = 2 * math.pi * k / num_escoltas
                                        dx = 60 * math.cos(angulo)
                                        dy = 60 * math.sin(angulo)
                                        screen.blit(imagen_explosion, (punto_intermedio[0] - 15, punto_intermedio[1] - 8))
                                        screen.blit(imagen_ladrones, (punto_intermedio[0] + dx - 5, punto_intermedio[1] + dy - 5))
                                    pygame.display.flip()
                                    screen.blit(screen_copy, (0, 0))
                                    
                                    ladrones_win = self.asalto(vehiculo_actual,ladrones.get_ataque(),ladrones.get_defensa())

                                    if ladrones_win:
                                            screen.blit(imagen_perdedora,(900,300))
                                    else:
                                        screen.blit(imagen_ganadora,(900,300))
                                    
                                    ladrones_b = True
                            

                        if recorrido[i + 1] == recorrido_actual.get_paradas()[cantidad_paradas].get_destino():
                            time.sleep(5)
                            
                            if cantidad_paradas < len(recorrido_actual.get_paradas())-1:
                                cantidad_paradas += 1
                            
                            
                            if recorrido_actual.get_paradas()[cantidad_paradas].get_tipo() == 'Entregar':
                                cambio_dinero = vehiculo_actual.get_dinero_actual() - recorrido_actual.get_paradas()[cantidad_paradas].get_dinero()
                                cambio_peso = vehiculo_actual.get_peso_actual() - recorrido_actual.get_paradas()[cantidad_paradas].get_dinero()

                                vehiculo_actual.set_peso_actual(cambio_peso)
                                vehiculo_actual.set_dinero_actual(cambio_dinero)

                            if recorrido_actual.get_paradas()[cantidad_paradas].get_tipo() == 'Recibir': 
                                cambio_dinero = vehiculo_actual.get_dinero_actual() + recorrido_actual.get_paradas()[cantidad_paradas].get_dinero()
                                recorrido_actual.get_paradas()[cantidad_paradas].set_dinero(cambio_dinero)
                                cambio_peso = vehiculo_actual.get_peso() + recorrido_actual.get_paradas()[cantidad_paradas].get_dinero()
                                
                                vehiculo_actual.set_peso_actual(cambio_peso)
                                vehiculo_actual.set_dinero_actual(cambio_dinero)
                                


                            datos_vehiculos = [
                                {"nombre": vehiculo_actual.get_codigo(), "ataque": vehiculo_actual.get_ataque(), "defensa": vehiculo_actual.get_defensa(), "dinero": vehiculo_actual.get_dinero_actual(), "peso": vehiculo_actual.get_peso_actual()},
                            ]

                            for recuadro, datos in zip(recuadros, datos_vehiculos):
                                pygame.draw.rect(screen, color_fondo, recuadro)
                                pygame.draw.rect(screen, color_borde, recuadro, 2, border_radius=radio_esquina)

                                textos = [
                                    f"Nombre del vehículo: {datos['nombre']}",
                                    f"Ataque: {datos['ataque']}",
                                    f"Defensa: {datos['defensa']}",
                                    f"Dinero: {datos['dinero']}",
                                    f"Peso del vehiculo: {datos['peso']}",
                                ]

                                for i, texto in enumerate(textos):
                                    texto_surface = fuente.render(texto, True, (0, 0, 0))
                                    texto_x = recuadro.x + 10
                                    texto_y = recuadro.y + (i * 25) + 10
                                    screen.blit(texto_surface, (texto_x, texto_y))
                            
                        

                        datos_vehiculos = [
                                {"nombre": vehiculo_actual.get_codigo(), "ataque": vehiculo_actual.get_ataque(), "defensa": vehiculo_actual.get_defensa(), "dinero": vehiculo_actual.get_dinero_actual(), "peso": vehiculo_actual.get_peso_actual()},
                            ]

                        for recuadro, datos in zip(recuadros, datos_vehiculos):
                            pygame.draw.rect(screen, color_fondo, recuadro)
                            pygame.draw.rect(screen, color_borde, recuadro, 2, border_radius=radio_esquina)

                            textos = [
                                f"Nombre del vehículo: {datos['nombre']}",
                                f"Ataque: {datos['ataque']}",
                                f"Defensa: {datos['defensa']}",
                                f"Dinero: {datos['dinero']}",
                                f"Peso del vehiculo: {datos['peso']}",
                            ]

                            for i, texto in enumerate(textos):
                                texto_surface = fuente.render(texto, True, (0, 0, 0))
                                texto_x = recuadro.x + 10
                                texto_y = recuadro.y + (i * 25) + 10
                                screen.blit(texto_surface, (texto_x, texto_y))

                            pygame.display.flip()


                    pygame.display.flip()
                    clock.tick(60)
                recorrido_hecho = True
                cantidad_recorridos += 1
                
        pygame.quit()


    #elegir el nodo en el que ocurrira el robo 
    def lugarRobo(self,paradas):
        rd=random.randint(0,len(paradas)-1)
        return paradas[rd].get_destino()
    
    def vehiculo_robo(self,recorridos):
        max_=0
        max_v=None
        for r in recorridos:
            v= r.get_vehiculo()
            actual= v.get_dinero_actual()
            if actual >= max_:
                max_=actual
                max_v=v

        return max_v

    #definir quien gana el asalto
    def asalto(self,vehiculo,ataque,defensa):
        #obtenemos datos 
        vA = vehiculo.get_ataque()
        vD = vehiculo.get_defensa()
        escoltas=vehiculo.get_escoltas()
        #aumentamos escoltas
        ataqueTotal= vA + 5 * escoltas
        defensaTotal= vD + 5 * escoltas
        #descontamos la defensa a el ataque 
        puntajeV= ataqueTotal-(int(defensa) * 3)
        puntajeL= (int(ataque) * 3) - defensaTotal
        vehiculo.set_defensa(vehiculo.get_defensa() - int(ataque)*3)

        if puntajeV >= puntajeL:
            return False
        else:
            #se descuenta la plata en el vehiculo
            return True

grafo = Grafo()
