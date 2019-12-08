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


class Student:
    def __init__(self,first_name='',last_name='',Id='',password=''):
        self.first_name=first_name
        self.last_name=last_name
        self.Id=Id
        self.password=password
