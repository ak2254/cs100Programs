

#11
def letterX(t, length):
        t.down()
        t.left(45)
        for i in range(4):
                t.fd(length/2)
                t.bk(length/2)
                t.right(90)
        t.right(45)

def stair(t,num_stairs,tread_size,rise_height):
    t.down()
    
    for i in range(num_stairs):       #loop num_stairs times
        t.fd(tread_size)
        t.right(90)
        t.forward(rise_height)
        t.left(90)


import turtle
s = turtle.Screen()
aTurt = turtle.Turtle()
stair(aTurt,3,10,20)
'''

def exes(t, initSize, deltaSize,separation, xNum):
##    s = deltaSize
    t.up()
    t.fd(separation)
    t.down()
    for i in range(xNum):
        letterX(t, initSize)
        initSize = initSize*deltaSize
        t.up()
        t.fd(separation)
        t.down()



import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
exes(shelly, 100, 0.6, 30, 6)

'''







'''

#12
def wordLengths(text):
    d = {}
    text1= text.split()
    for word in text1:
        if len(word) in d:
            d[len(word)] +=1
        else:
            d[len(word)] = 1
    return d

text = 'Go to Heaven for the climate Hell for the company'
print(wordLengths(text))'''

'''#13
def initVowelCount(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    vowels = 'aeiou'
    i = read.readlines().lower()
    count = 0
    for string in i:
        k = string.split()
        for word in k:
            if word[0] in vowels:
                count +=1
        if count == 0:
            write.write('\n')
        else:
            write.write(str(count) + '\n')
    write.close()
    read.close()

initVowelCount('run.txt', 'runMostFreq.txt')'''










