#knn.py
from __future__ import division
import math
import sys

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
    dist = calc_distance(test,t)
    if val > dist:
      min_dist[index] = dist
      min_ind[index] = i
  return zip(min_ind, min_dist)
  







