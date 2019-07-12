'''#11
def rectangle(t, size1, size2):
    t.down()
    for i in range(2):
        t.fd(size1)
        t.right(90)
        t.fd(size2)
        t.right(90)


#11b
def panels(t, initSize,delta,numPanels, angle):
    for i in range(numPanels):
        rectangle(t, initSize, initSize*2)
        initSize += delta
        t.up()
        t.right(angle)
import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
panels(shelly, 20, 15, 8, 20)'''
        
#12
'''def vowelUseDict(t):
    d ={'a':0 ,'e':0,'i':0, 'o':0,'u':0}
    t1= t.split()
    vowels = 'aeiou'
    for vowel in vowels:
        for word in t1:
            if vowel in word:
                d[vowel] +=1
    return d
text = 'like a vision she dances across the porch as the radio plays'
print(vowelUseDict(text))'''

#13
'''def longestWord(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        x= line.split()
        if len(line)==0:
            coutinue
        longest = 0
        for word in x:
            length = len(word)
            if length> longest:
                longest = length
        write.write(str(longest) + '\n')
    read.close()
    write.close()
inFile = 'you.txt'
outFile = 'troubleLongest.txt'
longestWord(inFile, outFile)'''


#midterm2
#11a
'''def halfSquare(t, length):
    t.down()
    for i in range(2):
        t.fd(length)
        t.right(90)
#11b
def halfSquares(t, inital,increment,reps):
    for i in range(reps):
        inital +=increment
        halfSquare(t,inital)
import turtle
s = turtle.Screen()
turt = turtle.Turtle()
halfSquares(turt, 20, 20, 10)'''

#12
'''def wordCount(inFile,outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        x= line.split()
        count = 0
        for word in x:
            count +=1
        write.write(str(count) +'\n')
    read.close()
    write.close()
wordCount('you.txt', 'catInTheHatOut.txt')'''

#13notdone
'''def initialVowels(inFile):
    vowels= 'aeiou'
    d = {}
    read = open(inFile, 'r')
    for line in read:
        x1= line.lower()
        x=x1.split()
        for word in x:
            if word[0] in d:
                lst=[]
                d[word[0]]= lst.append(word)
            elif word[0] in vowels:
                d[word[0]] = [word]

    return d
print(initialVowels('you.txt'))'''
            
#11a
'''def parallelLines(t, numLines,lineLength):
    for i in range(numLines):
        t.down()
        t.fd(lineLength)
        t.back(lineLength)
        t.up()
        t.right(90)
        t.fd(25)
        t.left(90)
        
        
        
import turtle
s = turtle.Screen()
turt = turtle.Turtle()
parallelLines(turt, 5,100)'''
      
        
        
#notdone12
def containsLetter(aLetter,strList):
    lst= []
    for word in strList:
        if aLetter in word:
            lst.append(word)
    return lst
def containWord(word,strList):
    lst = []
    for letter in word:
        containsLetter(letter, strList)
    
        
hulkLine = ["you", "wouldn't", "like", "me", "when", "i'm", "angry"]
word= 'hulk'
print(containWord(word, hulkLine))
#13
'''def getInt(minInt,maxInt):
        number = input(str('Please give me a number no less than' + minInt +'and no greater than ' + maxInt ))
        return str(number)
def getnumber(minInt,maxInt):
    number = getInt(minInt,maxInt)
    if '-' in number:
        return 'it is negative'
    elif number =='0':
        return 'it is zero'
    else:
        return 'it is positive'
print(getnumber('-5','7'))'''

'''#11a
def tri(t, length):
    t.down()
    for i in range(3):
        t.fd(length)
        t.back(length)
        t.right(120)

#11b
def tris(t,iniSize,ratio,rotation,num):
    for i in range(num):
        tri(t,iniSize)
        iniSize*=ratio
        t.right(rotation)

import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
tris(shelly, 100, 1.2, 30, 4)

#12
def initialLets(t):
    d ={}
    t1 = t.split()
    for word in t1:
        if word[0] in d:
            d[word[0]] +=1
        else:
            d[word[0]]=1
    return d
text = "I'm born to trouble I'm born to fate"
print(initialLets(text))'''

#13
'''def initVowels(inFile,outFile):
    vowels = 'aeiou'
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        line1= line.lower()
        line2= line1.split()
        for word in line2:
            if word[0] in vowels:
                write.write(word +' ')
        write.write('\n')
    read.close()
    write.close()
        
initVowels('you.txt', 'pay_me_vowels.txt') '''
#11
'''def letterX(t, length):
    t.down()
    t.right(45)
    for i in range(4):
        t.fd(length/2)
        t.back(length/2)
        t.right(90)
    t.left(45)

def exes(t, initSize, deltaSize,separation,xNum):
    for i in range(xNum):
        letterX(t,initSize)
        initSize *= deltaSize
        t.up()
        t.fd(separation)
import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
exes(shelly, 100, 0.6, 30, 6)'''
#12
'''def wordLengths(text):
    d = {}
    text1 = text.split()
    for word in text1:
        if len(word) in d:
            d[len(word)] +=1
        else:
            d[len(word)] =1
    return d
text = 'Go to Heaven for the climate Hell for the company'
print(wordLengths(text))'''

#13
'''def initVowelCount(inFile,outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    vowels = 'aeiou'
    count = 0
    for line in read:
        x = line.lower()
        x1= line.split()
        count = 0
        for word in x1:
            if word[0] in vowels:
                count +=1
        write.write(str(count) + '\n')
    read.close()
    write.close()
initVowelCount('you.txt', 'runFreq.txt')'''
#11a
'''def capitalL(t, width):
    for i in range(2):
        t.down()
        t.fd(width)
        t.back(width)
        t.left(90)
    t.right(180)

def Ls(t,initWidth,multiplier,reps,angle):
    for i in range(reps):
        capitalL(t, initWidth)
        initWidth *= multiplier
        t.up()
        t.right(angle)

import turtle
s = turtle.Screen()
aPen = turtle.Turtle()
aPen.left(60)
Ls(aPen, 20, 1.5, 3, 20)'''


#13 will do late
#11
'''def cup(t, sideLength):
    t.down()
    for i in range(3):
        t.fd(sideLength)
        t.left(90)
    t.up()
    t.fd(sideLength)
    t.left(90)



def cups(t, initial,incr, reps):
    for i in range(reps):
        cup(t, initial)
        initial +=incr
        t.right(90)
        t.fd(incr/2)
        t.left(90)
 
 


import turtle
s = turtle.Screen()
t = turtle.Turtle()
cups(t, 50, 30, 4) '''
#12
'''def uniqueWords(inFile,outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        x = line.lower()
        x1= x.split()
        count = 0
        lst = []
        for word in x1:
            if word not in lst:
                lst.append(word)
                count+=1
            else:
                continue
        write.write(str(count) +'\n')
    read.close()
    write.close()
    
uniqueWords('you.txt', 'turnOut.txt')'''


#13
'''import string
def importantWords(s, threshold):
    d = {}
    s1= s.lower()
    s2 = s1.split()
    for word in s2:
        if word in d:
            d[word] +=1
        elif len(word)>= threshold:
            d[word] = 1
        else:
            continue
    return d '''
#12
'''def initialDict(text):
    x1 = text.split()
    d ={}
    for word in x1:
        if word[0].lower() in d:
            d[word[0].lower()].append(word)
            
        else:
            d[word[0].lower()] = [word]
    return d
print(initialDict('The Call of the Wild'))'''





                
    

        
    


        
                
                

    
        




        
    

        





        

    
    
        

