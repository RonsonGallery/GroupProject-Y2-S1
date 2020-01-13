import menu
import LoginScreen
import examManagerClasses
import ExamManagerGetters
import datetime
import timeit

while(True):
    x = LoginScreen.Login()
    if x != 0:
        break
menu.menu(x)