def arrayMaxConsecutiveSum(inputArray, k):
    ans = 0
    for i in range(0, len(inputArray)-k+1):
        result = 0
        for j in range(i, i+k):
            result += inputArray[j]
        if ( result > ans ):
            ans = result
    return ans