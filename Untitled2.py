
def drawTick(t, tickLen):
    t.down()
    for i in range(1):
           t.right(90)
           t.fd(tickLen)

def drawTicks(t, tickLen, numTicks, distance):

    for i in range(numTicks):
        drawTick(t, tickLen)
    t.up()
    t.fd(distance)
    t.down()


 

def beginsWith(letter, strList):
    numofstr= 0
    for char in strList:
        if char[0] == letter:
            numofstr= numofstr + 1
    return numofstr

def greeting(greetStr):
    name = str(input("name?" ))
    day = str(input("day?" ))
    print(greetStr ,day ,name)
    if len(name) == len(day):
        print("Your name has the same number of characters as today!")
    elif len(name) > len(day):
        print("Your name has the more number of characters as today!")
    else:
        print("Your name has the less number of characters as today!")


def concentric(t, radius):
    t.up()
    t.right(90)
    t.fd(radius)
    t.left(90)
    t.down()
    t.circle(radius)
    t.up()
    t.left(90)
    t.fd(radius)
    t.right(90)
def dartboard(t, numRing, delta):
    s = delta
    for i in range(numRing):
        concentric(t, s)
        s = delta + s
    
    

import turtle
s = turtle.Screen()
aTurt = turtle.Turtle()
dartboard(aTurt, 5, 20) 



