import os
def main():
    os.system("mkdir bbdd")

    file = r'.\bbdd\viewUsers.txt'
    f = open(file, 'w')
    f.close()
    
    web = r'.\welcome.html'
    f = open(web, 'w')
    f.close()
    
if __name__ == '__main__':
    main()