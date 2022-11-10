class Vehiculo:
    color = 'white'
    whells = '\'29'
    doors = str(2)

class Coche(Vehiculo):
    velocidad = '200 Km/h'
    cilindrada = '1.5Lts'

volkswagen = Coche()

print(f'Este modelo de Volkswagen viene en color: {volkswagen.color}.\nTiene unas ruedas: {volkswagen.whells} Pulgadas.\nViene con {volkswagen.doors} puertas.\nSu velocidad Max. es de: {volkswagen.velocidad}.\nY, con una cilindrada de: {volkswagen.cilindrada}.\nGracias por su visita!.')