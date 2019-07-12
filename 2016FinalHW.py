#1 b
#2 c
#3 e
#4 a
#5 d
#6 a
#7 a
#8 b
#9 e
#10 e
#11a
def regularPoly(t, sideLen, numSides):
    t.down()
    for i in range(numSides):
           t.fd(sideLen)
           t.right((((numSides - 2) * 180)/numSides)-180)


def regularPolys(t, Slen, num, numSides):
    t.down()
    for i in range(num):
        regularPoly(t,Slen, numSides)
        numSides +=1


import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
regularPolys(shelly, 100,6,3)



#12
def wordLengths(inFile,outFile):
    inF=open(inFile, 'r')
    outF=open(outFile, 'w')
    for line in inF:
        x = line.split()
        d = {}
        for word in x:
            if len(word) not in d:
                d[len(word)] = 1
            else:
                d[len(word)] +=1
        maxF = 0
        for key in d:
            if d[key] > maxF:
                maxF = d[key]
                outF.write(str(key) + " " + str(maxF))
        outF.write('\n')
    inF.close()
    outF.close()
wordLengths('run.txt', 'zaxOut.txt')
#13
def countVowels(s):
    x = s.lower()
    count = 0
    vowels = 'aeiou'
    for char in x:
        if char in vowels:
            count +=1
    return count
print(countVowels('Amen'))
def vowelFrequency(t):
    d = {}
    x = t.split()
    
    for word in x:
        c = countVowels(word)
        if c not in d:
            d[c] = [word]
        else:
            d[c].append(word)
    return d

text = "Where hunger is ugly where souls are forgotten"
print(vowelFrequency(text))           
        
    

    


        
                           
            
 
                
    
    
