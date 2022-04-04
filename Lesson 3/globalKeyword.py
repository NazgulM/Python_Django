import config
import update

c = 0


def add():
    global c
    c = c + 2
    print("Inside add(): ", c)


add()
print('In main: ', c)
print()


def foo():
    x = 20

    def bar():
        global x
        x = 50

    print('Before calling bar: ', x)
    print('Calling bar now')
    bar()
    print('After calling bar: ', x)


foo()
print('X in main: ', x)
