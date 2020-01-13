import menu
import LoginScreen
import examManagerClasses
import ExamManagerGetters
import datetime
import timeit
start = timeit.default_timer()
while(True):
    x = LoginScreen.Login()
    if x != 0:
        break
stop = timeit.default_timer()
f=open("Log.txt","a")
f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesfuly logged in'+' Lengnth of execution:' + str(stop - start)+'\n' )
start = timeit.default_timer()
while(status):
    status = menu.menu(x)
stop = timeit.default_timer()
f=open("Log.txt","a")
f.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Succesfuly exiting program'+' Lengnth of execution:' + str(stop - start)+'\n' )
