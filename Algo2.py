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

    print (ar , ar[first:last+1], maxSum)

maxSubArray([1, 2, 4, -1, 4, -10, 4, -19, 18, -1, -3, -4, 11, 3, -20, 19, -33, 50, 66, -22, -4, -55, 91, 100, -102, 9, 10, 19, -10, 10, 11, 11, -10, -18, 50, 90])
maxSubArray([12, 12, 14, -88, -1, 45, 6, 8, -33, 2, 8, -9, -33, -8, -23, -77, -89, 1, 9, 10, 92, 87])
maxSubArray([565, 78, 33, 9, 10, 84, 71, -4, -22, -55, -10, 76, -9, -9, -11, 76, 89, 11, 10, -33, 9])
maxSubArray([2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
maxSubArray([2])
maxSubArray([-1, -1, -1, -1, -1, -100, -10, -10, 100, 100, 100, 100, -100, 100, 10, -10, -1])
maxSubArray([12, 23, 44, -17, 12, 14, -88, -1, 45, 6, 8, -33, 2, 8, -9, -33, -8, -23, -77, -89, 1, 9, 13, -25, 10, 92, 57, 99, -22])