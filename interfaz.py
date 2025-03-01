import pygame
from control import Control
from grafo_ciudad import Grafo
from recorridos import Recorrido,Parada
from ladrones import Ladrones
import sys


pygame.init()
pygame.display.set_caption('EL BOTIN')
screen = pygame.display.set_mode((1250, 650))

grafo = Grafo()
control = Control()

paradas = []
recorridos = []

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

black = (0, 0, 0)
white = (255,255,255)

confirmaciones = False
ladrones_ingresado = False
ruta_ingresada = False
imagen = pygame.image.load('resources\imagenes\grafo.jpeg')


#--------------------FUENTES----------------------------------------------

fuente = pygame.font.Font(None, 24)
font_size = 22  # Cambia esto al tamaño de fuente que quieras
precisionF = pygame.font.Font(None, font_size)

font = pygame.font.Font(None, 25)
active_box = None
done = False
ataque = ''
defensa = ''
#--------------------------INPUTS-----------------------------------------------

# Configuración del input para "Dinero"
input_box1 = pygame.Rect(470, 100, 150, 20)
text1 = ''
input_text1 = pygame.font.Font(None, 22).render("Dinero ", True, (0, 0, 0))

# Configuración del input para "Tiempo"
input_box2 = pygame.Rect(470, 500, 150, 20)
text2 = ''
input_text2 = pygame.font.Font(None, 22).render("Tiempo ", True, (0, 0, 0))

# Configuración del input para "Ataque"
input_box3 = pygame.Rect(130, 500, 150, 20)
text3 = ''
input_text3 = pygame.font.Font(None, 22).render("Ataque ", True, (0, 0, 0))

# Configuración del input para "Defensa"
input_box4 = pygame.Rect(130, 550, 150, 20)
text4 = ''
input_text4 = pygame.font.Font(None, 22).render("Defensa ", True, (0, 0, 0))


#--------------------MENUS DESPLEGABLES----------------------------------------


#Configuración del menú "Grupos"
clientes = pygame.Rect(200, 100, 150, 20)
opciones_clientes = ["CL1", "CL2", "CL3", "CL4", "CL5", "CL6", "CL7", "CL8", "CL9"]
clientes_activo = False
cliente_seleccionado = None

acciones = pygame.Rect(470, 150, 150, 20)
opciones_acciones = ["Entregar", "Recibir"]
acciones_activo = False
acciones_seleccionado = None

#--------------------BOTONES-----------------------------------------------

# Configuración del botón "Ingresar rutas"
boton_ruta = pygame.Rect(470, 250, 140, 20)
border_width = 2
border_ruta = pygame.Rect(boton_ruta.left - border_width, boton_ruta.top - border_width, boton_ruta.width + 2*border_width, boton_ruta.height + 2*border_width)

boton_ladrones = pygame.Rect(130, 600, 140, 20)
border_ladrones = pygame.Rect(boton_ladrones.left - border_width, boton_ladrones.top - border_width, boton_ladrones.width + 2*border_width, boton_ladrones.height + 2*border_width)

boton_simular = pygame.Rect(1000, 100, 140, 20)
border_simular = pygame.Rect(boton_simular.left - border_width, boton_simular.top - border_width, boton_simular.width + 2*border_width, boton_simular.height + 2*border_width)

boton_recorrido = pygame.Rect(480, 550, 140, 20)
border_recorrido = pygame.Rect(boton_recorrido.left - border_width, boton_recorrido.top - border_width, boton_recorrido.width + 2*border_width, boton_recorrido.height + 2*border_width)

def mostrar_alerta_temporal(mensaje, duracion=3000):
    inicio_alerta = pygame.time.get_ticks()
    alerta_activa = True
    
    while alerta_activa:
        # Verificar si ha pasado el tiempo de duración
        if pygame.time.get_ticks() - inicio_alerta > duracion:
            alerta_activa = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        # Dibuja un rectángulo para la alerta
        alert_rect = pygame.Rect(720, 50, 400, 10)
        pygame.draw.rect(screen, WHITE, alert_rect)

        # Renderiza el mensaje de la alerta
        text_surf = font.render(mensaje, True, BLACK)
        text_rect = text_surf.get_rect(center=alert_rect.center)

        # Muestra el mensaje en la pantalla
        screen.blit(text_surf, text_rect)
        pygame.display.flip()

        # Limpia la pantalla después de que la alerta esté activa
        if not alerta_activa:
            screen.fill(BLACK)
            pygame.display.flip()

def dinero_contenedores(dinero):
        c1= Control.cont1.get_cap_dinero() 
        c2=Control.cont2.get_cap_dinero()   
        c3=Control.cont3.get_cap_dinero() 
        if dinero % c3 ==  0:
            return True
        elif (((dinero % c3)) % c2) == 0:
            return True
        elif (((dinero % c3) % c2)% c1 )==0:
            return True
        else:
            return False



#-----------------------PYGAME-----------------------------------------------------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if ruta_ingresada and ladrones_ingresado:
            if confirmaciones:
                grafo.dibujar_grafo(recorridos,ladrones)
                confirmaciones = False
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clientes.collidepoint(event.pos):
                clientes_activo = not clientes_activo
            elif clientes_activo:
                for i, option in enumerate(opciones_clientes):
                    if pygame.Rect(clientes.x, clientes.y + (i+1)*30, clientes.width, clientes.height).collidepoint(event.pos):
                        cliente_seleccionado = option
                        
                        clientes_activo = False
                        break
            
            if acciones.collidepoint(event.pos):
                acciones_activo = not acciones_activo
            elif acciones_activo:
                for i, option in enumerate(opciones_acciones):
                    if pygame.Rect(acciones.x, acciones.y + (i+1)*30, acciones.width, acciones.height).collidepoint(event.pos):
                        acciones_seleccionado = option
                        acciones_activo = False
                        break


            elif boton_ruta.collidepoint(event.pos):
                if cliente_seleccionado is not None and dinero is not '' and acciones_seleccionado:
                    if int(dinero) > 3000:
                         mostrar_alerta_temporal('El monto exede la capacidad máxima de envio')
                    else:
                        if dinero_contenedores(int(dinero)):
                            parada = Parada(cliente_seleccionado,int(dinero),acciones_seleccionado)
                            paradas.append(parada)
                            ruta_ingresada = True
                        else:
                            mostrar_alerta_temporal("Los valores deben ser multiplos de 50, 100 o 150")    
                else:
                    mostrar_alerta_temporal('Asegurate de llenar todos los campos')
                
            
            elif boton_recorrido.collidepoint(event.pos):
                if paradas and tiempo:  # Verifica que 'paradas' no esté vacía y 'tiempo' no esté vacío
                    recorrido = Recorrido(paradas, int(tiempo))
                    if recorrido.get_recorrido() is None:
                        mostrar_alerta_temporal("No es posible hacer el recorrido en ese tiempo")
                    elif recorrido.get_recorrido() is not False:
                        recorridos.append(recorrido)
                        #obtenemos el centro del que sale 
                        centro= Control.get_centro(Control,recorrido.get_inicio())
                        #le quitamos el dinero a llevar a el centro
                        centro.set_dinero_in(centro.get_dinero_in() - recorrido.get_dineroLlevar())
                        print('Este es el dinero que hay actualmente en el centro')
                        print(centro.get_dinero_in())
                        paradas = []  # Restablece 'paradas' a una lista vacía
                        ruta_ingresada = True
                    else:
                        mostrar_alerta_temporal("la capacidad de los centros se excede")
                else:
                    mostrar_alerta_temporal("No se han ingresado paradas o tiempo.")

            if boton_ladrones.collidepoint(event.pos):
                if ataque and defensa:
                    ladrones_ingresado = True
                    ladrones = Ladrones(ataque,defensa)
                else:
                    mostrar_alerta_temporal('Asegurate de llenar todos los campos')
            
            if boton_simular.collidepoint(event.pos):
                if not ruta_ingresada and not ladrones_ingresado:
                    mostrar_alerta_temporal('Asegurate de completar todos los datos')
                confirmaciones = True
            

            if input_box1.collidepoint(event.pos):
                active_box = 1
            elif input_box2.collidepoint(event.pos):
                active_box = 2
            elif input_box3.collidepoint(event.pos):
                active_box = 3
            elif input_box4.collidepoint(event.pos):
                active_box = 4

        if event.type == pygame.KEYDOWN:
            if active_box is not None:
                if event.key == pygame.K_RETURN:
                    if active_box == 1:
                        dinero = text1
                    elif active_box == 2:
                        tiempo = text2
                    elif active_box == 3:
                        ataque = text3
                    elif active_box == 4:
                        defensa = text4
                elif event.key == pygame.K_BACKSPACE:
                    if active_box == 1:
                        text1 = text1[:-1]
                    elif active_box == 2:
                        text2 = text2[:-1]
                    elif active_box == 3:
                        text3 = text3[:-1]
                    elif active_box == 4:
                        text4 = text4[:-1]
                else:
                    if active_box == 1:
                        text1 += event.unicode
                    elif active_box == 2:
                        text2 += event.unicode
                    elif active_box == 3:
                        text3 += event.unicode
                    elif active_box == 4:
                        text4 += event.unicode
            
            
        screen.fill((255, 255, 255))
        screen.blit(imagen, (800, 250))

            
        txt_surface1 = font.render(text1, True, (0, 0, 0))
        screen.blit(input_text1, (input_box1.x-70, input_box1.y+5))
        screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box1, 2)

        txt_surface2 = font.render(text2, True, (0, 0, 0))
        screen.blit(input_text2, (input_box2.x-70, input_box2.y+5))
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box2, 2)

        txt_surface3 = font.render(text3, True, (0, 0, 0))
        screen.blit(input_text3, (input_box3.x-70, input_box3.y+5))
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box3, 2)

        txt_surface4 = font.render(text4, True, (0, 0, 0))
        screen.blit(input_text4, (input_box4.x-70, input_box4.y+5))
        screen.blit(txt_surface4, (input_box4.x+5, input_box4.y+2))
        pygame.draw.rect(screen, (0, 0, 0), input_box4, 2)
        
    #--------------------CONFIGURACION DE LOS MENUS DESPLEGABLES-----------------------------------------

        pygame.draw.rect(screen, (0, 0, 0), clientes, 2)
        menu_clientes = precisionF.render("Clientes", True, (0, 0, 0))
        screen.blit(menu_clientes, (clientes.x-85, clientes.y+2))
        
        pygame.draw.rect(screen, (0, 0, 0), acciones, 2)
        menu_acciones = precisionF.render("Acciones", True, (0, 0, 0))
        screen.blit(menu_acciones, (acciones.x-85, acciones.y+2))

    #------------------------BOTONES--------------------------------------------

        pygame.draw.rect(screen, black, border_ruta)
        pygame.draw.rect(screen, white, boton_ruta)
        ingresar_ruta = font.render("Ingresar", True, (0, 0, 0))
        screen.blit(ingresar_ruta, (boton_ruta.x + 10, boton_ruta.y + 3))

        pygame.draw.rect(screen, black, border_ladrones)
        pygame.draw.rect(screen, white, boton_ladrones)
        ingresar_ladrones = font.render("Ingresar", True, (0, 0, 0))
        screen.blit(ingresar_ladrones, (boton_ladrones.x + 10, boton_ladrones.y + 3))

        pygame.draw.rect(screen, black, border_recorrido)
        pygame.draw.rect(screen, white, boton_recorrido)
        ingresar_recorrido = font.render("Ingresar", True, (0, 0, 0))
        screen.blit(ingresar_recorrido, (boton_recorrido.x + 10, boton_recorrido.y + 3))

        pygame.draw.rect(screen, black, border_simular)
        pygame.draw.rect(screen, white, boton_simular)
        simular = font.render("Simular", True, (0, 0, 0))
        screen.blit(simular, (boton_simular.x+35, boton_simular.y + 3))


    #----------------------------------TEXTOS---------------------------------------------

        txt_surface0 = pygame.font.Font(None, 35).render("Planificación de rutas", True, (0, 0, 0))
        screen.blit(txt_surface0, (70, 50))

        txt_surface1 = pygame.font.Font(None, 30).render("Estadisticas de los ladrones", True, (0, 0, 0))
        screen.blit(txt_surface1, (50, 425))

        txt_surface2 = pygame.font.Font(None, 30).render("Ingresar tiempo de la ruta", True, (0, 0, 0))
        screen.blit(txt_surface2, (400, 425))

        txt_surface2 = pygame.font.Font(None, 35).render("Mapa", True, (0, 0, 0))
        screen.blit(txt_surface2, (760, 225))

        txt_surface3 = pygame.font.Font(None, 30).render("Excepciones:", True, (0, 0, 0))
        screen.blit(txt_surface3, (570, 45))

    #--------------------CONFIGURACION DE LAS OPCIONES DE LOS MENUS-----------------------------------------
        
    # Dibujar las opciones del menú si el menú está activo
        if clientes_activo:
            for i, option in enumerate(opciones_clientes):
                option_rect = pygame.Rect(clientes.x, clientes.y + (i+1)*30, clientes.width, clientes.height)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 1)
                option_text = font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x+35, option_rect.y+1))
        
        if acciones_activo:
            for i, option in enumerate(opciones_acciones):
                option_rect = pygame.Rect(acciones.x, acciones.y + (i+1)*30, acciones.width, acciones.height)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 1)
                option_text = font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (option_rect.x+35, option_rect.y+1))

        pygame.display.flip()
pygame.quit()


