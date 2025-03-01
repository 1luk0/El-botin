from collections import deque
from control import Control
class Grafond:
    def __init__(self):
        self.vertices={}
        self.peso={"CL2":{"CL5":4300},"CO2":{"CL8":4300},"CL5":{"CL2":4300},"CL8":{"CO2":4300}}
        
    def Agregar_nodo(self,vertice):
        if vertice not in self.vertices:
            self.vertices[vertice]={}
     
    def Agregar_arista(self,v1,v2,peso):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][v2]=peso
            self.vertices[v2][v1]=peso

    def get_adyacent(self,v):
        return list(self.vertices[v])
        

    def dijkstra(self, v_inicial, vehiculo):
        distancias = {v: [float('inf'), []] for v in self.vertices}
        distancias[v_inicial] = [0, [v_inicial]]
        visitados = set()
        cola = [(0, v_inicial)]
        
        while cola:
            d_actual, v_actual = min(cola)
            cola.remove((d_actual, v_actual))
            
            if v_actual not in visitados:
                visitados.add(v_actual)
                
                for ady, peso in self.vertices[v_actual].items():
                    n_dist = d_actual + peso
                    n_camino = distancias[v_actual][1] + [ady]
                    
                    if n_dist < distancias[ady][0] and (v_actual in self.peso.keys() and ady in self.peso.keys()):
                        if ady in self.peso[v_actual]:
                            if self.peso[v_actual][ady] >= vehiculo.get_pesoTotal():
                                distancias[ady] = [n_dist, n_camino]
                                cola.append((n_dist, ady))
                        else:
                            distancias[ady] = [n_dist, n_camino]
                            cola.append((n_dist, ady))  
                    elif n_dist < distancias[ady][0]:
                        distancias[ady] = [n_dist, n_camino]
                        cola.append((n_dist, ady))
    
        return distancias

     
    
    def test(metodo,v_inicial,v_final):
        return ()#costo minimo de vi a vf#
    
    def elejir_inicio(self,paradas,vehiculo):
        
        dij1= self.dijkstra("CO1", vehiculo)
        dij2= self.dijkstra("CO2", vehiculo)
        #miramos dede que centro se llega mas rapido al primer cliente
        if dij1[paradas[0]][0] < dij2[paradas[0]][0]:
            return "CO1"
        else:
            return "CO2"
    
    def obtener_ruta(self,paradas,vehiculo,tiempo,centro,dinero):
        dij= self.dijkstra(centro,vehiculo)
        #agregamos la ruta mas corta a nuestra ruta
        ruta = (dij[paradas[0]][1])
        #actualizamos el valor de la distancia 
        distancia=(dij[paradas[0]][0])

        #recorremos las paradas
        for i in range( len(paradas)-1):
            #hallamos el dijtra  de la siguiente parada
            dij1= self.dijkstra(paradas[i],vehiculo)
            #agregamos la ruta a la otra parada 
            r=(dij1[paradas[i+1]][1])
            r.pop(0)
            ruta += (r)
            distancia += dij1[paradas[i+1]][0]

        #miramos a que centro deberia regresar
        if centro== "CO1":
            if len(Control.centro1.get_vehiculos_in()) + 1 > Control.centro1.get_capacidad_vehiculos():
                centro= "CO2"
                if len(Control.centro2.get_vehiculos_in()) + 1 > Control.centro2.get_capacidad_vehiculos():
                    return False
            if Control.centro1.get_dinero_in() + dinero > Control.centro1.get_capacidad_dinero():
                centro= "CO2"
                if Control.centro2.get_dinero_in() + dinero > Control.centro2.get_capacidad_dinero():
                    return False
            if Control.centro1.get_escoltas_in() + 2 > Control.centro1.get_capacidad_escoltas():
                centro= "CO2"
                if Control.centro2.get_escoltas_in() + 2 > Control.centro2.get_capacidad_escoltas():
                    return False
        if centro== "CO2":
            if len(Control.centro2.get_vehiculos_in()) + 1 > Control.centro2.get_capacidad_vehiculos():
                centro= "CO1"
                if len(Control.centro1.get_vehiculos_in()) + 1 > Control.centro1.get_capacidad_vehiculos():
                    return False
            if Control.centro2.get_dinero_in() + dinero > Control.centro2.get_capacidad_dinero():
                centro= "CO1"
                if Control.centro1.get_dinero_in() + dinero > Control.centro1.get_capacidad_dinero():
                    return False
            if Control.centro2.get_escoltas_in() + 2 > Control.centro2.get_capacidad_escoltas():
                centro= "CO1"
                if Control.centro1.get_escoltas_in() + 2 > Control.centro1.get_capacidad_escoltas():
                    return False
        
        #agregar el regreso al centro
        dij2= self.dijkstra(ruta[-1],vehiculo)
        x=dij2[centro][1]
        x.pop(0)
        ruta += (x)
        
        if distancia > tiempo:
            raise ValueError
        
        return distancia,ruta

    def inicialiazar(self):
        #iniciaizacion grafo
        g = Grafond()
        g.Agregar_nodo('CL1')
        g.Agregar_nodo('CL2')
        g.Agregar_nodo('CL3')
        g.Agregar_nodo('CL4')
        g.Agregar_nodo('CL5')
        g.Agregar_nodo('CL6')
        g.Agregar_nodo('CL7')
        g.Agregar_nodo('CL8')
        g.Agregar_nodo('CL9')
        g.Agregar_nodo('CO1')
        g.Agregar_nodo('CO2')

        g.Agregar_arista('CL1','CO1',5)
        g.Agregar_arista('CL1','CL4',20)
        g.Agregar_arista('CO1','CL2',10)
        g.Agregar_arista('CO1','CL4',20)
        g.Agregar_arista('CL4','CL5',30)
        g.Agregar_arista('CL2','CL5',15)
        g.Agregar_arista('CL2','CL3',5)
        g.Agregar_arista('CL3','CL6',20)
        g.Agregar_arista('CL4','CO2',10)
        g.Agregar_arista('CL7','CO2',20)
        g.Agregar_arista('CL1','CL7',40)
        g.Agregar_arista('CO2','CL6',40)
        g.Agregar_arista('CO2','CL8',10)
        g.Agregar_arista('CL8','CL9',20)
        g.Agregar_arista('CL9','CL6',30)

        return g







