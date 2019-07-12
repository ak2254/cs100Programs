'''wtring a functon computeAvg that take one parameter:fileName , the function returns
the avg score in the file'''
def computeAvg(fileName):
    fileName = open('scores.text', 'r')
    aveg = 0
    count = 0
    for score in fileName:
        k = score.split()
        avg +=int(k[1])
        count += 1
    avg = avg / count
    fileName.close()
    return avg
