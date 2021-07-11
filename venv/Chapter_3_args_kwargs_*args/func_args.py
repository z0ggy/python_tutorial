def user_info(name, age=0, city="No City"):
    """This function prints name, age, and city from an argument provided to the function."""
    print("{} is {} years old, from {}".format(name, age, city))


user_info("Dominik", 40, "Gotham city")
user_info("Pat")
user_info(age=54, name="Pat")


# *args allows for unlimited variables to be passed into a function without defining them ahead of time

def add(*args):
    added_numbers = sum(args)
    print("This is the sum of a {}".format(sum(args)))


add(2, 4, 6, 8)


# **kwargs allows for unlimited keyword arguments to be passed into a function without defining them ahead of time

def application(**kwargs):
    print(kwargs)


application(numer="Jon", email="mail@mail.com")


def app(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. His email is {}.".format(fname, lname, company, email))


app("Bruce", "Wayne", "mail@mail.com", "Wayne Industry", 75000, hire_date="September 2000")
