def isOneSwapEnough(inputString):
  arr1 = []
  if isPolindrome(inputString):
    return True
  else:
    arr1 = list(inputString)
    for i in range(len(inputString)):
      for j in range(i+1, len(inputString)):
        newArr = arr1.copy()
        newArr[i] = inputString[j]
        newArr[j] = inputString[i]
        if (isPolindrome("".join(newArr))):
          return True
    return False


def isPolindrome(inputString):
  inv = ""
  for i in range(len(inputString)-1, -1, -1):
    inv=inv+inputString[i]
  if (inputString == inv):
    return True
  else:
    return False
  
result = isOneSwapEnough("abab")

print(result)

