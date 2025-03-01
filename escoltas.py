from vehiculos import Vehiculos

class Escoltas(Vehiculos):
    def __init__(self,codigo):
        super().__init__(5, 5)
        self.codigo=codigo
        self.peso=250

    def get_ataque(self):
        return super().get_ataque()
    def get_defensa(self):
        return super().get_defensa()
    def get_codigo(self):
        return self.codigo