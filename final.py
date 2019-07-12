def mostFrequent(inFile, outFile):
    read = open(inFile, 'r')
    write = open(outFile, 'w')
    for line in read:
        d = {}
        for char in line:
            if char  != " ":
                d[char] = line.count(char)
        maxFreq = max(d.values)
        for char in d:
            if d[char] == maxFreq:
                write.write(char)
        write.write('\n')
    read.close()
    write.close()
mostFrequent('run.txt', 'moreYouReadOut.txt')   









'''       x= line.split()
        count = 0
        d = ''
        for word in x:
            for letter in word:
                if letter.count > count: 
                    count == letter.count
                    d.append[letter]
                elif letter.count==count:
                    d.append[letter]
        write.write(d + '\n')
    read.close()
    write.close()
mostFrequent('run.txt', 'moreYouReadOut.txt')'''
 
