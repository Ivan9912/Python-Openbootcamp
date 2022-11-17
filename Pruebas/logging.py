# import logging 

# logging.basicConfig(Level=logging.INFO)
# # logging.basicConfig(Level=logging.ERROR)

# logging.info('Arrancando programa')
# logging.warning('Hace calor')
# logging.error('test')
# logging.critical('adiós')

#---------------------------------------------

# cursos = ['Java', 'Python', 'GIT']
# asistentes = [15, 20, 4]
# demo = zip(cursos, asistentes)
# print(list(demo))

#--------------------------
# ista1 = ['f','ñ','p','i','j','c']

# ordenada = sorted(lista1, reverse=True, key= lambda x: str(x).startswith('i'))
# print(ordenada)l

#------------------
# from getpass import getpass #MUY ÚTIL PARA MI PROYECTO

# user = input("username: ")
# password = getpass("password: ")
# print(user, password)
#------------------------------

#Mini juego de adivinianzas
secreto = 99

valor = 0
while valor != secreto:
    valor = input('Ingrese un valor númerico: ')
    valor = int(valor)
    
    if valor > secreto:
        print('Muy alto el valor.')
        continue
    
    if valor < secreto:
        print('Muy bajo el valor.')
        continue
print('Acertaste el valor.')