import examManagerClasses
import ExamManagerGetters
import LoginScreen
f=open("Log.txt","w")
f.close()
questions = []

def menu(x):


    print("-Menu-")
    if x == 1:
        print("-1-Add new user")
        print("-2-Delete existing user")
        print("-3-Update existing user <in development>")
    if x == 2 or x == 1:
        print("-4-Add new exam <in development>")
        print("-5-view existing exam <in development>")
        #print("-5-Delete existing question <in development>")
        print("-6-Update existing question <in development>")
    print("-7-View questions <in development>")
    print("-0-Exit")

    choice = input()
    
    if choice == '1':
        print("which type of user would you like to add \n 1-Coordinator   2-Lecturer   3-Student")
        type=input()
        
        if(type=='1'):
            examManagerClasses.UserData.add_Coordinator("","","","","")
        if(type=='2'):
             examManagerClasses.UserData.add_Lecturer("","","","","")
        if(type=='3'):
              examManagerClasses.UserData.add_Student("","","","","")
    if choice == '2':
        print("which type of user would you like to Remove \n 1-Coordinator   2-Lecturer   3-Student")
        type=input()
        if(type=='1'):
            examManagerClasses.UserData.remove_Coordinator("","")
        if(type=='2'):
             examManagerClasses.UserData.remove_Lecturerer("","")
        if(type=='3'):
              examManagerClasses.UserData.remove_Student("","")
    if choice == '4':
        examManagerClasses.UserData.add_exam("")
    if choice == '5':
        examManagerClasses.UserData.open_exam("")
    #if choice == '6':


    if choice == '0':
        return False
    return True

loop = True
#LoginScreen



#while loop:
  #  loop = menu()
   # for q in questions:
    #    print("question diffculty is: ",q.question_info["Difficulity"])