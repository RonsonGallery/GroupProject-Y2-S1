import examManagerClasses
import ExamManagerGetters
import LoginScreen
import logging
import datetime
import timeit
f=open("Log.txt","w")
f.close()
questions = []

def menu(x):


    print("-Menu-")
    if x == 1:
        print("-1-Add new user <in development>")
        print("-2-Delete existing user <in development>")
        print("-3-Update existing user <in development>")
    if x == 2 or x == 1:
        print("-4-Add new question <in development>")
        print("-5-Delete existing question <in development>")
        print("-6-Update existing question <in development>")
    print("-7-View questions <in development>")
    print("-0-Exit")

    choice = input()
    
    if choice == '1':
        print("which type of user would you like to add \n 1-coordinator   2-lecturer   3-student")
        type=input()
        
        if(type=='1'):
            examManagerClasses.UserData.add_Coordinator("","","","","")
        if(type=='2'):
             examManagerClasses.UserData.add_Lecturer("","","","","")
        if(type=='3'):
              examManagerClasses.UserData.add_Student("","","","","")

    if choice == '4':
        q = classes.Question()
        q.question_info["Difficulity"] = "Medium"
        questions.append(q)

    if choice == '6':


     if choice == '0':
        return False
    return True

loop = True
#LoginScreen


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
    
#while loop:
  #  loop = menu()
   # for q in questions:
    #    print("question diffculty is: ",q.question_info["Difficulity"])