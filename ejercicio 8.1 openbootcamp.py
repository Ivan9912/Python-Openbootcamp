"""
    En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""
    
def main():

    with open('archivo.txt', 'w', encoding='utf-8') as fW:
        fW.write('Creo y escrivo esto en el archivo.txt\n')
        fW.close()
    with open('archivo.txt', 'r+', encoding='utf-8') as fR:
        fR.readlines()
        fR.write('Entro a archivo.txt por segunda vez.\n')
        fR.seek(0)
        data = fR.read()
        print(data)
        fR.close()
        
if __name__ == '__main__':
    main()