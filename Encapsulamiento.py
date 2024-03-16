import os

class Vehiculo():
    encendido = False

    def encender(self, encender_motor):
        if(encender_motor):
            self.encendido = self.chequeo_interno()
            self.estado()

    def estado(self):
        os.system("cls")

        if(self.encendido):
            print("vehículo encendido \n\n")
        else:
            print("vehículo apagado \n\n")
        
    def chequeo_interno(self):
        en_neutral = False

        if(en_neutral):
            return True
        else:
            return False
   
carro1 = Vehiculo()