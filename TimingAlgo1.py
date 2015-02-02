import random
from timeit import default_timer as timer

n=500

def maxSubArray(ar):
    tempSum=maxSum=ar[0]
    i=0
    first=last=0

    for i in range(0,len(ar)):
        for j in range(i,len(ar)):
            tempSum=sum(ar[i:j])
            if tempSum > maxSum:
                first=i
                last=j
                maxSum=tempSum



ar1=[]
ar2=[]
ar3=[]
ar4=[]
ar5=[]
ar6=[]
ar7=[]
ar8=[]
ar9=[]
ar10=[]

for x in range(0,n):
    ar1.append(random.randint(-100, 100))
    ar2.append(random.randint(-100, 100))
    ar3.append(random.randint(-100, 100))
    ar4.append(random.randint(-100, 100))
    ar5.append(random.randint(-100, 100))
    ar6.append(random.randint(-100, 100))
    ar7.append(random.randint(-100, 100))
    ar8.append(random.randint(-100, 100))
    ar9.append(random.randint(-100, 100))
    ar10.append(random.randint(-100, 100))

start = timer()
maxSubArray(ar1)
maxSubArray(ar2)
maxSubArray(ar3)
maxSubArray(ar4)
maxSubArray(ar5)
maxSubArray(ar6)
maxSubArray(ar7)
maxSubArray(ar8)
maxSubArray(ar9)
maxSubArray(ar10)
end = timer()
print(end-start)