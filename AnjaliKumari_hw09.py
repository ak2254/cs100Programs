#Anjali Kumari
#CS 100 2017 section 005
#HW 09
#1
def initialLetterCount(wordList):
    d = {}
    for string in wordList:
        if string[0] in d:
            d[string] +=1
        else:
            d[string] =1
    return d
horton = ['I','say','what','I','mean','and','I','mean','what','I','say']
print(initialLetterCount(horton))

#2
def initialLetters(wordList):
    di = {}
    for string in wordList:
        if string[0] in di:
            lst = []
            lst.append(string) 
        else:
            di[string[0]] = [string]
    return di
print(initialLetters(horton))           
            

#3
def shareALetter(wordList):
    d ={}
    for string in wordList:
        d[string] = [string]

    for key in d:
        for word in wordList:
            for char in word:
                if char in key and word not in d[key]:
                    d[key].append(word)
    return d
print(shareALetter(horton))
    
