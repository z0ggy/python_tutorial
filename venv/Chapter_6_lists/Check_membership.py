fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print("apple" in fruits)
print("apples" in fruits)

# Check membership and the number of items with the count method
print(fruits.count("apples"))

fruits.append("apples")
print(fruits.count("apples"))

# Check membership as well as the index position using the index function
fruits.append("lemon")
print(fruits)
print(fruits.index("lemon"))


