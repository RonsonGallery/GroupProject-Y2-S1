import os
import datetime
import timeit
import subprocess
class Department:
    def __init__(self, dep_name='', coordinator_name=''):

        self.dep_name = dep_name
        self.coordinator_name = coordinator_name
        self.course = Course()


    def __del__(self):
        None

class Course:
    def __init__(self, course_name='', lecturer_name='', course_year=''):

        self.course_name = course_name
        self.lecturer_name = lecturer_name
        self.course_year = course_year


    def __del__(self):
        None

class Exam:
    def __init__(self, exam_year='', semester='',exam_period=''):

        self.exam_period=exam_period
        self.exam_year = exam_year
        self.exam_semester = semester
        self.question_list = []


    def __del__(self):
        None

class Question(Exam):
    def __init__(self,exam_year,semester,exam_period):
        self.question_info = {'Difficulity': '', 'subject': '', 'sub_subject': '', 'Code': '', 'Format': ''}
        super()._init_(exam_year,semester,exam_period)

    def print_question_info(self):
        for k, v in self.question_info.items():
            print(f'{k} : {v}')

    def __del__(self):
        None


class Coordinator:
    def __init__(self,first_name='',last_name='',Id='',password=''):
        self.first_name=first_name
        self.last_name=last_name
        self.Id=Id
        self.password=password


class Lecturer(Coordinator):
    def __init__(self,first_name,last_name,Id,password):
        super()._init_(first_name,last_name,Id,password)


class Student(Lecturer):
    def __init__(self,first_name='',last_name='',Id='',password=''):
          super()._init_(first_name,last_name,Id,password)

class UserData:
    def __init__(self):
        self.lecturer_list = []

    def add_Coordinator(self, first_name='',last_name='',Id='',password=''):
        start = timeit.default_timer()
        print("First Name of Coordinator: ")
        first_name=input()
        print("Last Name of Coordinator: ")
        last_name=input()
        print("Id of Coordinator: ")
        Id=input()
        print("password of Coordinator: ")
        password=input()
        f=open("Coordinator.txt","a")
        L=["\n",first_name," ",last_name," ",Id," ",password]
        f.writelines(L)
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Cordinator Added Succesfuly'+ ' Lengnth of execution:' + str(stop - start)+'\n')
    def add_Lecturer(self, first_name='',last_name='',Id='',password=''):
         start = timeit.default_timer()
         print("First Name of Lecturer: ")
         first_name=input()
         print("Last Name of Lecturer: ")
         last_name=input()
         print("Id of Lecturer: ")
         Id=input()
         print("password of Lecturer: ")
         password=input()
        #self.Lecturer_list.append((first_name,last_name,Id,password))
         f=open("Lecturerer.txt","a")
         L=["\n",first_name," ",last_name," ",Id," ",password]
         stop = timeit.default_timer()
         f.writelines(L)  
         f=open("Log.txt","a")
         f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Lecturer Added Succesfuly' + ' Lengnth of execution:' + str(stop - start)+'\n')

    def add_Student(self, first_name='',last_name='',Id='',password=''):
        start = timeit.default_timer()
        print("First Name of Student: ")
        first_name=input()
        print("Last Name of Student: ")
        last_name=input()
        print("Id of Student: ")
        Id=input()
        print("password of Student: ")
        password=input()
       #self.Student_list.append((first_name,last_name,Id,password))
        f=open("Student.txt","a")
        L=["\n",first_name," ",last_name," ",Id," ",password]
        f.writelines(L)
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Student Added Succesfuly'+ ' Lengnth of execution:' + str(stop - start)+'\n')

       
    def remove_Coordinator(self,Id=''):
        start = timeit.default_timer()
        Id = input("Which id would you like to remove")
        f = open("Coordinator.txt", "r")
        g = open("Coordinator1.txt" ,"w")
        for line in f:
            if Id in line:
                    continue
            g.writelines(line)
        f.close()
        g.close()
        f = open("Coordinator.txt", "w")
        g = open("Coordinator1.txt" ,"r")
        for line in g:
             f.writelines(line)
        g.close()
        f.close()
        os.remove("Coordinator1.txt")
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Cordinator Removed Succesfuly'+ ' Lengnth of execution:' + str(stop - start)+'\n')
    def remove_Lecturerer(self,Id=''):
        start = timeit.default_timer()
        Id = input("Which id would you like to remove")
        f = open("Lecturerer.txt", "r")
        g = open("Lecturerer1.txt" ,"w")
        for line in f:
            if Id in line:
                    continue
            g.writelines(line)
        f.close()
        g.close()
        f = open("Lecturerer.txt", "w")
        g = open("Lecturerer1.txt" ,"r")
        for line in g:
             f.writelines(line)
        g.close()
        f.close()
        os.remove("Lecturerer1.txt")
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Lecturer Removed Succesfuly'+ ' Lengnth of execution:' + str(stop - start)+'\n')
    def remove_Student(self,Id=''):
        start = timeit.default_timer()
        Id = input("Which id would you like to remove")
        f = open("Student.txt", "r")
        g = open("Student1.txt" ,"w")
        for line in f:
            if Id in line:
                    continue
            g.writelines(line)
        f.close()
        g.close()
        f = open("Student.txt", "w")
        g = open("Student1.txt" ,"r")
        for line in g:
             f.writelines(line)
        g.close()
        f.close()
        os.remove("Student1.txt")
        stop = timeit.default_timer()
        f=open("Log.txt","a")
        f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Student Removed Succesfuly'+ ' Lengnth of execution:' + str(stop - start)+'\n')

    def add_exam(self):
            print("Make Sure you copy the exam to the apropriate directory")
            Name = input("Enter the name of the file fully: ")
            Day = input("Enter Day: ")
            Month = input("Enter Month: ")
            Year = input("Enter Year: ")
            Moed = input("Enter the moed A for the first B for second C for special: ")
            Semester = input("Enter the Semester (Winter,Spring,Summer): ")
            Format = input("Enter the format for the file (docx,pdf): ")
            f=open("Exams.txt","a")
            L=["\n",Name," ",Day,".",Month,".",Year," ",Moed.lower()," ",Semester.lower()," ",Format.lower()]
            f.writelines(L)
            f.close()
    def open_exam(self):
            Day = input("Enter Day: ")
            Month = input("Enter Month: ")
            Year = input("Enter Year: ")
            Format = input("Enter the format for the file (docx,pdf): ")
            Date = Day + '.' + Month + '.' +Year
            f = open("Exams.txt" ,"r")
            for line in f:
                if Date in line:
                    line = line.split()
                    Directory = os.getcwd()
                    Directory = Directory.replace('\\','\\\\')
                    print(Directory)
                    os.system(str(Directory) +'\\' +'Exams'+'\\'+ str(line[0])+'.'+Format)
                    #os.system('C:\\Users\\Owner\\source\\repos\\MenuFix\\MenuFix\\Exams' +'\\' + str(line[0])+'.'+Format)
                    break
            f.close()
                