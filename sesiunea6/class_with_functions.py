class Dog:
    species = 'mamal'

    def __init__(self, age, name):   # instance attribute
        self.age = age
        self.name = name

    def bark(self): # self -> reference to the current object
        print('Ham, ham')

    def get_owner(self):
        return f'Eu sunt {self.name} si ma detine Andrei'

dog = Dog(3, 'Rex')
dog.bark()
print(dog.get_owner())

dog2 = Dog(3, 'Mimi')
print(dog2.get_owner())
print(type(dog))
print(type(int))
