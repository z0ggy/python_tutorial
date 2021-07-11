fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]


def print_fruits():
    print(fruits)


print(fruits, years)

# Append method for add item to the list
fruits.append("oranges")
print_fruits()

# List extend method allow to add multiple items into the list from another list
fruits.extend(years)
print_fruits()

# Remove method remove item from list
fruits.remove("oranges")
print_fruits()

# Pop method remove item by item index
fruits.pop(0)
print_fruits()

# pop with negative index for remove item from the end of the list
fruits.pop(-1)
print_fruits()

# sort method only sort item like list (same type or similar like integer-float)
# fruits.sort() will give us error because of different type of data
# create new number list
numbers = [5, 1928, 4, 17, 68, 73.43, 89.78]
numbers.sort()
print(numbers)

