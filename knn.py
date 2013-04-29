#knn.py
from __future__ import division
import math
import sys
import parse3
#from scipy.spatial.distance import euclidean

def calc_distance(vector1, vector2):
  s = 0
  for i,v in enumerate(vector1):
    s += ((v - vector2[i]) ** 2)
  return math.sqrt(s)

def hamming_distance(vector1, vector2):
  diffs = 0
  for (p1,p2) in zip(vector1,vector2):
    if p1 != p2:
      diffs +=1 
  return diffs

def reduced_hamming(vector1,vector2, amt):
  diffs = 0
  diff = int(len(vector1)/amt)
  i = 0
  while i < len(vector1):
    if vector1[i] != vector2[i]:
      diffs += 1
    i = i+ diff
  return diffs


def find_nearest(test, train_set, k):
  min_dist = [float(sys.maxint)] * k
  min_ind = [0] * k
  for i,t in enumerate(train_set):
    #index of maximum value
    index = min_dist.index(max(min_dist))
    val = max(min_dist)
    dist = reduced_hamming(test,t, 50)
    if val > dist:
      min_dist[index] = dist
      min_ind[index] = i
  return (min_ind, min_dist)

def pick_closest(train_set,test, mins, method):
  dec = 0
  truth = 0
  min_ind, min_dis = mins
  if method == 1:
    print "Min_ind"
    for m in min_ind:
      if str(train_set[m]["IsTrue"]) == '0':
        dec += 1
      else:
        truth += 1
    if dec >= truth:
      return 0
    else: 
      return 1


    

def compile_train(gram_type, train):
  new_train_list = []
  for t in train:
    new_train_list.append(t[gram_type])
  return new_train_list


baselines = ["uniVec", "bigVec", "charVec", "uniVecBIN", "bigVecBIN", "charVecBIN"]
test, train = parse.knn_distributions()

def calc_nearest(baseline, trains, train):
  tests = []
  length = len(test)
  k = 0
  for review in test:
    b = baselines[baseline]
    mins = find_nearest(review[b], trains[baseline],3)
    p = pick_closest(train, review, mins, 1)
    print p
    tests.append(p)
    if k==length/4:
        print "25% done"
    if k==length/2:
        print "50% done"
    if k==length*3/4:
        print "75% done"
    k=k+1
  return tests
def create_trains(train):
  trains = []
  for b in baselines:
    t = compile_train(b,train)
    trains.append(t)
  return trains

trains = create_trains(train)
#print "LENGTH"
#print len(trains[0])
print "Starting knn.."#
nearest= calc_nearest(3, trains, train)
print nearest
out = open ("uniBIN.txt",'w')
for n in nearest:
  out.write(str(n))







    








