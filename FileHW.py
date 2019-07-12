#Anjali Kumari
#CS 100 2017 section 005
#HW File
#1

def file_copy(in_file, out_file):
    readFile = open(in_file, 'r')
    writeFile = open(out_file, 'w')
    for k in readFile:
        writeFile.write(readFile)   
    infile.close()
    out_file.close()
   
    

#2
def file_stats(in_file):
    inF = open(in_file, 'r')
    lines = 0
    for line in inF:
        lines +=1
    inF.close()
    inF = open(in_file)
    l = inF.read()
    wordList = l.split()
    words = len(wordList)

    inF.close()
    inF = open(in_file, 'r')

    content = inF.read()
    characters = len(content)
    
    print("lines " + str(lines) +"\n" +"words" + str(words) + '\n' + 'characters' + " " + str(characters))
                
                
        
        
        
        
        
#3
import string
        
def repeat_words(inputFile, outputFile):
    readFile = open(inputFile, 'r')
    writeFile = open(outputFile, 'w')
    lst = []
    for line in readFile:
        k = line.lower().split()
        for i in range(len(k)):
            k[i] = k[i].strip(string.punctuation)
        for word in k:
            if k.count(word) > 1:
                if word not in lst:
                    lst.append(word)
                    writeFile.write(word + ' ')
        writeFile.write('\n')
    readFile.close()
    writeFile.close()
    
                    
            
            
            
            
    
    
    
    
    
    

