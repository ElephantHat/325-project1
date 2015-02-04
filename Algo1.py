def maxSubArray(ar):
    tempSum=maxSum=ar[0]
    first=last=0

    for i in range(len(ar)):
        for j in range(i,len(ar)):
            tempSum=sum(ar[i:j+1])
            if tempSum > maxSum:
                first=i
                last=j
                maxSum=tempSum

    return (ar[first:last+1], maxSum)
