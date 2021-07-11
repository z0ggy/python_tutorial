"""
BREAK
end the loop. go to the next statement in the program (outside the loop)
"""

# Break
temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    if temp_f == 32:
        break

# Continue
for i in range(1, 11):
    if i == 7:
        print("We are skipping number 7.")
        continue
    print("This is the number {}.".format(i))

for i in range(1, 11):
    if i == 3:
        pass
    else:
        print("This is the number {}.".format(i))
