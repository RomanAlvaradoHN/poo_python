import os

class Carro():
    def desplazamiento(self):
        print("Me deplazo utilizando 4 ruedas \n\n")

class Moto():
    def desplazamiento(self):
        print("Me deplazo utilizando 2 ruedas \n\n")

class Camion():
    def desplazamiento(self):
        print("Me deplazo utilizando 6 ruedas \n\n")
    

carro = Carro()
carro.desplazamiento()

moto = Moto()
moto.desplazamiento()

camion = Camion()
camion.desplazamiento()