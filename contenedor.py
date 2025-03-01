class Contenedor:
    def __init__(self,peso,cap_dinero):
        #kilos
        self.peso=peso
        #millones
        self.cap_dinero=cap_dinero

    def get_cap_dinero(self):
        return self.cap_dinero
    
    def get_peso(self):
        return self.peso
    
    def set_cap_dinero(self,cap_dinero):
        self.cap_dinero= cap_dinero

    def set_peso(self,peso):
        self.peso= peso
    