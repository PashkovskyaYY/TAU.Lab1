import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color

def choise():
    inertialessUnitName = "Безынерционное звено"
    aperiodicUntName = "Апериодическое звено"

    neednewChoise  = True

    while neednewChoise:
        userInput = input("Введите номер команды: \n"  #\n переносит ввод на следующую строку
                        '1 - ' + inertialessUnitName + ';\n'
                        '2 - ' + aperiodicUntName + ';\n')

         if userInput.isdigit():
             neednewChoise = False
             userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = "Апериодическое звено"
            else:
                print('\n Недопустимое значение!')
                neednewChoise = True
        else:
            print('\n Пожалуйста, введите числовое значение!')
            neednewChoise = True
    return name

def getUnit(name):

    neednewChoise = False

     k = input('пожалуйста, введите коэффициент "k": ')
     t = input('пожалуйста, введите коэффициент "t": ')

     if k.isdigit() and t.isdigit():
         k = int(k)
         t = int(t)
         if name == 'Безынерционное звено':
             unit = matlab.tf([k], [1])
         elif name == "Апериодическое звено":\
             unit = matlab.tf([k], [t, 1])
     else:
         print('\n Пожалуйста, введите числовое значение!')
         neednewChoise = True

    return unit

def graph(num, title, y, x):
    pyplot.subploy(2,1,num)
    pyplot.grid(True)
    if title == "Переходная характеристика":
        pyplot.plot(x, y, 'purple')
    elif title = "Импульсная характеристика":
        pyplot.plot(x, y, 'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда сигнала')
    pyplot.xlabel('Время, с')


unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 1000):
    timeLine.append(i/1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, "Переходная характеристика", y, x)
[y,x] = matlab.impulse(unit, timeLine)
graph(2, "Импульсная характеристика", y, x)
pyplot.show()





choise()
