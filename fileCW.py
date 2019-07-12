outFile = open('hello.txt','w')
for i in range(1,6):
    outFile.write( str(i) + '\n')
outFile.close()
