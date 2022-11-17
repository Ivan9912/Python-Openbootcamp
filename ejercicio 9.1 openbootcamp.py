"""
        Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""
paisesIn = input("ingrese nombre de paises separados por una \',\' y que no se repitan. Por favor: ")
paisesIn = paisesIn.title()
paisesIn = paisesIn.split(',')
paisesIn = set(paisesIn) #set() quita elementos repetidos. Pero queda un diccionario.
paisesIn = sorted(paisesIn) #ordena albabeticamente y queda una lista como salida.
listaPaises = []
for i, enumerar in enumerate(paisesIn):
    enumerar = f'{i+1}.{enumerar}' 
    listaPaises.append(enumerar)
paisesIn = ', '.join(listaPaises)
print(f'Países ingresados: {paisesIn}')