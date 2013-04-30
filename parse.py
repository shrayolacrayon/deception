#Word N-gram
#Character n-gram
#Part of speech
import nltk
import numpy
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from collections import Counter
import time
start_time = time.time()

f = open('train', 'r');
s=f.read();
train=[]
k=0
le=len(s.split("\n"))
print "Reading training data..."
uniAll=[]
bigAll=[]
charAll=[]
posAll=[]
co= 0
for sent in s.split("\n"):
    parts=sent.split(",")
    toks=[word_tokenize(t) for t in sent_tokenize(parts[2])]
    uni=[]
    big=[]
    char=[]
    pos=[]
    for t in sent_tokenize(parts[2]):
        for i in range(len(t)-2):
            trig=t[i]+t[i+1]+t[i+2]
            char.append(trig)
            if not trig in charAll:
                charAll.append(trig)
    for sen in toks:
        #add POS
        tags=nltk.pos_tag(sen)
        for x in tags:
            pos.append(x[1])
            if not x[1] in posAll:
                posAll.append(x[1])
        #add uni
        for i in range(len(sen)):
            curr=sen[i]
            uni.append(curr);
            if not curr in uniAll:
                uniAll.append(curr);
            #add big
            if i!=len(sen)-1:
                nex=sen[i+1]
                bigval=curr+" "+nex
                big.append(bigval)
                if not bigval in bigAll:
                    bigAll.append(bigval)  
    uniDist=Counter(uni)
    bigDist=Counter(big)
    charDist=Counter(char)
    posDist=Counter(pos)
    if not (co%10 == 0 or co%10 == 5):
        train.append({"IsTrue":parts[0],"IsPos":parts[1], "text":parts[2], "pos":pos, "uni":uni, "big":big,"char":char,"uniDist":uniDist,"bigDist":bigDist,"charDist":charDist, "posDist":posDist})
    co+=1
    if k==le/4:
        print "25% done"
    if k==le/2:
        print "50% done"
    if k==le*3/4:
        print "75% done"
    k=k+1

print "Building aggregate data..."
labels=["uni","big","char","pos"]
Pos={"uni":[],"big":[],"char":[],"pos":[]}
Neg={"uni":[],"big":[],"char":[],"pos":[]}
Dec={"uni":[],"big":[],"char":[],"pos":[]}
Real={"uni":[],"big":[],"char":[],"pos":[]}
PosReal={"uni":[],"big":[],"char":[],"pos":[]}
NegReal={"uni":[],"big":[],"char":[],"pos":[]}
PosDec={"uni":[],"big":[],"char":[],"pos":[]}
NegDec={"uni":[],"big":[],"char":[],"pos":[]}
k=0
p=0
tr=0
de=0
for rev in train:
    p=p+1
    if rev["IsTrue"]=="1":
        tr=tr+1
        for l in labels:
            Real[l].extend(rev[l])
        if rev["IsPos"]=="0":
            for l in labels:
                PosReal[l].extend(rev[l])
                Pos[l].extend(rev[l])
        else:
            for l in labels:
                NegReal[l].extend(rev[l])
                Neg[l].extend(rev[l])
    else:
        de=de+1
        for l in labels:
            Dec[l].extend(rev[l])
        if rev["IsPos"]=="0":
            for l in labels:
                PosDec[l].extend(rev[l])
                Pos[l].extend(rev[l])
        else:
            for l in labels:
                NegDec[l].extend(rev[l])
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
print "done"

#---------------------------------------------#
print ("building distribution tables...")
for rev in train:
    uniVec,bigVec,charVec,posVec=[],[],[],[]
    uniVecBIN,bigVecBIN,charVecBIN,posVecBIN=[],[],[],[]
    for tok in uniAll:
        if tok in rev["uniDist"]:
            uniVec.append(rev["uniDist"][tok])
            uniVecBIN.append(1)
        else:
            uniVec.append(0)
            uniVecBIN.append(0)
    for tok in bigAll:
            if tok in rev["bigDist"]:
                bigVec.append(rev["bigDist"][tok])
                bigVecBIN.append(1)
            else:
                bigVec.append(0)
                bigVecBIN.append(0)
    for tok in charAll:
            if tok in rev["charDist"]:
                charVec.append(rev["charDist"][tok])
                charVecBIN.append(1)
            else:
                charVec.append(0)
                charVecBIN.append(0)
    for tok in posAll:
            if tok in rev["posDist"]:
                posVec.append(rev["posDist"][tok])
                posVecBIN.append(1)
            else:
                posVec.append(0)
                posVecBIN.append(0)
            rev["uniVec"]=uniVec
            rev["bigVec"]=bigVec
            rev["charVec"]=charVec
            rev["uniVecBIN"]=uniVecBIN
            rev["bigVecBIN"]=bigVecBIN
            rev["charVecBIN"]=charVecBIN
            rev["posVec"]=posVecBIN
            rev["posVecBIN"]=posVecBIN
print "DONE"

def numocc(token, table_name, table_type):
    if token in table_name[table_type]:
        return table_name[table_type][token]
    else:
        return 0
f= open('Validation', 'r');
s=f.read();
test=[]
k=0
le=len(s.split("\n"))
print "Reading testing data..."
for sent in s.split("\n"):
    parts=sent.split(",")
    toks=[word_tokenize(t) for t in sent_tokenize(parts[2])]
    uni=[]
    big=[]
    char=[]
    for t in sent_tokenize(parts[2]):
        for i in range(len(t)-2):
            trig=t[i]+t[i+1]+t[i+2]
            char.append(trig)
    for sen in toks:
        #add uni
        for i in range(len(sen)):
            curr=sen[i]
            uni.append(curr);            
            #add big
            if i!=len(sen)-1:
                nex=sen[i+1]
                bigval=curr+" "+nex
                big.append(bigval)
    uniDist=Counter(uni)
    bigDist=Counter(big)
    charDist=Counter(char)
    #vectorize:
    test.append({"IsTrue":parts[0],"IsPos":parts[1], "text":parts[2], "pos":pos, "uni":uni, "big":big,"char":char,"uniDist":uniDist,"bigDist":bigDist,"charDist":charDist, "posDist":posDist})
    if k==le/4:
        print "25% done"
    if k==le/2:
        print "50% done"
    if k==le*3/4:
        print "75% done"
    k=k+1
print "DONE"
print ("building test VECTORS...")
for rev in test:
    uniVec,bigVec,charVec=[],[],[]
    uniVecBIN,bigVecBIN,charVecBIN,=[],[],[]
    for tok in uniAll:
        if tok in rev["uniDist"]:
            uniVec.append(rev["uniDist"][tok])
            uniVecBIN.append(1)
        else:
            uniVec.append(0)
            uniVecBIN.append(0)
    for tok in bigAll:
            if tok in rev["bigDist"]:
                bigVec.append(rev["bigDist"][tok])
                bigVecBIN.append(1)
            else:
                bigVec.append(0)
                bigVecBIN.append(0)
    for tok in charAll:
            if tok in rev["charDist"]:
                charVec.append(rev["charDist"][tok])
                charVecBIN.append(1)
            else:
                charVec.append(0)
                charVecBIN.append(0)
            rev["uniVec"]=uniVec
            rev["bigVec"]=bigVec
            rev["charVec"]=charVec
            rev["uniVecBIN"]=uniVecBIN
            rev["bigVecBIN"]=bigVecBIN
            rev["charVecBIN"]=charVecBIN
print "DONE"
print time.time() - start_time, "seconds"
#-----------------------------------#
#COPY THIS WHOLE FILE AND WRITE YOUR CODE HERE!

#-----------------------------------#
#COPY THIS WHOLE FILE AND WRITE YOUR CODE HERE!


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
    return RealDist, DecDist, PosRealDist, NegRealDist, PosDecDist, NegDecDist, PosDist, NegDist,

def testingData():
    return test
