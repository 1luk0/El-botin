
class Centros:
    def __init__(self,capacidad_vehiculos,vehiculos_in,vehicuos_inG,capacidad_dinero,dinero_in,clientes,escoltas_in,capacidad_escoltas):
        self.capacidad_vehiculos = capacidad_vehiculos
        self.vehiculos_in = vehiculos_in
        self.capacidad_dinero = capacidad_dinero
        self.dinero_in = dinero_in
        self.clientes = clientes
        self.escoltas_in = escoltas_in
        self.capacidad_escoltas= capacidad_escoltas
        self.vehiculos_inG= vehicuos_inG
    
    # Getters
    def get_capacidad_vehiculos(self):
        return self.capacidad_vehiculos

    def get_vehiculos_in(self):
        return self.vehiculos_in
    
    def get_vehiculos_inG(self):
        return self.vehiculos_inG

    def get_capacidad_dinero(self):
        return self.capacidad_dinero

    def get_dinero_in(self):
        return self.dinero_in

    def get_clientes(self):
        return self.clientes

    def get_escoltas_in(self):
        return self.escoltas_in
    def get_capacidad_escoltas(self):
        return self.capacidad_escoltas


    # Setters
    def set_capacidad_vehiculos(self, capacidad_vehiculos):
        self.capacidad_vehiculos = capacidad_vehiculos

    def set_vehiculos_in(self, vehiculos_in):
        self.vehiculos_in = vehiculos_in

    def set_vehiculos_in(self, vehiculos_inG):
        self.vehiculos_inG = vehiculos_inG

    def set_capacidad_dinero(self, capacidad_dinero):
        self.capacidad_dinero = capacidad_dinero

    def set_dinero_in(self, dinero_in):
        self.dinero_in = dinero_in

    def set_clientes(self, clientes):
        self.clientes = clientes

    def set_escoltas_in(self, escoltas_in):
        self.escoltas_in = escoltas_in
    def set_capacidad_escoltas(self, capacidad_escoltas):
        self.capacidad_escoltas = capacidad_escoltas
