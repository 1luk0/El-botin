class Vehiculos:

    def __init__(self,ataque,defensa):
        self.ataque = ataque
        self.defensa = defensa
    
     # Getters
    def get_ataque(self):
        return self.ataque

    def get_defensa(self):
        return self.defensa

    # Setters
    def set_ataque(self, ataque):
        self.ataque = ataque

    def set_defensa(self, defensa):
        self.defensa = defensa