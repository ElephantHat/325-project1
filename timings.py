import Algo1 as alg1
import Algo2 as alg2
import Algo3 as alg3

import random
import datetime

#build arrays of random numbers
A=[]
for h in range(10):
    A.append([])
    for i in range(100, 1000, 100):
        ar=[]
        for j in range(i):
            ar.append(random.randint(-100, 100))
        A[h].append(ar)

    for i in range(1000, 10000, 1000):
        ar=[]
        for j in range(i):
            ar.append(random.randint(-100, 100))
        A[h].append(ar)

#do timings
al1 = al2 = al3 = al4 = []

for h in range(len(A)):
    al1.append({})
    al2.append({})
    al3.append({})
    al4.append({})
    for i in range(len(A[h])):
        #Algorithm 1
        if i > 9:
            time1 = datetime.datetime.utcnow()
            alg1.maxSubArray(A[h][i])
            time2 = datetime.datetime.utcnow()
            finaltime = (time2 - time1)
            al1[h][len(A[h][i])] = finaltime.microseconds
        else:
            al1[h][len(A[h][i])] = 0



        #Algorithm 2
        time1 = datetime.datetime.utcnow()
        alg2.maxSubArray(A[h][i])
        time2 = datetime.datetime.utcnow()
        finaltime = (time2 - time1)
        al2[h][len(A[h][i])] = finaltime.microseconds

        #Algorithm 3
        time1 = datetime.datetime.utcnow()
        alg3.maxSubArray(A[h][i], 0, len(A[h][i])-1)
        time2 = datetime.datetime.utcnow()
        finaltime = (time2 - time1)
        al3[h][len(A[h][i])] = finaltime.microseconds


#get averages for alg1
averages = {}
for i in range(100, 1000, 100):
    averages[i] = 0

for i in range(1000, 10000, 1000):
    averages[i] = 0

total = 0
for i in al1:
    total+=1
    for j in range(100, 1000, 100):
        averages[j] += i[j]

    for j in range(1000, 10000, 1000):
        averages[j] += i[j]

for i in averages:
    for j in range(100, 400, 100):
        i[j] = i[j]/total

    for j in range(1000, 10000, 1000):
        i[j] = i[j]/total

print "Algorithm 1 Timings : ", al1
print "Algorithm 1 Averages: ", averages

#get averages for alg2
averages = {}
for i in range(100, 1000, 100):
    averages[i] = 0

for i in range(1000, 10000, 1000):
    averages[i] = 0

total = 0
for i in al2:
    total+=1
    for j in range(100, 1000, 100):
        averages[j] += i[j]

    for j in range(1000, 10000, 1000):
        averages[j] += i[j]

for i in averages:
    for j in range(100, 400, 100):
        i[j] = i[j]/total

    for j in range(1000, 10000, 1000):
        i[j] = i[j]/total

print "Algorithm 2 Timings : ", al2
print "Algorithm 2 Averages: ", averages

#get averages for alg3
averages = {}
for i in range(100, 1000, 100):
    averages[i] = 0

for i in range(1000, 10000, 1000):
    averages[i] = 0

total = 0
for i in al3:
    total+=1
    for j in range(100, 1000, 100):
        averages[j] += i[j]

    for j in range(1000, 10000, 1000):
        averages[j] += i[j]

for i in averages:
    for j in range(100, 400, 100):
        i[j] = i[j]/total

    for j in range(1000, 10000, 1000):
        i[j] = i[j]/total

print "Algorithm 3 Timings : ", al3
print "Algorithm 3 Averages: ", averages

