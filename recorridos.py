import random
from control import Control
from grafond import Grafond

class Dinero:
  
    #saber si un centro tiene el dinero suficiente para hacer un a ruta
    def hay(dinero):
        d1=Control.centro1.get_dinero_in()
        d2=Control.centro2.get_dinero_in()
        if d1 >= dinero and d2 >=dinero:
            return "ANY"
        elif d1 >=dinero:
            return "CO1"
        elif d2 >= dinero:
            return "CO2"
        else:
            raise ValueError
        
    def capacidad(dinero, vehiculo):
        cap= vehiculo.get_capacidad()
        if cap > dinero:
            raise ValueError
        else:
            return True
            

    #dice cual es el tamaño adecuado de vehiculo
    def tamaño_v(dinero):
        p1=Control.blindado_S1.get_capacidad()
        p2=Control.blindado_G1.get_capacidad()
        
        if dinero > p2:
            raise ValueError
        elif dinero > p1:
            return "GRANDE"
        else:
            return "PEQUEÑO"
        
    #que vehiculo puede hacer la ruta    
    def vehiculo_libre(centro,tamaño): 
        if centro == "CO1":
            if tamaño =="GRANDE":
                vehiculos= Control.vehiculos_blindados_inG
                for v in vehiculos:
                    if len(v.get_rutas()) == 0:
                        return v
            if tamaño == "PEQUEÑO":
                vehiculos= Control.vehiculos_blindados_in
                for v in vehiculos:
                    if len(v.get_rutas()) == 0:
                        return v
        if centro == "CO2":
            if tamaño =="GRANDE":
                vehiculos= Control.vehiculos_blindados_inG2
                for v in vehiculos:
                    if len(v.get_rutas()) == 0:
                        return v
            if tamaño == "PEQUEÑO":
                vehiculos= Control.vehiculos_blindados_in2
                for v in vehiculos:
                    if len(v.get_rutas()) == 0:
                        return v
                    
    #se llama para obtener el vehiculo                
    def elegir_vehiculo(self,centro,dinero):
       tamaño= self.tamaño_v(dinero)
       vehiculo= self.vehiculo_libre(centro,tamaño)
       return vehiculo     

                  
class Parada:
    
    def __init__(self,destino,dinero,tipo):
        self.destino=destino
        self.tipo=tipo
        self.dinero= dinero

    def get_codigo(self):
        return self.codigo

    # Setter para codigo
    def set_codigo(self, value):
        self.codigo = value

    def get_vehiculo(self):
        return self.vehiculo

    def set_vehiculo(self, value):
        self.vehiculo = value

    # Getter y setter para destino
    def get_destino(self):
        return self.destino

    def set_destino(self, value):
        self.destino = value

    # Getter y setter para dinero
    def get_dinero(self):
        return self.dinero

    def set_dinero(self, value):
        self.dinero = value

    # Getter y setter para tipo
    def get_tipo(self):
        return self.tipo

    def set_tipo(self, value):
        self.tipo = value

    # Getter y setter para tiempo
    def get_tiempo(self):
        return self.tiempo

    def set_tiempo(self, value):
        self.tiempo = value


class Recorrido:
    
    def __init__(self,paradas,tiempo):
        g= Grafond()
        grafo= g.inicialiazar()

        self.paradas= paradas
        self.recorrido=None
        ruta=[]
        self.dineroLlevar=0
        self.dineroRec=0
        dineroLlevar = 0
        dineroRec = 0

        #calcular la cantidad de dinero a llevar y recibir de las paradas
        for p in paradas:
            if p.get_tipo() == "Entregar":
                dineroLlevar += p.get_dinero()
                self.dineroLlevar = dineroLlevar
            if p.get_tipo() == "Recibir":
                dineroRec += p.get_dinero()
                self.dineroRec = dineroRec
        #ver si los centros tienen suficiente dinero
        try:
            centro = Dinero.hay(dineroLlevar)
             #ver si las cantidades de dinero pueden ser transportadas
            try:
                vlleva= Dinero.tamaño_v(dineroLlevar)
                vtrae=Dinero.tamaño_v(dineroRec)
                
                 #establecer el tamaño
                if vlleva == "GRANDE" or vlleva == "PEQUEÑO" and vtrae =="GRANDE" or vtrae == "PEQUEÑO":
                    if vlleva == "GRANDE" or vtrae == "GRANDE":
                        tamaño= "GRANDE"
                    else:
                        tamaño= "PEQUEÑO"

                    #obtener recorrido
                    for p in paradas:
                        ruta.append(p.get_destino())

                    #obtenemos el centro de op donde iniciamos
                    if centro == "ANY":
                        if tamaño == "GRANDE":
                            inicio= grafo.elejir_inicio(ruta,Control.blindado_G1)
                        if tamaño == "PEQUEÑO":
                            inicio= grafo.elejir_inicio(ruta,Control.blindado_S1)
                    else:
                        inicio=centro
                    
                    self.inicio= inicio

                    #obtener el vehiculo que va ha hacer la ruta
                    if dineroLlevar > dineroRec:
                        
                        v=Dinero.elegir_vehiculo(Dinero,inicio,dineroLlevar)
                    else:
                        v=Dinero.elegir_vehiculo(Dinero,inicio,dineroRec)
                        
                    #obtener el tiempo y la ruta mas corta para hacer todo el recorrido
                    self.vehiculo= v
                    
                    recorrido= grafo.obtener_ruta(ruta,v,tiempo,inicio,dineroRec)
                    if recorrido:
                        self.recorrido= recorrido
                        v.set_rutas(recorrido)
                        v.set_dinero_actual(dineroLlevar)
                        v.set_peso_actual(v.get_peso()+ dineroLlevar)
                    else:
                        self.recorrido=False
            except ValueError:
                print("el dinero excede la capacidad de los vehiculos")
        except ValueError:
            print("no hay la suficiente cantidad de dinero")

       
    def get_paradas(self):
        return self.paradas
    def get_vehiculo(self):
        return self.vehiculo
    def get_inicio(self):
        return self.inicio
    def get_recorrido(self):
        return self.recorrido
    def get_dineroLlevar(self):
        return self.dineroLlevar
    def get_dineroRec(self):
        return self.dineroRec


            

p1= Parada("CL1",10,"Entregar")
p2= Parada("CL7",20,"Recibir")
p3= Parada("CL2",30,"Recibir")

rec1=Recorrido([p1,p2,p3],100)
        


        


        



        
