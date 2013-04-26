#compare text files
readingOutput1= open("svm1Tests/char.txt","r")
readingOutput2= open("svm1Tests/uni.txt","r")
readingOutput3= open("svm1Tests/big.txt","r")

correctReadingOutput= open("ValidationAnswers/T:D.txt", "r")

testChar= []
testUni= []
testBig= []

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

for line in correctReadingOutput:
	line.rstrip()
	correct.append(line)

if not (len(testChar) == len(correct) and len(testUni) == len(correct) and len(testBig) == len(correct)):
	print "One of the files is the wrong size...too many or too few reviews"
else:
	total= len(correct)

	numCorrectChar=0
	numCorrectUni= 0
	numCorrectBig= 0

	for t in range(0,len(correct)):
		if correct[t] == testChar[t]:
			numCorrectChar+=1
		if correct[t] == testUni[t]:
			numCorrectUni+=1
		if correct[t] == testBig[t]:
			numCorrectBig+=1


	print numCorrectChar
	print "This is the percent accuracy for each type of feature!"
	print "Char: "+str(numCorrectChar/float(total))
	print "Uni: "+str(numCorrectUni/float(total))
	print "Big: "+str(numCorrectBig/float(total))