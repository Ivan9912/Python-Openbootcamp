import pickle

def main():
    
    class Juguete:
        nombre = ''
        precio = 0.0
        
        def __init__ (self, nombre, precio):
            self.precio = precio
            self.nombre = nombre
        
        def getNombre(self):
            return self.nombre
    
    j1 = Juguete('Potato', 10.5)
    
    f = open('.\Pruebas\datos.bin', 'wb')
    pickle.dump(j1, f)
    f.close()
    
    
if __name__ == '__main__':
    main()