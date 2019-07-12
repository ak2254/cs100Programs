###Anjali Kumari
###CS 100 2017 section 005
###HW 00, sept 12, 2017
##
##
###Exercise 5b
##months = 12
##age = 18
##number = 3
##
##
##
###Exercise 5c
##height = 7.63
##pi = 3.14
##lenght = 5.67
##
##
##
###Exerice 5d
##manFromUncle = 'Napolean solo'
##MyName = 'Anjali Kumari'
##KeyOfRoom = 'Hey there'
##
###1-1
###1 Answer: In a print statement if you leave out one parentheses, or both, it gives an syntaxError.
###2 Answer: It give an invalid syntaxError.
###3 Answer: It adds the two numbers up. for example: 2++2 = 4.
###4 answer: It give an invalid token syntax error.
###5 Answer: Two values without an operator between them gives an invalid syntax error.
##
##
###1-2
###1
##seconds = 42 * 60 + 42
###2
##miles = 10 / 1.61
###3
##MPH = ((10 * 3600) / (2562* 1.61))
##
##
###2-1
###1 Answer: It gives an syntax error stating that can't assign to literal.
###2 Answer: It comes out as both x and y are asigned as 1.
###3 and #4 Answer: they both work and don't show any kind of error.
###5 Answer: It comes as an name error and does not recall x and y sepreatly.
##
##
###2-2
###1
##v = (4 / 3) * pi * 5**3
###2
##cost = ((24.95 * 60)* 0.40) + 3 + 0.75 * 59
##
###3
##Time = '7:20:51'
##
##
###2
##import turtle
##s = turtle.Screen()
##t = turtle.Turtle()
##ints = [6, 5, 4, 3, 2]
##for i in ints:
##    if i%2 == 1:
##        t.forward(100)
##        t.right(90)
##
##aList = ['one', -1, 2]
##prefix = aList[:2]
##print(prefix)
##
##import turtle
##s = turtle.Screen()
##t = turtle.Turtle()
##for i in range(5):
##    if i//4 == 0:
##        t.forward(100)
##        t.right(90)
##import turtle
##s = turtle.Screen()
##t = turtle.Turtle()
##for i in range(2):
##    t.forward(100)
##    t.right(90)
##    t.forward(100)
import turtle
t = turtle.Turtle()
for i in range(4):
    if i%1 == 0:
        t.forward(100)
        t.left(90)
    else:
        t.forward(100)
        t.right(90)
