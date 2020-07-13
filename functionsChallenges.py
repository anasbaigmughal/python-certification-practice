print("\nWARM UP SECTION")
print("===============")

def lesserOfTwoEvens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
print("Lesser of Two Evens Result: {}".format(lesserOfTwoEvens(2, 5)))

def animalCrackers(text):
    list1 = text.split(" ")
    if (list1[0])[0] == (list1[1])[0]:
        return True
    else:
        return False
print("Animal Crackers Result: {}".format(animalCrackers("Zebra Horse")))

def makesTwenty(n1, n2):
    if n1+n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
print("Makes Twenty Result: {}" .format(makesTwenty(2, 3)))

print("\nLEVEL 1 PROBLEMS")
print("================")

def oldMacdonald(name):
    changedName = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return changedName
print("Old MacDonald Result: {}".format(oldMacdonald("macdonald")))

def masteryoda(text):
    list1 = text.split(" ")
    return " ".join(list1[::-1]) #" "means to place spaces in between elements to be joined
print("Master Yoda Result: {}".format(masteryoda("I am home")))

def almostThere(n):
    n = abs(n)
    if n>=90 and n<=110:
        return True
    elif n>=190 and n<=210:
        return True
    else:
        return False
    return True
print("Almost There Result: {}".format(almostThere(209)))

print("\nLEVEL 2 PROBLEMS")
print("================")

def find33(nums):
    limit = len(nums)
    i = 0
    while i < limit:
        if nums[i] == 3 and i < limit-1:  #limit to check i is not last element
            if  nums[i+1] == 3:
                return True
        i += 1
    return False
print("Find 33 Result: {}".format(find33([3, 1, 3])))

def paperDoll(text):
    i = 0
    resultText = ""
    while i < len(text):
        resultText += (text[i]*3)
        i += 1
    return resultText
print("Paper Doll Result: {}".format(paperDoll("Hello")))

def blackJack(a, b, c):
    sum = a+b+c
    if sum <= 21:
        return sum
    else:
        if a == 11 or b == 11 or c == 11:
            sum = sum-10
            if sum > 21:
                return "BUST"
            else:
                return sum
        else:
            return "BUST"
print("Black Jack Result: {}".format(blackJack(9, 9, 11)))

def summerOf69(arr):
    sum = 0
    skipFlag = False
    for i in arr:
        if i != 6 and skipFlag != True:
            sum += i
        elif i==6:
            skipFlag = True
        elif skipFlag:
            if i ==  9:
                skipFlag = False
    return sum
print("Summer of '69 Result: {}".format(summerOf69([2, 1, 6, 9, 11])))

print("\nCHALLENGING PROBLEMS")
print("====================")

def spyGame(nums):
    trueChars = 0
    for i in nums:
        if i == 0:
            if trueChars == 0: #already detected ' '
                trueChars = 1 #now already detected '0'
            if trueChars == 1: #already detected '0'
                trueChars = 2 #now already detected '00'
        if i == 7 and trueChars == 2: #now already detected '007'
            return True
    return False
print("Spy Game Result: {}".format(spyGame([1,0,2,4,0,5,7])))

def countPrimes(num):
    primeCount = 0
    list1 = range(2, num)
    for i in list1:
        j = 2
        primeFlag = True
        while j < i:
            if i%j == 0:
                primeFlag = False
            j += 1
        if primeFlag:  
            primeCount += 1
    return primeCount
print("Count Primes Result: {}".format(countPrimes(100)))

def justForFun(letter):
    dict1 = {'a':"  *\n * *\n*****\n*   *\n*   *\n", 'b':"****\n*   *\n****\n*   *\n****\n", 'c':" ****\n*\n*\n*\n ****\n", 'd':"****\n*   *\n*   *\n*   *\n****\n", 'e':"*****\n*\n****\n*\n*****\n",}
    return dict1[letter]
print("Just For Fun Result: \n\n{}".format(justForFun("c")))