#LoginScreen
import menu
import datetime
import timeit
def Login():
    f=open("Log.txt","a")
    f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesfuly enterd menu' )
    print("Welcom To Program, please enter: ")
    print('1 - to log in as Coordinator')
    print('2 - to log in as Lecturer')
    print('3 - to log in as Student')
    kind = int(input()) # משתנה התופס את סוג המשתמש
    if (kind == 1):
        start = timeit.default_timer()
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
                    stop = timeit.default_timer()
                    f=open("Log.txt","a")
                    f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesful login as Coordinator'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                    return 1
                stop = timeit.default_timer()
                f=open("Log.txt","a")
                f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Failed login as Coordinator'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                return 0
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Failed login as Coordinator'+ ' Lengnth of execution:' + str(stop - start)+'\n')
        return 0
       
    if (kind == 2):
        start = timeit.default_timer()
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
                    stop = timeit.default_timer()
                    f=open("Log.txt","a")
                    f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesful login as Lecturer'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                    return 2
                stop = timeit.default_timer()
                f=open("Log.txt","a")
                f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' failed login as Lecturer'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                return 0
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' failed login as Lecturer'+ ' Lengnth of execution:' + str(stop - start)+'\n')
        return 0

    if (kind == 3):
        start = timeit.default_timer()
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
                    stop = timeit.default_timer()
                    f=open("Log.txt","a")
                    f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Sucessful login as Student'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                    return 3
                stop = timeit.default_timer()
                f=open("Log.txt","a")
                f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' failed login as Student'+ ' Lengnth of execution:' + str(stop - start)+'\n')
                return 0
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' failed login as Student'+ ' Lengnth of execution:' + str(stop - start)+'\n')
        return 0

    else:
         stop = timeit.default_timer()
         f=open("Log.txt","a")
         f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' failed login as any of the legal options'+ ' Lengnth of execution:' + str(stop - start)+'\n')
         return 0
