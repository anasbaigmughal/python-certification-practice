def a():
    print("\nNEXT")


a()
f = open("myText.txt", "w")
f.write("This is the text file")
f.close  # must to close so written text is retained and saved

lines = ["Hello World \n", "Welcome to delayed start\n"]
print(type(lines))
f = open("myText.txt", "w")
f.writelines(lines)
f.close()

f1 = open("myText.txt", "r")
line = f1.readline()
while line != "":
    print(line)
    line = f1.readline()
f1.close()

f = open("myText.txt", "r")
while True:
    try:
        line = next(f)
        print(line)
    except StopIteration:
        break
f.close()

f = open("myText.txt", "a+")  # a+ read n write
f.write("appended text")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()

a()
f = open("myText.txt", "r+")
f.seek(3, 0)
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("binfile.bin", "wb")
num = list(range(11))
arr = bytearray(num)
f.write(arr)
f.close()

f = open("binfile.bin", "rb")
num = list(f.read())
print(num)
f.close()

import sys
randomList = ['a',0,2,3]
for entry in randomList:
    try:
        print("the entry is ", entry)
        r=1/(int)(entry)
        break
    except:
        print("Error of errors", sys.exc_info()[0],"occured")
        print("Next entry")
        print()
print("The reciprocal of ", entry, "is", r)

a()
randomList = ['a',0,2,3]
for entry in randomList:
    try:
        print("the entry is ", entry)
        r=1/(int)(entry)
        break
    except Exception as e:
        print("Error of errors", e.__class__,"occured")
        print("Next entry")
        print()
print("The reciprocal of ", entry, "is", r)

try:
    pass
except ValueError:
    pass
except(TypeError,ZeroDivisionError):
    pass
except:
    pass

#raise KeyboardInterrupt

try:
    a=int(input("Enter positive integer:"))
    if a<=0:
        raise ValueError("This is not positive number")
except ValueError as ve:
        print(ve)
 
 
print("================================")
try:
    num=int(input("enter a number:"))
    assert num%2==0 #for errors related to logic of your program, not true errors which crash app
except:
    print("Not an even number")
else:
    reciprocal = 1/num
    print(reciprocal)
 

 
try:
    f=open("myText.txt","r")
finally: #always executes
    f.close()

class MyError(Exception):
    pass
raise MyError("My Error Happened")
 
 
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)

com1 = Computer("i5","16gb")
com2 = Computer("17","32gb")
Computer.config(com1)
com2.config()
 
 
class Computer:
    def __init__(self):
        self.name ='anas'
        self.age='23'
    def update(self):
        self.age=30
c1=Computer()
c2=Computer()
print(id(c1))
print(id(c2))
c1.name = "Asad"
print(c1.name)
c2.update()
print(c2.age)
print(c1.age)

class Car:
    wheels = 4 #static vriable

    def __init__(self):
        self.mileage = 100
        self.company = "Honda"
c1 = Car()
c2=Car()
c1.mileage=10
c1.wheels=5
Car.wheels =8 #updating static variable
print(c1.mileage, c1.company, c1.wheels)
print(c2.mileage, c2.company, Car.wheels)
 
 
class Student:
    university = "BUIC"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    @classmethod #decorator
    def info(cls): #class method with class but not self
        return cls.university
    @staticmethod #decorator
    def info1(): #class method with class but not self
        print("this is static method")
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)
    def get_m1(self):
        return self.m1


s1 = Student(35,46,12)
s2 = Student(45,47,39)
print(s1.avg())
print(s2.avg())
# print(s1.info()) #without @classsmethodnot working as static variable
print(s1.info())
print(Student.info())
print(s1.get_m1()) #accessor method
 
 
#inner class
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lp = self.Laptop() #calls constructor of inner class
    def show(self):
        print(self.name, self.rollno)
        self.lp.show()
    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i7"
            self.ram = 32
        def show(self):
            print(self.brand,self.cpu, self.ram)

s1 = Student("Anas", 3)
s2 = Student("Asad", 4)
s1.show()
print(s1.lp.brand)
#print(s1.lp.show())
lap1 = s1.lp
lap1.show()
 
 
#inheritence
class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A): #single level inheritence
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(B): #multi level inheritence
    def feature5(self):
        print("Feature 5 working")
    def feature6(self):
        print("Feature 6 working")
a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()
b1.feature2()
c1 = C()
c1.feature1()
 
 
#inheritence
class A:
    def __init__(self):
        print("classA")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A): #single level inheritence
    def __init__(self):
        super().__init__()
        print("classB")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
b = B() #calls B class constructor if present, if not then calls A class constructor
 
 
class A:
    def __init__(self):
        print("classA")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(): #single level inheritence
    def __init__(self):
        print("classB")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(A,B): #single level inheritence
    def __init__(self):
        super().__init__() #will call preference one class constructor first
        print("classC")
    def feat3(self):
        super().feature2()
    def feature5(self):
        print("Feature 5 working")
    def feature6(self):
        print("Feature 6 working")
c = C()
c.feat3() 
#in multiple inheritence if same name methods in super classes then it will check for the order of preference method
 
 
#polymorphism

class Anaconda():
    def execute(self):
        print("Compiling...")
        print("Running...")
class MyEditor():
    def execute(self):
        print("Spelling checking...")
        print("Convention checkingn...")
        print("Compiling...")
        print("Running...")
class Laptop():
    def code(self, ide):
        ide.execute()
lap = Laptop()
spyder = Anaconda() 
editor = MyEditor()
#ducktyping : executes as per the object passed
lap.code(spyder)
lap.code(editor)
 
 
#operator overloading
class Student():
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = Student(m1, m2)
        return s3
    def __gt__():
        pass
    def __str__(self): #returns object information
        return "{} {}".format(self.m1,self.m2)
# print(a+b) = # print(a.__add__(b))
s1 = Student(60,30)
s2 = Student(58,30)
s3 = (s1+s2)
print(s3.m1, s3.m2)
print(s1) #def __str__(self)
print(repr(s1)) #as it is print
 
# python modules
# package has many modules in hierarchy but module is single

 
import functools
lst = [1, 3, 4, 6, 2]
print("The sum of the list elements is: ", end="")
print(functools.reduce(lambda a, b: a+b, lst)) #reduce keep on applying function and then returning the end result 

print("The maximum of the list elements is: ", end="")
print(functools.reduce(lambda a, b: a if a>b else b, lst)) #keep on applying functionality consequently on all elements one by one and then return result at the end

def printEven(testList):
    for i in testList:
        if i%2==0:
            yield i #retains memory of the variable, like static local variable

lst = [1,4,5,6,7]
print("the orignal numbers in the list are: "+str(lst))
print("the even numbers in the list are:", end="")
for j in printEven(lst):
    print(j,end=" ")
 

#docStrings
 
def myFun():
    return None
print("============")
print("Using __doc__:")
print(myFun.__doc__)
print("Using Help")
print("============")
help(myFun())
 

def myFun(arg1):
     
    Summary line
    Extended description of function

    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value
     
    return arg1
print(myFun.__doc__) #to display documentation on console
 
class A():
    pass
class B(A):
    pass
#b=B()
#print(B.__bases__)
 
class A():
    class_var = 1
    def __init__(self, var):
        self.var=var
a1=A(2)
a2=A(3)

print(A.__dict__)
print(a1.__dict__)
print(a2.__dict__)

#iterators
myTuple = ("apple","banana","cherry")
myit = iter(myTuple)
print(next(myit))
print(next(myit))
print(next(myit))

#iterator with self made class
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x

myclass = MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#using loop with iterator
i=0
while i<10:
    print(next(myiter))
    i+=1

#filter with iterator
lst =[1, 'a', 0, False, True, '0']
fil_lst = filter(None, lst)
print("the remaining elements are:")
for element in fil_lst:
    print(element)
#variable shadowing is related to scope of variable if same names are used locally and globally
