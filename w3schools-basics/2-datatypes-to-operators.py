#------------------------ DATA TYPES -----------------------

# What data type is x?
## (I have written the answers as comments at the end of each line)

x = 5; print(type(x)) # int (integer)

x = "Hello World!" # str (string)

x = 20.5 # float (floating point number)

x = ["a","b","c"] # list

x = ("a","b","c") # tuple
    ## (note: lists are mutable, tuples are immutable)

x = {"name":"John","age":36} # dict (dictionary)

x = True #bool (boolean)

#------------------------ NUMBERS -------------------------

# 1: insert correct syntax to convert x to floating point number
x=5
x= float(x)

# 2: convert x to integer
x=5.5
x= int(x)

# 3: convert x to complex number
x=5;
x=complex(x)

## Complex numbers can have a real and imaginary part:
a = 5
b = 3
c = complex(a, b)
print(z.real) # 5.0
print(z.imag) #3.0

#------------------------ STRINGS -------------------------

# 1: use 'len' to print length of string
x= "Hello World"
print(len(x))

# 2: get first character of string 'txt'
txt = "Hello World"
x = txt[0]

# 3: get characters from index 2-4 (llo)
x = txt[2:5]

# 4: return string with no whitespaces at start/end
txt = " Hello World "
x = txt.strip()

# 5: convert value of txt to UPPERCASE and lowercase
x = txt.upper()
y = txt.lower()

# 6: replace H with J (resulting in Jello World)
txt = txt.replace("H", "J")

# 7: add placeholder for age parameter
age = 36
txt = "My name is John and I am {}"
print(txt.format(age))

## str.format() method inserts variables into string placeholders.
## alternatively:
txt = f"My name is John and I am {age}"; print(txt)

#------------------------ BOOLEANS -------------------------

# what would be printed after these statements?

print(10>9) # True

print(10==9) # False

print(10<9) # False

bool("abc") # True
bool("") # False
    ## non-empty strings are truthy

bool(0) # False
bool(1) # True
    ## 0 is falsy, all other ints (-ve and +ve) are true

#------------------------ OPERATORS -------------------------

# 1: multiply 10 by 5 and print output
print(10 * 5)

# 2: divide 10 by 2
print(10/2)

# 3: use membership operator to check if "apple" exists in 'fruits' object
fruits = ["apple","banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit")

# 4: use comparison operator to check if 5 is NOT equal to 10
if 5 != 10:
    print("numbers are not equal")

# 5: use logical operator to check if at least one statement is True
if 5 == 10 or 4 == 4:
    print("At least one statement is true")
