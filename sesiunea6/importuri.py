'''
Clasele se scriu cu litera mare si fara fara jos ('_'): NumeClasa
Numele fisierelor in care se afla o clasa au acelasi nume cu clasa doar ca se scrie cu litera mica si cu '_' (bara jos): nume_clasa
'''

from magic_methods import Dog
from classwithattributes import Dog as DogWithAttributes
from classes.dogs.dog import Dog as Dog2

d = Dog(1, 'Dinu')
print(d)

d2 = DogWithAttributes
print(d2)

d3 = Dog2(1, 'Rex')
print(d3)

