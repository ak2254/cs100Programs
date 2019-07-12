#Anjali Kumari
#CS 100 2017 section 005
#HW 03, sept 23, 2017
import math 
a = 3
b = 4
c = 5


#1
if a < b :
    print("OK")
if c < b:
    print("OK")
if a + b == c:
    print("OK")
if a**2 + b**2 == c**2:
    print("OK")


#2
if a < b :
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")

if a + b == c:
    print("OK")
else:
    print("NOT OK")

if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")





#3
import turtle
s = turtle.Screen()
pen = turtle.Turtle()


color = input("what color? ")
lineWidth = int(input("what line width? "))
lineLength = int(input("what line length? "))
shape = input(" line, triangle or square? ")

if shape == "triangle":
    pen.up()
    pen.color(color)
    pen.width(lineWidth)
    pen.down()
    pen.forward(lineLength)
    pen.left(120)
    pen.forward(lineLength)
    pen.left(120)
    pen.forward(lineLength)
elif shape== "square":
    pen.up()
    pen.color(color)
    pen.width(lineWidth)
    pen.down()
    pen.forward(lineLength)
    pen.right(90)
    pen.forward(lineLength)
    pen.right(90)
    pen.forward(lineLength)
    pen.right(90)
    pen.forward(lineLength)
elif shape=="line":
    pen.up()
    pen.color(color)
    pen.width(lineWidth)
    pen.down()
    pen.forward(lineLength)



    
