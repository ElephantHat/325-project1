def maxSubArray(ar):
    tempSum=maxSum=0
    i=0
    first=last=0

    for i in range(0,len(ar)):
        tempSum=ar[i]
        if tempSum>maxSum:
                    first=i
                    last=i
                    maxSum=tempSum
        for j in range(i+1,len(ar)):
            tempSum=tempSum+ar[j]
            if tempSum>maxSum:
                    first=i
                    last=j
                    maxSum=tempSum

    return (ar[first:last+1], maxSum)
