class Dog:
    species = 'mamal'
    age = 12
    name = 'Spark'  # class attribute -> the same for all object of this class


d = Dog()
print(d.name)

d2 = Dog()
print(d2.name)

d3 = Dog()
d3.name = Dog()
print(d3.name)  # name -> becomes instance attribute

d2.name = 'Puffy'
print(d2.name, d.name)

Dog.name = 'Bruno'
print(d2.name, d.name, d3.name)


# class attributes are usually used for defining constants within a class

class Dog2:
    species = 'mamal'  # class attribute

    # constuctor
    def __init__(self, age, name):  # instance attribute
        self.age = age
        self.name = name


my_dog = Dog2(10, 'Rex')

print(my_dog.age)
print(my_dog.name)

# Dog2.name -> incorrect because name is an instance attribute and it can only be accessed via an instance (object) of this class
