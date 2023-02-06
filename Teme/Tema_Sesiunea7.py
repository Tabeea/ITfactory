# 2. Rezolvă exercițiul
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import abstractmethod, ABC
class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        aria1= self.__latura*self.__latura
        return f"Aria: {aria1}"

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        self.__latura = None

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        aria1 = self.PI*(self.__raza*self.__raza)
        return f'Aria cercului este {aria1}'

    def descriere(self):
        print('Eu nu am colturi')

cerc1= Cerc(10)
print(cerc1.raza)
cerc1.raza = 5
print(cerc1.raza)
del cerc1.raza
print(cerc1.raza)
cerc1.raza = 7
print(cerc1.raza)
print(cerc1.aria())
print(20*"-")

patrat1= Patrat(7)
print(patrat1.latura)
patrat1.latura = 5
print(patrat1.latura)
del patrat1.latura
print(patrat1.latura)
patrat1.latura = 7
print(patrat1.latura)
print(patrat1.aria())


# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Pătrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui


# 1. Ce inseamna if __name__ == "__main__" scris intr - un fisier python?
# A module can define functions, classes, and variables.

# Variabila __name__ are valori diferite in functie de locatia din care rulam codul
# Daca este din modul (python file unde scriu codul), __name__ = __main__
# Daca importam modul-ul (imi creez un nou 'python file') atunci __name__ va fi numele modulului importat
# __name__ = 'nume_modul'

# 2. Cum instalam un pachet extern python?
# Se va folosi command prompt pentru a instala packages
# Search in start command prompt -> open --> Scriem pip pentru a instala diferite pachiete
# C:\Users\tabee>pip install numpy

# 3. Ce este dataclass in python?
# Dataclasses reprezinta clasele python, si sunt utile pentru stocarea obiectelor de date.
# from dataclasses import dataclass
# @dataclass

# 4. Ce este functia hash?
# hash (object) - returneaza valoarea hash a obiectului (daca exista)
# Valorile hash sunt integers. Sunt folosite pt a compara rapid cheile unui dictionar
# Hash este doar pentru obiectele mutabile (bool, int, float, list, tuple, str)
a = hash(42)
print(a)
b = hash(42.11)
print(b)
c = hash('abcd')
print(c)

# 5. Cum pot face codul de mai jos sa functioneze corect?

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __hash__(self):
        return hash(self.age) + hash(self.name)

    def __str__(self):
        return f'My age is {self.age} and my name is {self.name}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age and self.name == other.name

s = set()
p = Person(29, "Adrian")
s.add(p)
p1 = Person(30, "Ana")
s.add(p1)
print(s)
