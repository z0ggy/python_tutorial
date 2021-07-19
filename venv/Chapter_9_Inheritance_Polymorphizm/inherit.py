class Person:
    def __init__(self, firstname, lastname, health, status):
        """ initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class."""

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves"""
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()


# class Enemy inherit from person class to be able to use attribute and methods that we made in a Person class
# inheritance example
class Enemy(Person):
    # We know that firstname, lastname, health and status come from Person class Instead of reassigning them we use
    # super method to initialize those attributes as they are defined in parent(Person)
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

        # now that we have created our enemy constructor or init method for our enemy class we can create some new
        # methods for our enemy class since we are creating an enemy our first method will be the hurt method we'll
        # define our method the same way we have defined all other method in our classes before enemy class method
        # take 2 argument self and other

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)

# error condition
# Rey.steal(Alex)
