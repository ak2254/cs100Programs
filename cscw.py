
def scoreAvg(line):
    ScoreList = line.split(",")
    total = 0
    for i in ScoreList:
        total += int(i)
    avg = total/len(ScoreList)
    return avg

print(scoreAvg("87, 92, 45"))

        
        
