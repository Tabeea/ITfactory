# Ex 1 Variabila este zona din memoria unui calculator care tine date
import math
import numbers

# Ex 2 & 3 Variabile: string, int, float, bool + functia type

# string
culoare = 'rosu'
print(type(culoare))

# int
an_nastere = 2000
print(type(an_nastere))

# float
pret = 199.99
print(type(pret))

# bool
copil = True
print(type(copil))

# Ex 4
pret = 199.99
print(round(pret))
pret = 200
print(type(pret))

# Ex 5
print(f'Culoarea mea preferata este {culoare}')
print(f'Ana este nascuta in anul {an_nastere}')
print(f'Este oferta! Costa {pret} lei')
print(f'Un {copil} te poate face sa zambesti!')

# Ex 6
x = input('Nume: ')
y = input('Prenume: ')
print(f'Numele complet are {len(x)+len(y)} caractere')

# Ex 7
x = input('Lungime: ')
y = input('Latime: ')
print(f'Aria dreptunghiului este {float(x)*float(y)}')

# Ex 8 Afișează de câte ori apare cuvântul 'the';
prep = 'Coral is either the stupidest animal or the smartest rock'
print(prep.count(' the '))

# Ex 9 Același string:
#  inlocuieste the cu THE peste tot;
#  Printează rezultatul.

print(prep.replace('the','THE'))

# 10. Același string. Folosește un assert ca să verifici dacă acest string conține doar numere.

assert prep.isdigit()
print('Prep contine numere')

# Exerciții optionale:

# 1
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.

var1 = input('String cu dimensiune impara:')
var2 = int((len(var1)/2))
print(var1[var2])


# 2. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# # - printează ambele variabile pentru verificare.

input('String: ').split()
