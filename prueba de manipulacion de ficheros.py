def main():
    
    file_name = r'C:\Users\Desktop\usuarios.txt' #agregar ubicacion del archivo txt
    users = []
    passwords = []
    validation = True
    
    with open(file_name, 'w', encoding='utf-8') as fAdd:
        fAdd.write(':Users:Passwords\n1 :Nora:1234321\n2 :Exequiel:23214\n3 :Iván:12456834\n4 :Gastón:12564534\n5 :Ramón:14568234\n')
        fAdd.close()
    print("Hi!")
    
    while (validation):
        question1 = 'yes' 
        question2 = 'y'
        question3 = 'si'
        question4 = 'sí'
        question5 = 's'
        response = input("Do you want to add a user and password?\nType Yes or Not: ")
        lowerResponse = response.lower()
        if question1 == lowerResponse or question2 == lowerResponse or question3 == lowerResponse or question4 == lowerResponse or question5 == lowerResponse:
            print('')
            addDataUser = input("'Tell the user to add:'  ")
            addDatePassword = input("Now add the password:  ")
            with open(file_name, 'a', encoding='utf-8') as newAdd:
                newAdd.write(f'new :{addDataUser}:{addDatePassword}\n')
                newAdd.close()
            break
        else:
            print('The previously loaded list will be displayed:')
            validation = False

    class Datas:
        def indexingData(self, data):
            with open(data, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                f.close()
            for line in lines: 
                listnames = "".join(line).split('\n')
                separateOfData = "".join(listnames).split(':')
                users.append(separateOfData[1])
                passwords.append(separateOfData[2])
            return
        
    callData = Datas()  
    callData.indexingData(file_name)   
    
    print('')
    for i, user in enumerate(users):
        password = passwords[i]
        print(f'{user} : {password}')
    print('')
    
if __name__ == '__main__':
    main()