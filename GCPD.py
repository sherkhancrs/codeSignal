def isPrime(x) : 
    if (x <= 1) : 
        return False
    if (x <= 3) : 
        return True
    if (x % 2 == 0 or x % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= x) : 
        if (x % i == 0 or x % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def findDividers(n):
    divider = 2;
    aDividers = []
    if (isPrime(n)):
        return [n]
    while n != 1:
        if (n%divider)==0:
            aDividers.append(divider)
            n = n/divider
        else:
            divider+=1
    return aDividers

def greatestCommonPrimeDivisor(a, b):
    listA = (findDividers(a))
    listB =(findDividers(b))
    print(listA, listB)
    adividersSet = set()
    bdividersSet = set()
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] == listB[j]:
                adividersSet.add(listA[i])
                bdividersSet.add(listB[j])
    print(adividersSet)
    print(bdividersSet)
    spisok = []
    for x in adividersSet:
       if (isPrime(x)):
           spisok.append(x)
    print(spisok)
    if (len(spisok) != 0):
        return max(spisok)
    else:
        return -1
