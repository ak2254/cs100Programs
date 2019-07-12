#Anjali Kumari
#CS 100 2017 section 005
#HW 04, sept 25, 2017

months = ["january", "february", "march", "april","may","june","july","august","september","october","november","december"]
#1
for j in months:
    if j[0] == 'j':
        print(j)

#2
for number in range(0,99):
    if number % 2 == 0 and number % 5 == 0:
        print(number)
#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for  char in horton:
    if char in vowels:
        print(char)
        
        
for index in range(len(horton)):
#find char at the position 
     char = horton[index]
     if char in vowels:
         print(char)

total = 0
for char in horton:
    if char in vowels:
        #add 1 to total
        #total = total +1
        total +=1
print(total)
         






#write a loop that calculates the list of vowels present in the string

vowelslist = []
for char in horton:
    if char in vowels:
        vowelslist.append(char)
print(vowelslist)


#write a loop that creates and displayes a string containing all the vowels the contain all the vowels in the string 
vowelsString = " "
for char in horton:
    if char in vowels:
        vowelsString = vowelsString+char 
print(vowelsString)
        

    
    
