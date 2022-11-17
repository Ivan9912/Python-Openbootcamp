import os
from getpass import getuser as gUser
from generatorHTML import html as gHTML

def main():
    file = r'.\ddbb\viewUsers.txt' 
    
    def welcome():
        os.system('start welcome.html')
        os.system(f'echo \'Welcome {gUser()}\'!!')

    i = 2
    with open(file, 'r', encoding='utf-8') as rLog:
        datas = rLog.readlines()
        rLog.close()
        while i >= 0:
            userIn = input ("Username: ")
            passIn = input ("Enter password: ")
            string = f'{userIn}:{passIn}'
            for data in datas:
                listnames = "".join(data).split('\n')
                separateOfDataOfNew = "".join(listnames).split(':', 1)
                if string == separateOfDataOfNew[1]:
                    uData = gHTML()
                    cor = len(datas)-1
                    if separateOfDataOfNew[0] == 'new ':
                        uData.helloWorld(userIn, cor)
                        welcome()
                    else:
                        uData.helloWorld(userIn, i)
                        welcome()
                    i = -1
                    break
                elif separateOfDataOfNew[0] == '_end ':
                    print(f'Ingresó el usuario o la contraseña incorrectamente.\nVuelva a intentar.\nTiene {i}/3 intentos para ingresar\n.')
                    i-=1
                elif i == 0:
                    print("Superó sus intentos de ingreso.")

if __name__ == '__main__':
    main()