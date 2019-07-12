#write a fuction total vowels that takes one parameter called massege a string the fuction claculates and returns the total number of vowels in the massege

 
def  totalVowels(Message):
    horton = "A person's a person, no matter how small."
    count = 0
    vowels= "aeiouAeiou"
    for char  in Message:
        if char in vowels:
            count = count+1 
    return count
horton = "A person's a person, no matter how small."

print(totalVowels(horton))




#def test retrun function takes a parameter sequence

def testReturn(sequence):
    for x in sequence:
        return x
print(testReturn("cs100"))

import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(4):
    if i%2 == 0:
        t.right(60)
        t.forward(100)
        t.right(60)



