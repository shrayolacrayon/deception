#Word N-gram
#Character n-gram
#Part of speech
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from collections import Counter

f = open('Train', 'r');
s=f.read();
train=[]
k=0
le=len(s.split("\n"))
print "Reading training data..."
for sent in s.split("\n"):
    parts=sent.split(",")
    toks=[word_tokenize(t) for t in sent_tokenize(parts[2])]
    uni=[]
    big=[]
    char=[]
    for t in sent_tokenize(parts[2]):
        for i in range(len(t)-2):
            char.append(t[i]+t[i+1]+t[i+2])
    for sen in toks:
        #add uni
        for i in range(len(sen)):
            curr=sen[i]
            uni.append(curr);
            #add big
            if i!=len(sen)-1:
                nex=sen[i+1]
                big.append(curr+" "+nex)
    uniDist=Counter(uni)
    bigDist=Counter(big)
    charDist=Counter(char)
    train.append({"IsTrue":parts[0],"IsPos":parts[1], "text":parts[2], "uni":uni,"big":big,"char":char,"uniDist":uniDist,"BigDist":bigDist,"charDist":charDist})
    if k==le/4:
        print "25% done"
    if k==le/2:
        print "50% done"
    if k==le*3/4:
        print "75% done"
    k=k+1
print "DONE"

print "Building aggregate data..."
sets={"uni":[],"big":[],"char":[]}
labels=["uni","big","char"]
Pos=sets
Neg=sets
Dec=sets
Real=sets
PosReal=sets
NegReal=sets
PosDec=sets
NegDec=sets
k=0
for rev in train:
    if rev["IsTrue"]==0:
        for l in labels:
            Real[l].extend(rev[l])
        if rev["IsPos"]==0:
            for l in labels:
                PosReal[l].extend(rev[l])
                Pos[l].extend(rev[l])
        else:
            
            for l in labels:
                NegReal[l].extend(rev[l])
                Neg[l].extend(rev[l])
    else:
        for l in labels:
            Dec[l].extend(rev[l])
        if rev["IsPos"]==0:
            for l in labels:
                PosDec[l].extend(rev[l])
                Pos[l].extend(rev[l])
        else:
            for l in labels:
                PosDec[l].extend(rev[l])
                Neg[l].extend(rev[l])
    if k==le/4:
        print "25% done"
    if k==le/2:
        print "50% done"
    if k==le*3/4:
        print "75% done"
    k=k+1
print "DONE"

PosDist={}
NegDist={}
DecDist={}
RealDist={}
PosRealDist={}
NegRealDist={}
PosDecDist={}
NegDecDist={}
for l in labels:
    print "Building "+str(l)+"-Gram..."
    PosDist[l]=Counter(Pos[l])
    NegDist[l]=Counter(Neg[l])
    DecDist[l]=Counter(Dec[l])
    RealDist[l]=Counter(Real[l])
    PosRealDist[l]=Counter(PosReal[l])
    NegRealDist[l]=Counter(NegReal[l])
    PosDecDist[l]=Counter(PosDec[l])
    NegDecDist[l]=Counter(NegDec[l])

f = open('Validation', 'r');
s=f.read();
test=[]
k=0
le=len(s.split("\n"))
print "Reading testing data..."
for sent in s.split("\n"):
    parts=sent.split(",")
    #print parts[2]
    toks=[word_tokenize(t) for t in sent_tokenize(parts[2])]
    uni=[]
    big=[]
    char=[]
    for t in sent_tokenize(parts[2]):
        for i in range(len(t)-2):
            char.append(t[i]+t[i+1]+t[i+2])
    for sen in toks:
        #add uni
        for i in range(len(sen)):
            curr=sen[i]
            uni.append(curr);
            #add big
            if i!=len(sen)-1:
                nex=sen[i+1]
                big.append(curr+" "+nex)
    uniDist=Counter(uni)
    bigDist=Counter(big)
    charDist=Counter(char)
    test.append({"IsTrue":parts[0],"IsPos":parts[1], "text":parts[2], "uni":uni,"big":big,"char":char,"uniDist":uniDist,"BigDist":bigDist,"charDist":charDist})
    if k==le/4:
        print "25% done"
    if k==le/2:
        print "50% done"
    if k==le*3/4:
        print "75% done"
    k=k+1
print "DONE"

#def numocc(token, table_name, table_type):
    #if token in table_name[table_type]
        #return table_name[table_type][token]
    #else return 0
#-----------------------------------#
#COPY THIS WHOLE FILE AND WRITE YOUR CODE HERE!

#return knn distributions
def knn_distributions():
    return PosDist,NegDist

def svm_buckets():
    return RealDist, DecDist, PosRealDist, NegRealDist, PosDecDist, NegDecDist, PosDist, NegDist

def testingData():
    return test
