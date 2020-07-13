def a():
    print("\nNEXT")
    
list1 = ['1', '2', '3', '4']
s = "-"

a()
s = s.join(list1)
print(s)
print(s.split("-"))

a()
list1 = ['1', '2', '3', '4']
list2 = ['a', 'b', 'c', 'd']
y = list(range(0, 100, 10))
# making list from range is very fast

print(list(zip(list1, list2)))

shuffle(list1)  # shuffles list in place
print(list1)

print(randint(0, 100))

#yourName = input("Enter your name: ")
# print(yourName.upper())

listMixed = ['Anas', 5, True]
print(len(listMixed))
print(listMixed[0:])
listMixed = listMixed+['Another']
print(listMixed*2)
listMixed.append("append me")
print(listMixed)

shuffle(listMixed)
print(listMixed.pop())
print(listMixed)
listMixed.reverse()  # in place reverse
print(listMixed)

# listMixed.sort() #not possible in str and int mixed elements string

list1 = [1, 2, 3, 3, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

matrix = [list1, list2, list3]
a()
print(matrix[0][1])

firstColumn = [row[0] for row in matrix]
a()
print(firstColumn)

# using list comprehension extract row or column from matrix
print(matrix[0])
print(list1.count(3))
help(list1.count)

x = 0
while x < 10:
    print("x is currently:", x, "dsd")
    print("x is still less than 10, adding 1 to x")
    x += 1
    if x == 3:
        print("x==3")
        pass
    else:
        print("continuing")
        continue
    x += 2

lst = [x**2 for x in range(0, 10) if x % 2 == 0]
#range(0,10) == range(10)
print(lst)

cels = [0, 10, 20.1, 34.5]
print(cels)
far = [((9/5)*temp + 32) for temp in cels]
print(far)

a()
lst = [x**2 for x in [x**2 for x in range(4)]]
print(lst)

# DICTIONARIES

d = {'key1': 'value1', 'key2': [0, 1, 2], 'key3': ['item0', 'item1', 'item3']}
a()
print(d)
print(d['key3'][2].upper())

d1 = {'key1': {'nestKey': {'subNestKey': 'valueSubNestKey1'}}}
print(d1['key1']['nestKey']['subNestKey'])
print(d.keys())
# d.clear() #clear all values of dictionary
print(d.values())
# print(type(d))

a()
if d.get('keyN') == None:
    print("Not found")
a()
print(d.pop('keyN', -1))  # return -1 if no pop item

d2 = {'key4': 200, 'key5': 300}
d.update(d2)  # append new items
print(d)

a()
x = set()
print(x)
x.add(1)
print(x)
x.add(2)
x.add(2) #does not add new 2 as 2 is already present
print(x)

list1 = [1,1,2,3,4,3,4,2,1]
print(set(list1)) #print only unique items

b = None
print(type(b))
b = 112
print(type(b))
print(b)

for i in x:
    print(i)
print(4 in x) #checks either number is present in set or not

x.update([0])
x.update(['a'])
x.update('a')
print(x)

import itertools

smallSet = set(itertools.islice(x, 2)) #to slice sets
print(smallSet)

#remove, discard methods difference

y  = {'a','b', 'c','d'}
set3 = x.union(y)
print(set3)
x,y = 'islamabad', 'something'
print("I am this %s person %s" %('something','second value'), end=' ')
print("I am this %s person %s" %(x, y), end=' ')
print("nothing new")
print('my name is: %s' %'An \t as') #evaluates escape sequences with %s => s for string
print('my name is: %r' %'An \t as') #does not evaluate escape sequences with %r => r for representation
print('I want to change %s' %3.75)
print('I want to change %d' %3.75) #d for int
print('floating point numbers: %15.1f' %(12.145)) #15 means print in how many boxes, .2f means how many digits after decimal
print('This is a string using format {}'.format('formatValue'))
print('This is a-{2} b-{0} c-{1}'.format('x','y','z'))

a=5
b=10
print(f'Five plus ten is {a+b} not {2*(a+b)}') #f solves inside variables expressions
print('Every %s good is %s' %('penny', 'penny')) #one value many times
print('Every {p} good is {p}' .format(p='penny')) #one value many times

#table
#^ for center align, similarly > and < symbols
print('{0:=<8} | {1:^9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:^9}'.format('Apple', '3.0'))
print('{0:8} | {1:^9}'.format('Oranges', '10'))
print("This is my ten--character, two decimal number: %10.2f" %13.579)
print("This is a 0 character and two decimal number: {0:10.2f}".format(13.786))

name = '\tAnas'
print(f"My name is: {name}")
print(f"My name is: {name!r}")

num = 23.123
print("my 10 character number is: {0:10.4f}".format(num))
print(f"my 10 character number is: {num:{10}.{6}}")

#lambda and map
def square(num):
    return num**2
list1 = [1,2,3,4,5]
print(list(map(square,list1))) #map applies function to all the elements of the list

def splicer(myString):
    if len(myString)%2==0:
        return 'even'
    else:
        return myString[0]
list2 = ['anas','baig', 'mughal', 'muhammadi']
print(list(map(splicer,list2)))

def checkEven(num):
    return num%2==0
list3 = list(range(11))
print(list(filter(checkEven,list3))) #prints only where return result is true otherwise skip it

#lamba is anonymous functions
squareMe1 = lambda num: num**2
print(squareMe1(2))
nums = list(range(11))
print(list(map(lambda num: num**2, nums)))
print(list(map(squareMe1, nums)))
print(list(filter(lambda num: num%2==0, nums)))
stringCut=lambda num:num[0:3]
print(stringCut("Hello"))

def myf(a,b):
    return sum((a,b))*.05
print(myf(40,60))

def myf1(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05
print(myf1(40,60,20))

def myFun(*args): #in form of tuples, takes multiple arguments
    return sum(args)*.05
print(myFun(40,60,20,10))


def myFun1(*args, **kwargs): #keyword args, must be passed in same sequence
    if 'fruit' in kwargs:
        print(f"I like {' and '.join(args)} and my fav fruit is {kwargs['fruit']}")
        print(f"May i have some {kwargs['juice']}")
    else:
        print("I don't like fruit")
print(myFun1('eggs', 'omlet', fruit='pineapple', juice='orange'))

x=25
def printer():
    x=50
    return x
x=25
print(x)
print(printer())

#LEG rule in python

f=lambda x:x**2

name = "Global Name"
def greet():
    name="Anas"
    def hello():
        print('Hello' + name)
    hello()
print(greet())

x=50
def fun():
    global x
    print("this is now using the global X")
    print(x)
    x=2
    print("ran fun(), changes global x to", x)

print("before calling fun(), X is:", x)
fun()
print("value of x outside of fun is:", x)