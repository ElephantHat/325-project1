#!/usr/bin/python
import json
import fileinput
import Algo1 as alg1
import Algo2 as alg2
import Algo3 as alg3

A=[]
f = open('MSS_Results.txt', 'w')

for line in fileinput.input():
    value = line.strip('\[\]\n ').split(',')
    A.append([int(x) for x in value])


f.write("Test results for Algorithm 1\n")

for ar in A:
    (subarray, maxSum) = alg1.maxSubArray(ar)
    f.write(json.dumps(ar) +", " + json.dumps(subarray) +", "+ str(maxSum)+"\n")

f.write("\n\nTest results for Algorithm 2\n")

for ar in A:
    (subarray, maxSum) = alg2.maxSubArray(ar)
    f.write(json.dumps(ar) +", " + json.dumps(subarray) +", "+ str(maxSum)+"\n")

f.write("\n\nTest results for Algorithm 3\n")

for ar in A:
    (low, high, maxSum) = alg3.maxSubArray(ar, 0, len(ar)-1)
    f.write(json.dumps(ar) +", " + json.dumps(ar[low:high+1]) +", "+ str(maxSum)+"\n")

f.close()
