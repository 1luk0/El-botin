from vehiculos_blindados import Blindados
from centros_de_operacion import Centros
from vehiculos_blindados_g import Blindados_G
from escoltas import Escoltas
from clientes import Clientes
from contenedor import Contenedor

class Control:

    cont1= Contenedor(50,50)
    cont2= Contenedor(100,100)
    cont3= Contenedor(150,150)
    #vehiculos bindados pequeños
    blindado_S1= Blindados("BlS01")
    blindadoP_S2=Blindados("BLS02")
    blindadoP_S3=Blindados("BLS03")
    blindadoP_S4=Blindados("BLS04")
    blindadoP_S5=Blindados("BLS05")
    blindadoP_S6=Blindados("BLS06")
    
    #vehiculos blindados grandes
    blindado_G1=Blindados_G("BlG01")
    blindado_G2=Blindados_G("BlG02")
    blindado_G3=Blindados_G("BlG03")
    blindado_G4=Blindados_G("BlG04")
    blindado_G5=Blindados_G("BlG05")
    blindado_G6=Blindados_G("BlG06")
    blindado_G7=Blindados_G("BlG07")
    blindado_G8=Blindados_G("BlG08")
    #escoltas
    # escolta1=Escoltas("ES01")
    # escolta2=Escoltas("ES02")
    # escolta3=Escoltas("ES03")
    # escolta4=Escoltas("ES04")
    # escolta5=Escoltas("ES05")
    # escolta6=Escoltas("ES06")
    # escolta7=Escoltas("ES07")
    # escolta8=Escoltas("ES08")
    # escolta9=Escoltas("ES09")
    # escolta10=Escoltas("ES010")
    # escolta11=Escoltas("ES011")
    # escolta12=Escoltas("ES012")
    
    #lista con los vehiculos
    vehiculos_blindados_in=[blindado_S1,blindadoP_S2,blindadoP_S3]
    vehiculos_blindados_in2=[blindadoP_S4,blindadoP_S5,blindadoP_S6]
    vehiculos_blindados_inG=[blindado_G1,blindado_G2,blindado_G3,blindado_G4]
    vehiculos_blindados_inG2=[blindado_G5,blindado_G6,blindado_G7,blindado_G8]
   

    #clientes
    cliente1=Clientes("CL1")
    cliente2=Clientes("CL2")
    cliente3=Clientes("CL3")
    cliente4=Clientes("CL4")
    cliente5=Clientes("CL5")
    cliente6=Clientes("CL6")
    cliente7=Clientes("CL7")
    cliente8=Clientes("CL8")
    cliente9=Clientes("CL9")

    clientes=[cliente1,cliente2,cliente3,cliente4,cliente5,cliente6,cliente7,cliente8,cliente9]
    
    #centros de operacion

    centro1= Centros(15,vehiculos_blindados_in,vehiculos_blindados_inG,60000,45000,clientes,6,12)
    centro2=Centros(18,vehiculos_blindados_in2,vehiculos_blindados_inG2,70000,30000,clientes,6,12)
    
    def get_centro(self,id):
        if id== "CO1":
            return self.centro1
        elif id== "CO2":
            return self.centro2




