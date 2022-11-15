def main():
    file = r'.\Proyecto de login y registro\viewUsers.txt' 
    
    i = 2
    with open(file, 'r', encoding='utf-8') as rLog:
        datas = rLog.readlines()
        rLog.close()
        while i >= 0:
            userIn = input ("Nombre de usuario: ")
            passIn = input ("Ingrese la contraseña: ")
            string = f'{userIn}:{passIn}'
            for data in datas:
                listnames = "".join(data).split('\n')
                separateOfDataOfNew = "".join(listnames).split(':', 1)
                if string == separateOfDataOfNew[1]:
                    if separateOfDataOfNew[0] == 'new ':
                        print(f'Bienvenido {userIn}!\nSu número de usuario es el #{len(datas)-1}')
                    else:
                        print(f'Bienvenido {userIn}!\nSu número de usuario es el #{i}')
                    i = -1
                    break
                elif separateOfDataOfNew[0] == '_end ':
                    print(f'Ingresó el usuario o la contraseña incorrectamente.\nVuelva a intentar.\nTiene {i}/3 intentos para ingresar\n.')
                    i-=1
                elif i == 0:
                    print("Superó sus intentos de ingreso.")
    
if __name__ == '__main__':
    main()