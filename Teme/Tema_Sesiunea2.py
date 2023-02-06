# 1. if else - verifica daca (if) o coditie se respecta sau nu. In cazul in care
# nu se respecta conditia initiala, atunci (else) va executa codul pentru cealalta conditie

#2 Verifică și afișează dacă x este număr natural sau nu.

x = 10
if x > 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = 7
if x > 0:
    print('x este un numar pozitiv')
elif x < 0:
    print('x este un numar negativ')
else:
    print('x este un numar neutru')

# 4. Verifică și afișează dacă x este între -2 și 13.

x = 6
if x > -2 and x < 13:
    print('x este intre -2 si 13')
else:
    print('x nu este intre -2 si 13')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

x = 100
y = 50
if x - y < 5:
    print('Diferenta este mai mica decat 5')
else:
    print('Diferenta este mai mare decat 5')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x =  1
if not 5 < x < 27:
    print('x nu este intre 5 si 27')
else:
    print('x este in intre 5 si 27')

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.

x = 6
y = 6

if x == y:
    print('x si y sunt egale')
elif x > y:
    print('x este mai mare ca y')
else:
    print('y este mai mare ca y')

# 8. x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x = 6
y = 6
z = 6

if x == y == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or y == z:
    print('Triunghi isoscel')
else:
    print('Triunghi oarecare')

# 9. Citește o literă de la tastatură.  (nu este oki)!!!!
# Verifică și afișează dacă este vocală sau nu.

x = ['a', 'e', 'i', 'o', 'u']
litera =input('Introdu o litera: ')

if litera in x:
    print('Litera este o vocala.')
else:
    print('Litera este o consoana.')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E

nota = int(input('Introdu nota: '))
if nota > 9:
    print('A')
elif nota > 8:
    print('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print('D')
elif nota > 4:
    print('E')
else:
    print('F')



# Exerciții Opționale



# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = 12345
if len(str(x)) < 4:
    print('x nu are minim 4 cifre')
else:
    print('x are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre. ( nu este oki)

x = 123465
if  x >= 100000 and x <= 999999:
    print('x are exact 6 cifre')
else:
    print('x nu are exact 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).

x = 5
if int(x) % 2 == 0:
    print(f'{x} este par')
else:
    print(f'{x} este impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?

x = 1
y = 7
z = 3
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
elif z > x  and z > y:
    print(z)
else:
    print('2 dintre ele sunt egale')

# 5. x, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x_unghi = int(input('Primul unghi al triunghiului: '))
y_unghi = int(input('Al doilea unghi al triunghiului: '))
z_unghi = int(input('Al treilea unghi al triunghiului: '))

total_unghi = x_unghi + y_unghi + z_unghi

if total_unghi <= 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul este invalid')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citește de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu un numar:'))
print(prop[:-x])

# 7. Același string. Declară un string nou care să fie format din primele 5
# caractere + ultimele 5.

prop = 'Coral is either the stupidest animal or the smartest rock'
first_5characters = prop[:5]
last_5characters = prop[-5:]
print(first_5characters + last_5characters)


# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvânt
# ● output: 'Coral is either the stupidest animal or the smartest'

prop = 'Coral is either the stupidest animal or the smartest rock'
a = prop.index('rock')
print(prop[:a])





# Exerciții Bonus (may need google)


# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# ● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

import random
dice_roll = random.randint(1,6)
x = dice_roll
utilizator = input('Ghiceste ce numar va avea zarul: ')
if utilizator > x:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {utilizator} dar a fost {x}')
elif utilizator < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales  {utilizator} dar a fost {x}')
elif utilizator == dice_roll:
    print(f'Ai ghicit. Felicitări! Ai ales {utilizator} si zarul a fost {x}.')