'''>>> dScores ={}
>>> dScores{'jhon'} =95
SyntaxError: invalid syntax
>>> dScores['jhon'] =95
>>> dScores['jake'] =85
>>> dScores['jill'] =85
>>> dScores
{'jhon': 95, 'jake': 85, 'jill': 85}
>>> dScores['adam'] =93
>>> dScore
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dScore
NameError: name 'dScore' is not defined
>>> dScores
{'jhon': 95, 'jake': 85, 'jill': 85, 'adam': 93}
>>> dScores['adam'] = 83
>>> dScores
{'jhon': 95, 'jake': 85, 'jill': 85, 'adam': 83}
>>> dScores['adam'] += 2
>>> dScores
{'jhon': 95, 'jake': 85, 'jill': 85, 'adam': 85}

>>> for name in dScores:
	print(name)

	
jhon
jake
jill
adam

>>> for i in dScores:
	print(dScores[i])

	
95
85
85
85



>>> for i in dScores.values():
	print(i)

	
95
85
85
85

>>> for key in dScores:
	if dScores[key] == 85:
		print(key)

		
jake
jill
adam'''
'''examScores = [90,85,75,85,90,90]
d = {}
for score in examScores:
    if score not in d:
        d[score] = 1
    else:
        d[score] += 1
print(d)

examScores = [90,85,75,85,90,90]
d = {}
for score in examScores:
    d[score] = examsScores.count(score)'''

def wordFreq(text):
    text.lower()
    newText = text.split(' ')
    freq = {}
    for string in newText:
        if string not in freq:
            freq[string] = 1
        else:
             freq[string] +=1
    return freq
            
print(wordFreq("it is what it is"))

        

