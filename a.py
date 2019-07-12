def midline(t, lineLength):
    t.up()
    t.fd(lineLength/2)
    t.down()
    t.left(180)
    t.fd(lineLength)
    t.up()
    t.right(180)
    t.fd(lineLength/2)


def spiral(t, length, multiplier, numLines, angle):
    len1 = length
    for i in range(numLines):
        midline(t, len1)
        len1=len1*multiplier
        t.right(angle)
    return
    


def drawTick(t, tickLen):
    t.down()
    t.right(90)
    t.fd(tickLen)
    t.up()
    t.fd(-tickLen)
    t.left(90)
    
    

def drawTicks(t, tickLen, numTicks, distance):
    for i in range(numTicks):
        drawTick(t, tickLen)
        t.up()
        t.fd(distance)

#2
def evenLengths(stringList):
    ansList = []
    for string in stringList:
        if len(string)%2==0:
            ansList.append(string)
    return ansList
song = ['happy', 'birthday', 'to', 'you']
print(evenLengths(song))



#3
def courseLoad(light, heavy):
    credit = int(input("how many credits?"))
    if credit <=  light:
        print( credit, "is a light schedule.")
        return "light"
    if credit >= heavy:
        print( credit, "is a heavy schedule.")
        return "heavy"
    else:
        print(credit, "is a average")
        return "average"
mySchedule = courseLoad(11, 16)




