import datetime
import timeit
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