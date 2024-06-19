#------------------------ LISTS -------------------------

# 1: print second item in 'fruits' list
fruits = ["apple","banana","cherry"]
print(fruits[1])

# 2: change 'apple' to 'kiwi'
fruits[0] = "kiwi"

# 3: use 'append' method to add 'orange'
fruits.append("orange")

# 4: use 'insert' method to add 'lemon'
fruits.insert(1,"lemon")

# 5: use 'remove' method to remove 'banana'
fruits.remove("banana")

# 6: print last item in list with negative indexing
print(fruits[-1])

# 7: print third, fourth and fifth items
print(fruits[2:5])

# 8: print number of items in list
print(len(fruits))

#------------------------ TUPLES -------------------------

# 1: print first item in 'fruits' tuple
fruits = ("apple","banana","cherry")
print(fruits[0])

# 2: print number of items
print(len(fruits))

# 3: print last item
print(fruits[-1])

# 4: print third, fourth and fifth items
print(fruits[2:5])

#------------------------ SETS ---------------------------

# 1: check if apple is present in 'fruits' set
fruits = {"apple","banana","cherry"}
if "apple" in fruits:
    print("yes")

# 2: use 'add' method to add 'orange'
fruits.add("orange")

# 3: add multiple items 'more_fruits' to fruits set
fruits = {"apple","banana","cherry"}
more_fruits = ["orange","mango","grapes"]

fruits.update(more_fruits)

# 4: use 'remove' method to remove 'banana'
fruits.remove("banana")

# 5: use 'discard' method instead
fruits.discard("banana")

    ## `remove` vs `discard`: discard is only used for sets,
    ## and remove throws `keyerror` if element is not present whereas
    ## discard does nothing.

#---------------------- DICTIONARIES ---------------------

# 1: use 'get' method to print value of 'model' key in 'car' dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# 2: change "year" value from 1964 to 2020
car["year"] = 2020

# 3: add key/value pair "colour":"red"
car["colour"] = "red"

# 4: use 'pop' method to remove 'model'
car.pop("model")

# 5: use 'clear' method to empty the dict
car.clear()
