ar = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]


def maxCross(ar, low, mid, high):
    leftSum = 0
    tempSum = 0
    leftHigh = mid
    for i in range(mid+1, low, -1):
        tempSum = tempSum + ar[i]
        if tempSum > leftSum:
            leftSum = tempSum
            leftHigh = i

    rightSum = 0
    tempSum = 0
    rightHigh = mid+1
    for j in range(mid+1, high):
        tempSum = tempSum + ar[j]
        if tempSum > rightSum:
            rightSum = tempSum
            rightHigh = j

    return(leftHigh, rightHigh, leftSum+rightSum)


def maxSubArray(ar, low, high):
    if high == low:
        return(low, high, ar[low])
    else:
        mid = (high + low)/2
        (leftLow, leftHigh, leftSum) = maxSubArray(ar, low, mid)
        (rightLow, rightHigh, rightSum) = maxSubArray(ar, mid+1, high)
        (crossLow, crossHigh, crossSum) = maxCrossing(ar, low, mid, high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return(leftLow, leftHigh, leftSum)
    elif rightSum >= leftSum and rightSum >= crossSum:
        return(rightLow, rightHigh, rightSum)
    else:
        return(crossLow, crossHigh, crossSum)

(low, high, maxSum) = maxSubArray(ar, 0, len(ar)-1)

print(ar, ar[low:high], maxSum)
  

