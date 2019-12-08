import examManagerClasses

questions = []

def menu():

    print("-Menu-")
    print("-1-Add new user <in development>")
    print("-2-Delete existing user <in development>")
    print("-3-Update existing user <in development>")
    print("-4-Add new question <in development>")
    print("-5-Delete existing question <in development>")
    print("-6-Update existing question <in development>")
    print("-7-View questions <in development>")
    print("-0-Exit")

    choice = input()

    if choice == '4':
        q = classes.Question()
        q.question_info["Difficulity"] = "Medium"
        questions.append(q)

    if choice == '6':


    if choice == '0':
        return False
    return True

loop = True

while loop:
    loop = menu()
    for q in questions:
        print("question diffculty is: ",q.question_info["Difficulity"])