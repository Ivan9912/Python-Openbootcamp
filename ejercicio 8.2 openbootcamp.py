"""
    En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle

def main():
    
    class Vehiculo:
        def __init__(self, modelo, año, color ):
            self.modelo = modelo
            self.año = año
            self.color = color
            
        def __str__(self):
            return f'Este vehículo modelo: {self.modelo} es del año {self.año} y viene del color {self.color}'
        
        def __repr__(self):
            """_Vehículo_
            """

    volkswagen = str(Vehiculo('Virtus Trendline', '2019', 'Azul Noche'))
    print(volkswagen)

    f = open('.\objVehiculo.bin', 'w+b')
    pickle.dump(volkswagen, f)
    #f.seek(0)
    f.close()
    
    t = open('.\objVehiculo.bin', 'r+b') 
    newVolkswagen = pickle.load(t)
    print(newVolkswagen)
    t.close()
    
if __name__=='__main__':
    main()