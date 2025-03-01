from vehiculos import Vehiculos

class Blindados(Vehiculos):
    def __init__(self,codigo):
        super().__init__(10, 5)
        #kilos
        self.peso = 500
        #millones
        self.capacidad= 1000
        self.velocidad= 5
        self.escoltas= 1
        self.dinero_actual=0
        self.codigo=codigo
        self.rutas=[]
        self.peso_actual = 500
    #getters
    def get_ataque(self):
        return super().get_ataque()
    
    def get_defensa(self):
        return super().get_defensa()
    
    def get_peso(self):
        return self.peso
    
    def get_peso_actual(self):
        return self.peso_actual

    def get_capacidad(self):
        return self.capacidad
    
    def get_dinero_actual(self):
        return self.dinero_actual

    def get_velocidad(self):
        return self.velocidad
    
    def get_escoltas(self):
        return self.escoltas
    
    def get_codigo(self):
        return self.codigo
        
    def set_dinero_actual(self,dinero_actual):
        self.dinero_actual= dinero_actual
    
    def set_peso_actual(self,peso_actual):
        self.peso_actual= peso_actual   

    def get_rutas(self):
        return self.rutas
    
    def set_rutas(self,rutas):
        self.rutas=rutas
        
    def get_pesoTotal(self):
        total = self.get_capacidad()+ self.get_peso() + (self.get_escoltas() * 250)
        return total
    
