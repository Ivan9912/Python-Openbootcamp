"""
    En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce 

def main():
    print('Agrega un número que será tomado como máximo.\nEjemplo 0 - número')
    inN1 = input()
    inN = inN1.isdigit()
    if inN:
        if inN > 0:
            inN = int(inN1)
            numerosList = list(range(inN))
            numerosList = filter((lambda x: x%2), numerosList)
            numerosList = list(numerosList)
            numerosList = reduce((lambda a, b: a + b), numerosList)
            print(f'La suma de todos los números impares de 0 al \'{inN}\' es: {numerosList}')
        else:
            print(f'\'{inN}\' es un número negativo o cero.\nVuelva a intentar.\n')
            main()
    else:
            print(f'\'{inN1}\' es una cadena de texto.\nVuelva a intentar.\n')
            main()

if __name__ == '__main__':
    main()