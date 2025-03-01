from contenedor import Contenedor
class Clientes:
    def __init__(self,codigo):
        self.contenedor1= Contenedor(5,5)
        self.contenedor2=Contenedor(20,20)
        self.contenedor3=Contenedor(50,50)
        self.codigo= codigo
    
     # Getters
    def get_contenedor1(self):
        return self.contenedor1
    def get_contenedor2(self):
        return self.contenedor2
    def get_contenedor3(self):
        return self.contenedor3n
    def get_codigo(self):
        return self.codigo
    

 