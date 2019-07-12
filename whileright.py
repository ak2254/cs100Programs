def getNegative():
    number = int(input("enter a number:" ))
    while number <= 0:
        number = int(input("enter a number: "))
    return number 
  
'''def getAges(letter):
    Get the age of every person whose name begins with letter
    rtnLst = []

    while True:
        name = input('Enter name: ')
        if name == '':
            return rtnLst
        if name[0] != letter:
            continue
        age = input('Enter age: ')        
        rtnLst.append(age)
print(getAges('a'))'''


"""def oddNumbers():
    lst = []
    while True:
           num = (input("enter odd positive number: "))
           if num%2 == 1:
               continue
           if num == '':
                break   
           lst.append(num)
            
print(oddNumbers())"""

        
import string
string.punctuation

str1 = "...hello..."
str1.strip(string.punctuation)
str1

cleanstr1 = str1.strip(string.punctuation)
cleanstr1


"""def playwithdice():
    import random
    tryz = 0
    while True:
        tryz +=1
        num1 = random.randint(1,6)
        num2= random.randint(1,6)
        if num1== 6 and num2 == 6:
            return tryz
print(playwithdice())"""


'''def randomChars(text, threashold):
    import random
    vowels ="aeiouAEIOU"
    tryz = 0
    count = 0
    while true:
        tryz += 1
        randChar = text[random.randint(0, len(text)-1)]
        if randChar in vowels:
           count += 1
        if count == threashold:
            break

    return tryz'''
        


            
        
    
    
            
        
