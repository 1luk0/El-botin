from vehiculos import Vehiculos

class Ladrones(Vehiculos):
    def __init__(self, ataque, defensa):
        super().__init__(ataque, defensa)

    def get_ataque(self):
        return super().get_ataque()
    def get_defensa(self):
        return super().get_defensa()