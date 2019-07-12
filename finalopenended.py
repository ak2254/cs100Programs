#final exam

#12
'''"'def mostFrequent(inFile,outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        d = {}
        for char in line:
            if char != " ":
                d[char] = line.count(char)

    maxFreq = 0
    for char in d:
        if d[char] > maxFreq:
            maxFreq == char.values()
            write.write(char)
        write.write('\n')
    read.close()
    write.close()

mostFrequent('moreYouRead.txt', 'moreYouReadOut.txt')'''


#13a
#done
'''def longEnough(s, threshold):
    if len(s) >= threshold:
        return True
    else:
        return False

print(longEnough('Amen', 4))
#13b done
def longWords(t,i):
    k = t.split()
    d = {}
    for word in k:
        if longEnough(word, i) == True:
            d[word] = k.count(word)
    return d
text = 'one fish two fish red fish blue fish'
print(longWords(text, 4))'''

#12done
'''def wordsByLine(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        k = line.split()
        d = {}
        for word in k:
            if word in d:
                d[word] +=1
            else:
                d[word] = 1
        for word in d:
            write.write(word + ' : ' + str(d[word]) + " ")
        write.write('\n')
       
    write.close()
    read.close()
wordsByLine('fish.txt', 'fishWords.txt')'''


#13done'
'''
def lineIndex(fName):
    read = open(fName, 'r')
    d = {}
    count = 0
    for line in read:
        k = line.split()
        for word in k:
            
            if word not in d:
                lst = []
                d[str(word)] = [count]
            elif count not in d[str(word)]:
                d[str(word)].append(count)
        count +=1
        
    return d
    
print(lineIndex('makeItRain.txt'))'''

#12done
'''def fileStats(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
 
    import string
    punct = string.punctuation
    lines = 0
    num = '0987654321'
    chars = 0
    words =0
    d = 0
    p =0
    for line in read:
        lines+=1
        k = line.split()
        for word in k:
            words +=1
        for char in line:
            if char in punct:
                p +=1
            if char in num:
                d +=1
            chars +=1
    chars +=lines

    write.write(str(d) + '\n' )
    write.write(str(p))
    write.write(str(lines))
    write.write(str(chars))
    write.write(str(words))
    write.close()
    read.close()

fileStats('k.txt', 'stats.txt')'''
#13done
'''
def symmetry(text):
    k = text.split()
    d = {}
    for word in k:
        if word[0] == word[-1] and word[0] not in d:
            d[word[0]] = 1
        elif word[0] in d and word[0] == word[-1]:
            d[word[0]] +=1
    return d
'''


#12done
'''def lineStats(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        d1 = {}
        for char in line:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] +=1
        k = line.lower()
        k1 = k.split()
        d = {}
        for word in k1:
            if word not in d:
                d[word] = 1
            else:
                d[word] +=1
        write.write("words " +str(len(d)) + " chars " + str(len(d1)- 1))
        write.write('\n')
    write.close()
    read.close()
    
    
            
    
lineStats('lineIn.txt', 'lineOut.txt')'''

            

#13done
'''def vowelEndings(text):
    k = text.split()
    vowels = 'aeiou'
    d = {}
    for word in k:
        if word[-1] in vowels and word[-1] not in d:
            d[word[-1]] = [str(word)]
        elif word[-1] in d and str(word) not in d[word[-1]]:
            d[word[-1]].append(str(word))
    return d
t = 'today you are you there is no one alive who is you-er than you'
print(vowelEndings(t))'''

            
#12done
'''def wordLenghts(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        k = line.split()
        d = {}
        for word in k :
            if len(word) not in d:
                d[len(word)] = 1
            else:
                d[len(word)] +=1
        maxF = 0
        for key in d:
            if d[key] > maxF:
                maxF = d[key]
                write.write(str(key) + " " + str(maxF))
        write.write('\n')
    write.close()
    read.close()
wordLenghts('run.txt', 'zaxOut.txt')'''
#13done
'''
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
print(vowelFrequency(text)) '''          
        
#class problem
'''1a)
class BankAccount:
    def __init__(self, balance, accNumber,customerName):
        self.Balance = balance
        self.accNum = accNumber
        self.cName = customerName
    def deposit(self,amount):
        self.Balance +=amount
    def withdraw(self, amount):
        if self.Balance >= amount:
            self.Balance = self.Balance - amount
            return True
        else:
            return False
    def getBalance(self):
        return self.Balance
'''
    

    
                
    
                
            
        
        
    

            
                
            
