'''#13
def lineIndex(fName):
    d = {}
    count = 0
    rFile = open(fName, 'r')
    for line in rFile:
        x = line.split()
        for word in x:
            if word not in d:
                d[word] = [count]
            if word in d and count in d[word]:
                d[word].append(count)
        count +=1
    rFile.close()
    return d'''

        
                
                
