import examManagerClasses


def get_exam_info(obj: examManagerClasses.Exam):
    with open('Exams.txt') as f:
        line = f.read().split()
    obj.exam_year = line[0]
    obj.exam_semester = line[1]
    obj.exam_period = line[2]
 
    



def get_question_info(obj: examManagerClasses.Exam):
    with open('Questions.txt') as f:
        for line in f:
            if not line.strip():
                break
            line = line.split()
            empty_question = examManagerClasses.Question()
            for key in empty_question.question_info.keys():
                empty_question.question_info[key] = line[0]
                line = line[1:]
            obj.question_list.append(empty_question)


def get_course_info(obj_course: examManagerClasses.Course, obj_exam: examManagerClasses.Exam):
    with open('Courses.txt') as f:
        line = f.read().split()
    obj_course.course_name = line[0]
    obj_course.lecturer_name = line[1]
    obj_course.course_year = line[2]
    obj_course.exam = obj_exam


def get_department_info(obj_course: examManagerClasses.Course, obj_department: examManagerClasses.Department):
    with open('Departments.txt') as f:
        line = f.read().split()
    obj_department.dep_name = line[0]
    obj_department.coordinator_name = line[1]
    obj_department.course = obj_course

