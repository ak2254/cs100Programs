#12
'''def initialLets(t):
    d = {}
    for string in t:
            if string[0] in d:
                d[string] =+1
            else:
                d[string] = 1
    return d 
text = "I'm born to trouble I'm born to fate"
print(initialLets(text))'''

#13
def initVowels(inFile, outFile):
    readFile = open(infile, 'r')
    writeFile = open(outFile, 'w')
    for line in readFile:
        wordsList = line.lower().split()
        for word in wordsList:
            word = word.strip(string.puntuation)
            if word[0] in vowels:
                writeFile.write(wordwrite+ " ")
        writeFile.write('\n')
        readFile.close()
        writeFile.close()






'''

#14
def  lineStats(inflie, outfile):
    readFile = open(infile, 'r')
    writeFile = open(outfile, 'w')
    for line in readFile:
        word = 0
        char = 0
        for word in line.split():
            word +=1
            char += len(word)
            char +=len(line.split-1)
            writeFile.write(str(word) + " " + str(count)+ '\n')
    readFile.close()
    writeFile.close()
            
            
inF = 'promisedLand.txt'
outF = 'promisedLandStats.txt'
lineStats(inF, outF) '''

'''def initialDict(text):
    
    di = {}
    k = text.lower().split()
    for string in k:
        if string[0] in di:
            lst = []
            lst.append(string) 
        else:
            di[string[0]] = [string]
    return di
print(initialDict('The Call of the Wild'))'''

'''import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(6):
    t.forward(100)
    t.left(120)'''

def occurrences(fileName, searchStr):
    rtnVal = 0
    inF = open(fileName)
    for line in inF:
        lineLower = line.lower()
        rtnVal += lineLower.count(searchStr)
        inF.close()
    return rtnVal
seuss = open('you.txt', 'w')
seuss.write('Today you are You, that is truer than true.' + '\n')
seuss.write('There is no one alive who is Youer than You.' + '\n')
seuss.close()
print(occurrences('you.txt', 'you'))
seuss.close()
