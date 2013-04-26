import SVM
import parse

#useParser to get Reviews from Test or Validation get tuple (0,0,review)
test= parse.testingData()

(trueTable, decTable, truePosTable, trueNegTable, decPosTable, decNegTable, posTable, negTable)= parse.svm_buckets()
#loop through each review and use one svm...output a text file with answers...
#print test[0]['uni']

def getTotalCountFeature(type1, table):
	values= table[type1].values()
	#print len(values)
	numTotal=0
	for v in values:
		numTotal+=v
	return numTotal


output1= open('svm1Tests/char.txt',"w")
output2= open('svm1Tests/uni.txt',"w")
output3= open('svm1Tests/big.txt',"w")
output= open('ValidationAnswers/T:D.txt',"w")
for te in test:
	#svm1 char
	#svm1 uni
	#svm1 big
	type1= 'char'
	numFeaturesTrueC= getTotalCountFeature(type1, trueTable)
	numFeaturesDecC= getTotalCountFeature(type1, decTable) 
	type2= 'uni'
	numFeaturesTrueU= getTotalCountFeature(type2, trueTable)
	numFeaturesDecU= getTotalCountFeature(type2, decTable) 

	type3= 'big'
	numFeaturesTrueB= getTotalCountFeature(type3, trueTable)
	numFeaturesDecB= getTotalCountFeature(type3, decTable) 

	if te == test[-1]:
		output1.write(str(SVM.getTrueOrDeceptive(type1, numFeaturesTrueC, numFeaturesDecC, te[type1], trueTable, decTable)))
		output2.write(str(SVM.getTrueOrDeceptive(type2, numFeaturesTrueU, numFeaturesDecU, te[type2], trueTable, decTable)))
		output3.write(str(SVM.getTrueOrDeceptive(type3, numFeaturesTrueB, numFeaturesDecB, te[type3], trueTable, decTable)))
		output.write(str(te["IsTrue"]))
	else:
		output1.write(str(SVM.getTrueOrDeceptive(type1, numFeaturesTrueC, numFeaturesDecC, te[type1], trueTable, decTable))+"\n")
		#print "writing char"
		output2.write(str(SVM.getTrueOrDeceptive(type2, numFeaturesTrueU, numFeaturesDecU, te[type2], trueTable, decTable))+"\n")
		#print "writing uni"
		output3.write(str(SVM.getTrueOrDeceptive(type3, numFeaturesTrueB, numFeaturesDecB, te[type3], trueTable, decTable))+"\n")
		#print "writing big"
		output.write(str(te["IsTrue"])+"\n")

output1.close()
output2.close()
output3.close()
print "Done evaluating"


#for Validation set...at same time create textfile with true answers so we can calculate our percentages...

