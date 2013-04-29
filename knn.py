#knn.py
from __future__ import division
import math
import sys
import parse2
from scipy.spatial.distance import euclidean

def calc_distance(vector1, vector2):
  s = 0
  for i,v in enumerate(vector1):
    s += ((v - vector2[i]) ** 2)
  return math.sqrt(s)

def find_nearest(test, train_set, k):
  min_dist = [float(sys.maxint)] * k
  min_ind = [0] * k
  for i,t in enumerate(train_set):
    #index of maximum value
    index = min_dist.index(max(min_dist))
    val = max(min_dist)
    dist = euclidean(test,t)
    if val > dist:
      min_dist[index] = dist
      min_ind[index] = i
  return (min_ind, min_dist)

def pick_closest(train_set,test, mins, method):
  dec = 0
  truth = 0
  min_ind, min_dis = mins
  if method == 1:
    for m in min_ind:
      print train_set[m]["isPos"]
      if train_set[m]["IsPos"] == 0:
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
test, train = parse2.knn_distributions()

def calc_nearest(baseline, trains, train):
  tests = []
  for review in test:
    b = baselines[baseline]
    mins = find_nearest(review[b], trains[baseline],1)
    p = pick_closest(train, review, mins, 1)
    print p
    tests.append(p)
  return tests
def create_trains(train):
  trains = []
  for b in baselines:
    t = compile_train(b,train)
    trains.append(t)
  return trains

trains = create_trains(train)
for t in train:
  print t["IsPos"]

print calc_nearest(0, trains, train)






    








