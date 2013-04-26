import random


#First State Machine Bigram words
def getTrueOrDeceptive(type1, numFeaturesTrue, numFeaturesDec, reviewFeatures, trueTable, decTable):
	
	truth= 0
	deception= 0
	#print "I am the true features: %i, and I am deception features: %i"% (numFeaturesTrue, numFeaturesDec)
	for feature in reviewFeatures:
		trueNum= trueTable[type1][feature]
		#totalTrueNum= getTotalCountFeature(type1, trueTable)
		trueProb= trueNum/float(numFeaturesTrue)

		decNum= decTable[type1][feature]
		#totalDecNum= getTotalCountFeature(type1, decTable)
		decProb= decNum/float(numFeaturesDec)

		if trueProb > decProb:
			truth= truth + 1
		elif trueProb < decProb:
			deception= deception + 1
		else:
			# what to do if the probabilities are equal
			truth= truth + 1
			deception= deception + 1


	if truth > deception:
		print "I am most definitely True!!!!!!!!!!!!!!!!!!!!!!"
		return 1
		
	elif truth < deception:
		print "I am most definitely FALSE AND DECEITFUL!!s"
		return 0
		
	else:
		
		if numFeaturesTrue > numFeaturesDec:
			print "WOOOOOOOOHHHHHHOOOOOOOO"
			return 1
			
		elif numFeaturesTrue < numFeaturesDec:
			print "SHIIIIIIIIIIIIIIITTTTTTTTTTTTTT"
			return 0
			
		else:
			decidingFactor= random.random()
			if 0.5 >= decidingFactor:
				#print "I'm only RANDOM"
				return 1
				
			else:
				return 0
		

