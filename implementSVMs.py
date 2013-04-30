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
output4= open('svm2Tests/char.txt',"w")
output5= open('svm2Tests/uni.txt',"w")
output6= open('svm2Tests/big.txt',"w")
output= open('ValidationAnswers/T:D.txt',"w")

#svm1 char
#svm1 uni
#svm1 big
type1= 'char'
numFeaturesTrueC= getTotalCountFeature(type1, trueTable)
numFeaturesDecC= getTotalCountFeature(type1, decTable) 

numFeaturesPosC= getTotalCountFeature(type1, posTable)
numFeaturesNegC= getTotalCountFeature(type1, negTable) 

numFeaturesTrueGivenPC= getTotalCountFeature(type1, truePosTable)
numFeaturesDecGivenPC= getTotalCountFeature(type1, decPosTable) 

numFeaturesTrueGivenNC= getTotalCountFeature(type1, trueNegTable)
numFeaturesDecGivenNC= getTotalCountFeature(type1, decNegTable) 

type2= 'uni'
numFeaturesTrueU= getTotalCountFeature(type2, trueTable)
numFeaturesDecU= getTotalCountFeature(type2, decTable) 

numFeaturesPosU= getTotalCountFeature(type2, posTable)
numFeaturesNegU= getTotalCountFeature(type2, negTable) 

numFeaturesTrueGivenPU= getTotalCountFeature(type2, truePosTable)
numFeaturesDecGivenPU= getTotalCountFeature(type2, decPosTable) 

numFeaturesTrueGivenNU= getTotalCountFeature(type2, trueNegTable)
numFeaturesDecGivenNU= getTotalCountFeature(type2, decNegTable) 

type3= 'big'
numFeaturesTrueB= getTotalCountFeature(type3, trueTable)
numFeaturesDecB= getTotalCountFeature(type3, decTable) 

numFeaturesPosB= getTotalCountFeature(type3, posTable)
numFeaturesNegB= getTotalCountFeature(type3, negTable) 

numFeaturesTrueGivenPB= getTotalCountFeature(type3, truePosTable)
numFeaturesDecGivenPB= getTotalCountFeature(type3, decPosTable) 

numFeaturesTrueGivenNB= getTotalCountFeature(type3, trueNegTable)
numFeaturesDecGivenNB= getTotalCountFeature(type3, decNegTable) 

for te in test:

	posOrNegC= SVM.getTrueOrDeceptive(type1, numFeaturesPosC, numFeaturesNegC, te[type1], posTable, negTable)
	posOrNegU= SVM.getTrueOrDeceptive(type2, numFeaturesPosU, numFeaturesNegU, te[type2], posTable, negTable)
	posOrNegB= SVM.getTrueOrDeceptive(type3, numFeaturesPosB, numFeaturesNegB, te[type3], posTable, negTable)

	trueOrDecC=0
	trueOrDecU=0
	trueOrDecB=0

	if posOrNegC == 1:
		trueOrDecC= SVM.getTrueOrDeceptive(type1, numFeaturesTrueGivenPC, numFeaturesDecGivenPC, te[type1],truePosTable, decPosTable)
	else:
		trueOrDecC= SVM.getTrueOrDeceptive(type1, numFeaturesTrueGivenNC, numFeaturesDecGivenNC, te[type1],trueNegTable, decNegTable)
	
	if posOrNegU == 1:
		trueOrDecU= SVM.getTrueOrDeceptive(type2, numFeaturesTrueGivenPU, numFeaturesDecGivenPU, te[type2], truePosTable, decPosTable)
	else:
		trueOrDecU= SVM.getTrueOrDeceptive(type2, numFeaturesTrueGivenNU, numFeaturesDecGivenNU, te[type2], trueNegTable, decNegTable)

	if posOrNegB == 1:
		trueOrDecB= SVM.getTrueOrDeceptive(type3, numFeaturesTrueGivenPB, numFeaturesDecGivenPB, te[type3], truePosTable, decPosTable)
	else:
		trueOrDecB= SVM.getTrueOrDeceptive(type3, numFeaturesTrueGivenNB, numFeaturesDecGivenNB, te[type3], trueNegTable, decNegTable)
	

	if te == test[-1]:
		output1.write(str(SVM.getTrueOrDeceptive(type1, numFeaturesTrueC, numFeaturesDecC, te[type1], trueTable, decTable)))
		output2.write(str(SVM.getTrueOrDeceptive(type2, numFeaturesTrueU, numFeaturesDecU, te[type2], trueTable, decTable)))
		output3.write(str(SVM.getTrueOrDeceptive(type3, numFeaturesTrueB, numFeaturesDecB, te[type3], trueTable, decTable)))
		output4.write(str(trueOrDecC))
		output5.write(str(trueOrDecU))
		output6.write(str(trueOrDecB))
		output.write(str(te["IsTrue"]))
	else:
		output1.write(str(SVM.getTrueOrDeceptive(type1, numFeaturesTrueC, numFeaturesDecC, te[type1], trueTable, decTable))+"\n")
		output2.write(str(SVM.getTrueOrDeceptive(type2, numFeaturesTrueU, numFeaturesDecU, te[type2], trueTable, decTable))+"\n")
		output3.write(str(SVM.getTrueOrDeceptive(type3, numFeaturesTrueB, numFeaturesDecB, te[type3], trueTable, decTable))+"\n")
		output4.write(str(trueOrDecC)+"\n")
		output5.write(str(trueOrDecU)+"\n")
		output6.write(str(trueOrDecB)+"\n")
		print te.keys()
		output.write(str(te["IsTrue"])+"\n")

output1.close()
output2.close()
output3.close()

output4.close()
output5.close()
output6.close()
print "Done evaluating"


#for Validation set...at same time create textfile with true answers so we can calculate our percentages...

