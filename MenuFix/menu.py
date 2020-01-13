import examManagerClasses
import ExamManagerGetters
import LoginScreen
import logging
import datetime
import timeit
questions = []
f=open("Log.txt","a")
f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesfuly Enterd Menu' + '\n' )
def menu(x):


    print("-Menu-")
    if x == 1:
        print("-1-Add new user")
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



    
#while loop:
  #  loop = menu()
   # for q in questions:
    #    print("question diffculty is: ",q.question_info["Difficulity"])