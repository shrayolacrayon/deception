#knn.py
from future import division
import math

def calc_distance(vector1, vector2):
  s = 0
  for i,v in enumerate(vector1):
    s += ((v - vector2[i]) ** 2)
  return math.sqrt(s)

def find_nearest(test, train_set):
  pass

calc_distance([1,0,0,0,0], [0,0,0,0,0])
