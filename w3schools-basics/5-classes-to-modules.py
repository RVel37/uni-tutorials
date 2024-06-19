#------------------------- CLASSES ---------------------------

# 1: create class 'MyClass'
class MyClass:
    x = 5

# 2: create an object for 'MyClass' called 'p1'
p1 = MyClass()

# 3: Use p1 object to print value of x
print(p1.x)

# 3: create an init function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

#------------------------ INHERITANCE -------------------------

# 1: create class 'Student' that inherits properties + methods from 'Person' class
class Student(Person):
    pass

# 2: execute 'printname' method of object x
class Person:
  def __init__(self, fname):
    self.firstname = fname
  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#------------------------ MODULES ----------------------------

# 1: import a module 'mymodule'
import mymodule

# 2: create alias for a module
import mymodule as mx

# 3: print all variables + function names in a module
print(dir(mymodule))

#4: import only the 'person1' dictionary within 'mymodule' module
from mymodule import person1
