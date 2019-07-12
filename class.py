import turtle
s = turtle.Screen()
t = turtle.Turtle()
times= int(input("number of times: "))

sLength =int(input("length of side: "))

gap = 25

t.down()
for g in range(3):
    t.down()
    for i in range(4):
        t.fd(sLength)
        t.right(90)
    t.up()
    t.fd(gap+sLength)
    t.down()
