#-------------------Add and multiply using FUNCTIONS-------------------
'''
Youtube
def add(n1,n2):
    return n1+n2

a=int(input())
b=int(input())
c=int(input())
added=add(a,b)
output=added*c
print(output)


class goa():
    name=""
    drink=""
    def party(self):
        print("Lets Party...")
    def beach(self):
        print("enjoying")

ramesh = goa()
suresh = goa()
ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="Yes"
suresh.drink="No"

print(ramesh.name)
print(suresh.name)
print("drink:",ramesh.drink)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()

------------ Ques 2-------------------
class laptop():
    price=0
    processor=""
    ram=""
HP=laptop()
DELL=laptop()
LENOVO=laptop()

HP.price=50000
HP.processor="i5"
HP.

#--------------------class- DAY - 4-------------------------
def myfun():
  #docstring
    print("hi welcome to python functions")
myfun()


#----------------find power----------------------------
def power(x,n):
    return x**n
result=power(2,10)
#print(result)

def power(x,n):
    return x**n,n**x
r1,r2=power(2,10)
print(r1,r2)

def power(x,n):
    return x**n,n**x
r=power(2,10)
print(r,type(r))
#using loop to print
for i in r:
    print(i)


def sum(a,b):
    return a+b
print((sum(100,200)))

def sum(a,b=300):
    return a+b
print((sum(100,200)))

def sum(a=200,b=300):     #local values
    return a+b
print((sum(100,200)))
print(sum(100))
print(sum())

#-------FUNCTION OVERLOADING------(Python Doesnt support)----
#---------it gives error for this program-----------
def sum(a,b,c):
    return a+b
def sum(a,b,c):
    return a+b+c
print(sum(100,200))
print(sum(100,200,300))

#func overloading
def sum(a,b,c):
        return a+c

print(sum(100,200,300))
#print(sum(100,200))
print(sum(100,None,200))

#---------------TO pass many arguments
def sum(*args):
    sum=0
    print(type(args))
    for i in args:
        sum=sum+i
    return sum
    print(args)
print(sum(1,2,3,4))

def sum(** kwargs):
    print(type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

sum(name="Amit",Roll=111,marks=70)

#lambda functions----anonymous function
x=lambda  n:n+10
print(x(10))
-----------------------------------------------
def mul_no(n):
    return  n*10
print(mul_no(10))
x=lambda n:n*10
print(x(10))

#-------------filter using lambda,list--------------
l=[1,2,3,4,5]
n=list(filter(lambda x:x%2==0,l))
print(n)

l=range(1,10)
n=list(filter(lambda x:x%2==0,l))
print(n)

#-------------lambda using def---------------
def even(x):
    if x%2==0:
        return x
l=range(1,10)
n=list(filter(even,l))   #old method
n1=list(filter(lambda x:x%2==0,l))    #new method both same output
print(n)
print(n1)


#--------------------------map using lambda--------------------
l=range(1,10)
n1=list(map(lambda x:x**2,l))
print(n1)

from functools import reduce
l=range(1,7)
n1=list(map(lambda x:x**2,l))
n2=reduce(lambda x,y:x+y,l)
print(list(l))
print(n2)

#-------------Call one module from another module-----------
import Mymodule
print(Mymodule.greetings())
print(Mymodule.add(10,20))
print(Mymodule.sumoflist([1,2,3,4]))
print(Mymodule.var)
print(Mymodule.reverse_string("Python"))
print(Mymodule.even(8))
print(Mymodule.square(4))

class Student:
    def getdata(self):  #member function or method
        self.Name=input("Enter your name: ") #data member
        self.Age=input("Enter your age: ")
        self.Marks=input("Enter your marks: ")
        self.Roll=input("Enter your rollno: ")
    def showdata(self):
        print("name:",self.Name)
        print("age:", self.Age)
        print("marks:", self.Marks)
        print("roll:", self.Roll)
Obj1=Student() #instantiation or object creation
Obj2=Student()
Obj1.getdata()  #calling the function
Obj1.showdata()
Obj2.getdata()
Obj2.showdata()  #current function so this object passes to self
print(Obj1.Name,Obj1.Age,Obj1.Marks,Obj1.Roll)

class Student:
    def getdata(self):  #member function or method
        self.Name=input("Enter your name: ") #data member
        self.Age=input("Enter your age: ")
        self.Marks=input("Enter your marks: ")
        self.Roll=input("Enter your rollno: ")
    def showdata(self):
        print("name:",self.Name)
        print("age:", self.Age)
        print("marks:", self.Marks)
        print("roll:", self.Roll)
Obj1=Student() #instantiation or object creation
Obj2=Student()
Student.getdata(Obj2)
Student.showdata(Obj2)

#-----------------------CONSTRUCTOR----------------------------
class Student:
    def __init__(self,name,age): #self->obj1
        self.Name=name
        self.Age=age

    def getdata(self):
        print("Name:",self.Name)
        print("Age:",self.Age)

    def setdata(self):
        self.Name=input("enter name:")
        self.Age = input("enter age:")

Obj1=Student("Rajni",19) #create the object
Obj2=Student("Kant",19)

Obj1.getdata()
Obj1.setdata()


class Student:
    University='VTU'
    def __init__(self,name,age): #self->obj1
        self.Name=name
        self.Age=age

    def showdata(self):
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("University: ",Student.University)


Obj1 = Student("Rajni", 19)  # create the object
Obj2 = Student("Kant", 19)
Obj1.showdata()
Obj2.showdata()

class Student:
    def __init__(self,name,age): #self->obj1
        self.Name=name  #public
        self._Age=age    #protected
        self.__marks=0     #private

    def showdata(self):
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("marks",self.marks)
Obj1 = Student("Rajni", 19)
Obj1.showdata()
print(Obj1.Name)
print(Obj1.Age)
'''
#---------------------------INHERITANCE---------------------
class Vehicle():  #base/ parent/ super
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):   #subclass child derived
    def __init__(self,make,model,year):
        Vehicle.__init__(self,make,model,year) #or super().__init__(self,make,model,year)
        self.color="Black"
        self.type="Sedan"
        self.price=10
    def showdata(self):
        print("make:",self.make)
        print("model:", self.model)
        print("year:", self.year)
        print("color:", self.color)
        print("price:", self.price)
        print("type:", self.type)
Punch=Car("tata","Punch",2022)
Punch.showdata()












