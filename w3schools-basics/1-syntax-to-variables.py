#------------------------ SYNTAX -------------------------

# 1: how to print
print("Hello World")

# 2: print yes if 5>2
if 5>2:
    print("YES")


#------------------------ COMMENTS -------------------------

# 1: how to comment
# this is a comment

# 2: how to multi-line comment
"""
This is a comment
written in
more than 1 line
"""


#------------------------ VARIABLES -------------------------

# 1: create variable 'carname' and assign value 'Volvo' to it
carname = "Volvo"

# 2: create variable 'x' and assign value '50' to it
x = 50

# 3: Display sum of 5+10 using x and y variables
x=5
y=10
print(x + y)

# 4: create variable z, assign x+y to it, print result
x=5; y=10; z = x + y
print(z)

# 5: assign values to multiple variables in one line
x,y,z = "Orange","Banana","Cherry"

# 6: assign same value to all three variables in one code line
x=y=z="Orange"

# assign global variable 'x'
def myfunc():
    global x
    x = "fantastic"
