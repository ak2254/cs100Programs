#Anjali Kumari
#CS 100 2017 section 005
#HW 02, sept 18, 2017

import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

#square
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)

#triangle
pen.up()
pen.goto(100, 150)
pen.down()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)

#regular pentagon
pen.up()
pen.goto(-180, 150)
pen.down()
pen.left(50)
pen.right(10)
pen.right(10)
pen.fd(100)
pen.right(72)
pen.fd(100)
pen.right(72)
pen.fd(100)
pen.right(72)
pen.fd(100)
pen.right(72)
pen.fd(100)

#circles
pen.up()
pen.goto(-120, -200)
pen.down()
pen.circle(50)
pen.up()
pen.goto(-70,-215)
pen.down()
pen.circle(100)
pen.up()
pen.goto(-20,-230)
pen.down()
pen.circle(150)
pen.up()
pen.goto(30, -245)
pen.down()
import math
#3a
a = math.factorial(100)
print(a)

#b
b = math.log2(1000000)
print(b) 
# c
c = math.gcd(63, 49)
print(c) 







pen.circle(200)
