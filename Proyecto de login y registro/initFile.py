import os
def main():
    os.system("mkdir ddbb")

    file = r'.\ddbb\viewUsers.txt'
    f = open(file, 'w')
    f.close()
    
    web = r'.\welcome.html'
    f = open(web, 'w')
    f.close()
    
if __name__ == '__main__':
    main()