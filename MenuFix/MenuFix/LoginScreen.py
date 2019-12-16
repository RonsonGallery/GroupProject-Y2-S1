#LoginScreen
import menu

def Login():
    
    print("Welcom To Program, please enter: ")
    print('1 - to log in as Coordinator')
    print('2 - to log in as Lecturer')
    print('3 - to log in as Student')
    kind = int(input()) # משתנה התופס את סוג המשתמש
    if (kind == 1):
        print('Entering Coordinator Menu...')
        Id = input('Enter Id: ') # משתנה התופס קוד זיהוי
        f = open('Coordinator.txt','r') # פותח קובץ
        for line in f:
            if Id in line:
                username = line[0:8] # שומר ת.ז
                password = line[9:14] # שומר סיסמא
                trytopass = input('Enter password:') # משתנה לניסיון מעבר הסיסמא
                if (password == trytopass):
                    print("succeeded")
                    return 1
                return False
        return False

    if (kind == 2):
        print('Entering Lecturer Menu...')
        Id = input('Enter Id: ') # משתנה התופס קוד זיהוי
        f = open('Lecturer.txt','r') # פותח קובץ
        for line in f:
            if Id in line:
                username = line[0:8]
                password = line[9:14]
                trytopass = input('Enter password:') # משתנה לניסיון מעבר הסיסמא
                if (password == trytopass):
                    print("succeeded")
                    return 2
                return False
        return False

    if (kind == 3):
        print('Entering Student Menu...')
        Id = input('Enter Id: ') # משתנה התופס קוד זיהוי
        f = open('Student.txt','r') # פותח קובץ
        for line in f:
            if Id in line:
                username = line[0:8]
                password = line[9:14]
                trytopass = input('Enter password:') # משתנה לניסיון מעבר הסיסמא
                if (password == trytopass):
                    print("succeeded")
                    return 3
                return False
        return False

    else:
         return False
