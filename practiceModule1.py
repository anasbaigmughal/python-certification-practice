from random import randint
from random import shuffle
import math
karachi = 1411
lahore = 377
quetta = 912
if karachi < lahore and karachi < quetta:
    print("Karachi is closest")
elif lahore < karachi and lahore < quetta:
    print("Lahore is closest")
else:
    print("Quetta is closest")


def myFunc(n):
    print("Muhammad Anas Baig")
    name = 'Anas'
    print('Hello %s' % (name))
    return n+1


print('Returned Value from Function %s' % (myFunc(4)))


def isPrime(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
        else:
            print(num, 'is prime')
            break


isPrime(111)


def isPrime1(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % 1 == 0:
            return False
    return True


print(isPrime1(18))

print('hello \n world')
names = "Muhammad Anas Baig"
length = len(names)
print(length)
print(names[5])
print(names[8:13])  # [start:end] slicing
print(names[::-1])  # to reverse a string
names = names + ' Mughal'
print(names)
print(names[0:100])  # index out of range but no error
# print(names[100]) #index out of range error
print(names.upper())
print(names.lower())
print(names.split(" "))  # split at " " space, or "*"
print("My name is: {}" .format(names))  # just like %s place holder
list1 = [1, 2, 3, 4, 5, 6]
# creates list of numbers second argument is not included in list elements
list2 = range(2, 7)
for num in list1:
    print(num)
print("after")
for num in list2:
    print(num)
listSum = 0
for num in list2:
    listSum += num
print("sum:")
print(listSum)
str = "Muhammad Anas Baig"
for letter in str:
    print(letter, end='')
list2 = [(2, 4), (6, 8), (10, 12)]

for tup in list2:
    print(tup)

for(t1, t2) in list2:  # picks only X values but not Y
    print(t1)

d = {'key1': 1, 'key2': 2, 'key3': 3}
print(d.items())
for item in d:
    print(item)
for k, v in d.items():
    print(k)
    print(v)
print(list(d.keys()))
print(sorted(d.values()))


def greater(a, b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")


greater(5, 21)


def capitalizeMe(str):
    return str.upper()


print(capitalizeMe("anas"))


def reverseMe(str):
    return str[::-1]


print(reverseMe("anas"))

print("NEXT")


def representThreeTimes(str):
    for n in str:
        for m in range(0, 3):
            print(n, end='')


representThreeTimes("anas")

print("\nNEXT")


def representThreeTimes1(str):
    for n in str:
        print(n*3, end='')


representThreeTimes1("anas")

print("\nNEXT")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def countPrimeNumbers(list1):
    primeCount = 0
    for n in list1:
        if num % n == 0:
            primeCount += 1
    print("Prime Count")
    print(primeCount)


countPrimeNumbers(list1)

# generate list between 0-100 with increment of 11
print(list(range(0, 100, 11)))

indexCount = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(indexCount, letter))
    indexCount += 1


def a():
    print("\nNEXT")


print("\nNEXT")
for i, letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i, letter))

a()
print(list(enumerate('abcde')))

a()
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(list2, list3)))  # packing/unpacking