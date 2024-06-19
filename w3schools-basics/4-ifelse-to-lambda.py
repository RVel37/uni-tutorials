#------------------------ IF-ELSE -------------------------

# 1: print "hello world" if a is greater than b
a=50; b=10
if a > b:
    print("hello world")

# 2: print "hello world" if a is NOT equal to b
if a != b:
    print("hello world")

# 3: print "yes" if a equals b, otherwise print "no"
if a == b:
    print("yes")
else:
    print("no")

# 4: print '1' if a equals b, print '2' if a > b, otherwise print '3'
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

# 5: print "hello" if a equals b AND c equals d
if a == b and c == d:
    print("hello")

# 6: print "hello" if a equals b OR if c equals d
if a == b or c == d:
    print("hello")

# 7: print "yes" if 5 is greater than 2
if 5 > 2:
    print("yes")

# 8: use one-line shorthand syntax to print "yes" if a = b, otherwise print "no"
print ("yes") if a == b else print ("no")

# 9: print "yes" if either a or b equals c
if a == c or b == c:
    print ("yes")

#------------------------ WHILE -------------------------

# 1: print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1

# 2: stop loop if i is 3
while i < 6:
    if i == 3:
        break
    i += 1

# 3: in loop, when i = 3, jump directly to next iteration
while i < 6:
    if i == 3:
        continue
    i += 1

# 4: print message when condition is false
while i < 6:
    print(i)
    i +=1
else:
    print("i is greater than 6")

#------------------------ FOR ---------------------------

# 1: loop through items in list 'fruits'
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

# 2: when value is 'banana', jump directly to next item
for x in fruits:
    if x == "banana":
        continue
    print (x)

# 3: use 'range' function to loop through code set 6 times
for x in range(6):
    print(x)

# 4: exit loop when x = 'banana'
for x in fruits:
    if x == "banana":
        break
    print(x)

#------------------------ FUNCTIONS ---------------------

# 1: create function 'my_function'

def my_function():
    print("hello from a function")

# 2: execute this function
myfunction()

# 3: inside function w/ 2 parameters, print 1st parameter
def my_function(fname,lname):
    print(fname)

# 4: let function return the 'x' parameter + 5
def my_function(x):
    return x + 5

# 5: add prefix to function definition, so any no. of arguments (args) can be passed
def my_function(*kids):
    print("The youngest child is " + kids[2])

    ## Usage:
    my_function("John","Jane","Jim")
    # "The youngest child is Jim"

# 6: add prefix to function definition, so any no. of KEYWORD args (kwargs) can be passed
def my_function (**kid):
    print("His last name is " + kid["lname"])

    ## Usage:
    my_function(fname="Toby", lname="Turner")

#------------------------ LAMBDA -------------------------

# 1: create lambda function that takes parameter 'a' and returns it
x = lambda a : a
