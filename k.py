def square(t,length):
    t.down()
    for i in range(4):
        t.fd(length)
        t.right(90)
import turtle
pen = turtle.Turtle()
number = int(input("number of squares: "))
sLength= int(input("Length of the side: "))
angle = int(input("angle value: "))
CS= int(input("increased between consecutive squares: "))
        
square(pen, sLength)
for i in range(number):
    square(pen,sLength)
    pen.right(angle)
    sLength= sLength+ CS
             
    
        
