def arrayChange(inputArray):
  count = 0;
  for i in range(len(inputArray)-1):
    if inputArray[i+1]<=inputArray[i]:
      while inputArray[i+1]<=inputArray[i]:
        inputArray[i+1]+=1
        count+=1
      
  return count

print(arrayChange([-1000, 0, -2, 0]))