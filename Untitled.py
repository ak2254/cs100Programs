def drawSquare(t, lenght):
    t.down()
    for i in range(4):
        t.fd(lenght)
        t.left(90)


def drawSquares(t, size, num, angle):
   for x in range(num):
        drawSquare(t, size)
        t.right(angle)



def bigCount(numList, threshold):
    count = 0
    for num in numList:
        if num > threshold:
            count = count + 1
    return count 
someNums = [-5, 6, 3, 0, 7]
print(bigCount(someNums, 2))

def getDate(message):
    month = str(input("what month is it? " ))
    date = str(input(" what is the date? "))
    print (month, date, message)
    rtnString=month+ " " +day
    return rtnString

def evenLengths(stringList):
    k = []
    for string in stringList:
        if len(string) % 2== 0:
            k.append(string)
    return k
song = ['happy', 'birthday', 'to', 'you']
print(evenLengths(song))


def courseload(light, heavy):
    credit = int(input("how many credits? "))
    if credit <= light:
        print(credit ,"is a light schedule")
        return light 
    elif credit >= light:
        print(credit , "is a heavy schedule")
        return light
    else:
        print(credit ,"is a average schedule")
        return light
print(courseload(11, 16))

        
def drawTick(t,tickLen):
    t.down()
    t.right(90)
    t.fd(tickLen)
    t.up()
    t.goto(0,0)


    


    
import turtle
s = turtle.Screen()
turt = turtle.Turtle()
drawTick(turt, 100)           
            
            
    


            
            
    
