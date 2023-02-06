class Dog:
    species = 'mammal'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f'age:{self.age}, name:{self.name}'

    def __repr__(self):  # folosit pentru printarea colectiilor de obiecte
        return self.__str__() # sau str(self)

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.age == other.age and self.name == other.name

d = Dog(5, 'Rex')
print(d)

d2 = Dog(4, 'Puffy')
print(d2)

l = [d2, d]
print(l)

d3 = Dog(4, 'Puffy')
print(d2 == d3)
print(d2 == 5)