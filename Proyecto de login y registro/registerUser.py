from getpass import getuser
def main():
    
    file_name = r'.\bbdd\viewUsers.txt'
    users = []
    passwords = []
    listData = [
        'user:pass'
    ]
    
    print(f'Hi {getuser()}! Welcome!')
    response = input(f'Do you want to add a user and password?\nType Yes or Not: ')
    lowerResponse = response.lower()
    
    questions = [
        'yes',
        'y',
        'si',
        'sí',
        's'
    ]
    
    def registro():
        callData = Datas()  
        callData.indexingData(file_name)   
        
        print('')
        for i, user in enumerate(users):
            password = passwords[i]
            print(f'{user} : {password}')
        print('')
        return
    
    class Datas:
        def indexingData(self, data):
            with open(data, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                f.close()
            for line in lines: 
                listnames2 = "".join(line).split('\n')
                separateOfData = "".join(listnames2).split(':')
                users.append(separateOfData[1])
                passwords.append(separateOfData[2])
            return
        
    with open(file_name, 'r', encoding='utf-8') as tr:
        otherLines = tr.readlines()
        for i, otherLine in enumerate(otherLines): 
            convert = f'{i} '
            if convert != '0 ':
                listnames = "".join(otherLine).split('\n')
                separateOfDataOfNew = "".join(listnames).split(':')
                if separateOfDataOfNew[0] == convert or separateOfDataOfNew[0] == 'new ':
                    listData.append(f'{separateOfDataOfNew[1]}:{separateOfDataOfNew[2]}')
        tr.close()
           
    with open(file_name, 'w', encoding='utf-8') as oAdd:
        for i, oneData in enumerate(listData):
            oAdd.write(f'{i} :{oneData}\n')
        oAdd.close()
   
    for i, question in enumerate(questions):
            if question == lowerResponse:
                validationUsers = []
                for list in listData:
                    separateOfDataComp = "".join(list).split(':')
                    validationUsers.append(separateOfDataComp[0])
                print('')
                addDataUser = input("Tell the user to add:  ")
                while addDataUser != '' and addDataUser != ' ' and addDataUser != '\n':
                    if addDataUser in validationUsers:
                        print("El usuarios ingresado ya existe.\nPresione ENTER para salir.\n O vuelva a intentar.")
                        addDataUser = input("\nTell the user to add:  ")   
                    else:
                        addDatePassword = input("Now add the password:  ")
                        with open(file_name, 'a', encoding='utf-8') as newAdd:
                            newAdd.write(f'new :{addDataUser}:{addDatePassword}\n_end :0:0 \n')
                            newAdd.close()  
                        break
            elif question != lowerResponse and i == 4:
                print('The previously loaded list will be displayed:')
                registro()
    
if __name__ == '__main__':
    main()