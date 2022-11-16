"""
    En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle
import Coche as c

def main():
     
    volkswagen = c.Vehiculo('Virtus Trendline', '2019', 'Azul Noche')
    
    print(volkswagen)

    f = open('.\objVehiculo.bin', 'w+b')
    pickle.dump(volkswagen, f)
        #f.seek(0)
    f.close()
        
    t = open('.\objVehiculo.bin', 'r+b') 
    newVolkswagen = pickle.load(t)
    print(newVolkswagen)
    t.close()
    
if __name__=='__main__': #si agrego esto, si o si debo de convertir la clase en un string, sino no me lo permite
     main()