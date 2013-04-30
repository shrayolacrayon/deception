#compare text files
readingOutput1= open("svm2Tests/char.txt","r")
readingOutput2= open("svm2Tests/uni.txt","r")
readingOutput3= open("svm2Tests/big.txt","r")
readingOutput4= open("svm2Tests/pos.txt","r")

correctReadingOutput= open("ValidationAnswers/T:D.txt", "r")

testChar= []
testUni= []
testBig= []
testPos= []

correct= []


for line in readingOutput1:
	line.rstrip()
	testChar.append(line)

for line in readingOutput2:
	line.rstrip()
	testUni.append(line)

for line in readingOutput3:
	line.rstrip()
	testBig.append(line)

for line in readingOutput4:
	line.rstrip()
	testPos.append(line)

for line in correctReadingOutput:
	line.rstrip()
	correct.append(line)

readingOutput3.close()
readingOutput2.close()
readingOutput1.close()
readingOutput4.close()
correctReadingOutput.close()

if not (len(testChar) == len(correct) and len(testUni) == len(correct) and len(testBig) == len(correct)and len(testPos) == len(correct)):
	print "One of the files is the wrong size...too many or too few reviews"
else:
	total= len(correct)

	numCorrectChar=0
	numCorrectUni= 0
	numCorrectBig= 0
	numCorrectPos=0

	for t in range(0,len(correct)):
		if correct[t] == testChar[t]:
			numCorrectChar+=1
		if correct[t] == testUni[t]:
			numCorrectUni+=1
		if correct[t] == testBig[t]:
			numCorrectBig+=1
		if correct[t] == testPos[t]:
			numCorrectPos+=1



	#print numCorrectChar
	print "This is the percent accuracy for each type of feature!"
	print "Char: "+str((numCorrectChar/float(total))*100)+"%"
	print "Uni: "+str((numCorrectUni/float(total))*100)+"%"
	print "Big: "+str((numCorrectBig/float(total))*100)+"%"
	print "Pos: "+str((numCorrectPos/float(total))*100)+"%"