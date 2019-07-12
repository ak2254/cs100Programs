#Anjali Kumari
#CS 100 2017 section 005
#HW , October 24, 2017

#1
def twoWords(length, firstLetter):
    lst = []
    while True:
        frstWord = str(input("Enter a 4-letter word please: "))
        if len(frstWord) != length:
            continue
        else:
            lst.append(frstWord)
            scndWord = str(input('Enter a word beginning with ' + firstLetter + ' please'))
        if scndWord[0] == firstLetter:
            lst.append(scndWord)
            break 
        else:
            scndWord = str(input('Enter a word beginning with ' + firstLetter + ' please'))
    return lst
print(twoWords(4, 'b'))            

#2
def twoWordsV2(length, firstLetter):
    lst = []
    while len(lst) != 2:
        frstWord = str(input("Enter a 4-letter word please: "))
        if len(frstWord) != length:
            continue
        else:
            lst.append(frstWord)
            scndWord = str(input('Enter a word beginning with ' + firstLetter + ' please'))
            
        if scndWord[0] == firstLetter:
            lst.append(scndWord)
        else:
            str(input('Enter a word beginning with ' + firstLetter + ' please'))
        return lst
print(twoWordsV2(4, 'b'))

#3
def enterNewPassword():
   nums = '0987654321'
   while True:
        paswrd = str(input("please enter 8-15 character password: "))
        for char in nums:
            if char in paswrd and len(paswrd) >= 8:
                print("It passed both tests")
                return paswrd
        print("you failed the one or both of the conditions")
                
print(enterNewPassword())

#4

def GuessNumber():
    tryz = 0
    import random
    num = random.randint(0,50)
    while tryz !=5:
        tryz += 1
        guess = int(input("guesss a number: "))
        if guess > num:
            print("number is too high")
        elif guess < num:
            print("number is too low")
        else:
            print("you are right! i was thinking of "+ num)
    return num
print(GuessNumber())

        
        
    

            
        

            
            
            
