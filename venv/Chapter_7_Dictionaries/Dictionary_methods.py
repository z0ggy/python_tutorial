stuff = {
    "food": 15,
    "energy": 100,
    "enemies": 3
}

# get method to get value of any key from dictionary
print(stuff.get("food"))

# items method take the name of the dictionary and output  the key value pairs
print(stuff.items())

# keys method return all keys from dictionary
print(stuff.keys())

# popitem allows us to remove the last item from a dictionary
print(stuff.popitem())
print(stuff)

# setdefault allows us to se value of the key in dictionary, allows as to set default value when the key is not in
# dictionary
print("setdefault")
print(stuff.setdefault("food"))
print(stuff.setdefault("friends", 123))
print(stuff)

# update methods update one dictionary with another or update existing item in dictionary
new_item = {"rocks": 4, "arrows": 18}
stuff.update(new_item)
print(stuff)

new_item = {"rocks": 2, "arrows": 5}
stuff.update(new_item)
print(stuff)

# add and update dictionary in the same time
up_new = {"food": 3, "webs": 2}
print(stuff)

stuff.update(food=450)
print(stuff)

# adding items directly into dictionary
stuff.update(cookies=6)
print(stuff)
