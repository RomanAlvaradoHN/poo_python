class Vehiculo():
    largo_chasis = 350
    ancho_chasis = 180
    ruedas = 4
    encendido = False

    def encender(self, encender_motor):
        self.encendido = encender_motor
        self.estado()

        
    def estado(self):
        if(self.encendido):
            print("vehículo encendido")
        else:
            print("vehículo apagado")
   
carro1 = Vehiculo()
carro2 = Vehiculo()

