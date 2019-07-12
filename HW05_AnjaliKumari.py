
#1a
def hasFinalLetter(strList, letters):
    strList = ['Hi there', 'It is ok', 'I am fine', 'I am good', 'the grade was an A',
           'it was not C']

    letters = 'adeoADEO'
    ansList = []
    for char in strList:
        if char[-1] in letters:
            ansList.append(char)
    return ansList

#1b
def hasFinalLetter(strList, letters):
    strList = ['Hi there', 'It is ok', 'I am fine', 'I am good', 'the grade was an A',
           'it was not C']

    letters = 'adeoADEO'
    ansList = []
    for char in strList:
        if char[-1] in letters:
            ansList.append(char)
    return ansList
strList = ['Hi there', 'It is ok', 'I am fine', 'I am good', 'the grade was an A',
           'it was not C']
letters = 'adeoADEO'
print(hasFinalLetter(strList, letters))


def hasFinalLetter(strList, letters):
    strList = ['Hi there', 'It is fine', 'I am good', 'Hello']
    letters = 'ankJANK'
    ansList = []
    for char in strList:
        if char[-1] in letters:
            ansList.append(char)
    return ansList
strList = ['Hi there', 'It is fine', 'I am good', 'Hello']
letters = 'ankJANK'
print(hasFinalLetter(strList, letters))



def hasFinalLetter(strList, letters):
    strList = ['hello', 'never mind', 'yes', 'do it']
    letters = 'oedtODET'
    ansList = []
    for char in strList:
        if char[-1] in letters:
            ansList.append(char)
    return ansList
strList = ['hello', 'never mind', 'yes', 'do it']
letters = 'oedtODET'
print(hasFinalLetter(strList, letters))

#2a

def isDivisible(maxInt, twoInts):
    maxInt = 99
    twoInts = (2,5)
    answerList = []
    for number in range(0,maxInt):
        if number % twoInts[0]== 0 and number % twoInts[1]== 0:
            answerList.append(number)
    return answerList

#2b
def isDivisible(maxInt, twoInts):
    maxInt = 99
    twoInts = (2,5)
    answerList = []
    for number in range(0,maxInt):
        if number % twoInts[0]== 0 and number % twoInts[1]== 0:
            answerList.append(number)
    return answerList
maxInt = 99
twoInts = (2, 5)
print(isDivisible(maxInt, twoInts))

def isDivisible(maxInt, twoInts):
    maxInt = 60
    twoInts = (10,7)
    answerList = []
    for number in range(1,maxInt):
        if number % twoInts[0]== 0 and number % twoInts[1]== 0:
            answerList.append(number)
    return answerList
maxInt = 60
twoInts = (2, 7)
print(isDivisible(maxInt, twoInts))


def isDivisible(maxInt, twoInts):
    maxInt = 60
    twoInts = (2,6)
    answerList = []
    for number in range(0,maxInt):
        if number % twoInts[0]== 0 and number % twoInts[1]== 0:
            answerList.append(number)
    return answerList
maxI = 60
twoI = (2, 6)
print(isDivisible(maxI, twoI))
    
    


    
    

