# 1. Sa se creeze o clasa Student cu atributele: nume, universitate, an (toate la constructor)
# 2. Sa se scrie functiile specifice astfel incat la printarea unui student sau colectii de studenti
# sa se afiseze toate atributele acestora
# 3. Fie lista de studenti:
# students = [
#         Student(name="Alex", university="Babes", year=3),
#         Student(name="Cristina", university="Yale", year=4),
#         Student(name="Meredith", university="Chicago", year=3),
#         Student(name="George", university="Harvard", year=1),
#         Student(name="Mark", university="NYU", year=4),
#       Student(name="Owen", university="NYU", year=4),
#       Student(name="Derek", university="Columbia", year=4)
#     ]
# a) creati clasa StudentDB si adaugati aceasta lista ca si clasa Attribute
# b) sa se creeze o functie care primeste ca parametru un student si returneaza daca acel student este inregistrat la vreo universitate.

# 4. Sa se scrie o functie care returneaza toate universitatile la care sunt inregistrati

class Student:

    # ex1
    def __init__(self, name, university, year):
        self.name = name
        self.university = university
        self.year = year

    # ex 2.a
    def __str__(self):
        return f'name:{self.name}, university: {self.university}, year: {self.year}'

    # ex 2.b
    def __repr__(self):
        return str(self)

    # 3.a

    # 3. b
    def __eq__(self, other):
        if not  isinstance(other, Student):
            return False
        return self.name == other.name and self.year == other.year and self.university == other.university
class StudentDB:
    students = [
        Student(name="Alex", university="Babes", year=3),
        Student(name="Cristina", university="Yale", year=4),
        Student(name="Meredith", university="Chicago", year=3),
        Student(name="George", university="Harvard", year=1),
        Student(name="Mark", university="NYU", year=4),
        Student(name="Owen", university="NYU", year=4),
        Student(name="Derek", university="Columbia", year=4)
    ]

    # 3. b
    def find_student(self, student):
        for std in self.students:
            if std == student:
                return True
        return False

    # ex 4
    def get_all_universities(self):
        universities = set()
        for student in self.students:
            universities.add(student.university)
        return list(universities)

std1 = Student('Viviana', 'UVT', 1)
std2 = Student('Gigel', 'UPT', 3)

print(std1)
print(std2)
print([std1, std2])

std3 = Student(name="Derek", university="Columbia", year=4)
stDB = StudentDB()

print(stDB.find_student(std3))

print(stDB.get_all_universities())