temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    if temp_f == 32:
        break
