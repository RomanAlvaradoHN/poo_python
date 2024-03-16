import os

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.marcha = "parqueo"

    def encender(self, encender_motor):
        self.encendido = encender_motor

    def estado(self):
        os.system("cls")
        print("marca: ", self.marca)
        print("modelo: " , self.modelo)
        print("endendido: ", self.encendido)
        print("marcha: ", self.marcha)
        

class Moto(Vehiculo):
    pass

moto1 = Moto("Genesis", "GN125")
moto1.estado()

