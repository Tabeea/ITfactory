# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu
# 1.Funcție care să calculeze și să returneze suma a două numere

def sumoftwonumbers(a,b):
    return a+b
s=sumoftwonumbers(-1,3)
print(s)

# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def oddorevennumber(nr):
    return True if nr % 2 == 0 else False
print(oddorevennumber(31))

# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

def get_total_characters():
    # totalchar = list(nume)
    nume =input('Nume:')
    total = 0
    for i in nume:
        if i == ' ':
            pass
        else:
            total = total + 1
    return total
print(get_total_characters())

# 4. Funcție care returnează aria dreptunghiului

def get_areaoftherectangle(L,l):
    return L*l
print(get_areaoftherectangle(L=8,l=4))

# 5. Funcție care returnează aria cercului

def get_areaofthecircle(R,PI):
    return R*R*PI
print(get_areaofthecircle(R=4,PI=3.14))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

def xinstring(x):
    text = input('Scrie un string: ')
    return True if x in text else False
print(xinstring('x'))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Numărul de caractere lower case este x
# ● Numărul de caractere upper case exte y

def string_check(string):
    a={"upper":0, "lower":0}
    for i in string:
        if i.isupper():
           a["upper"]+=1
        elif i.islower():
           a["lower"]+=1
        else:
           pass
    print ("String: ", string)
    print ("Numărul de caractere upper case este : ", a["upper"])
    print ("Numărul de caractere lower case este : ", a["lower"])
string_check('Ana are mere')

# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu
# numerele pozitive.

def positivenr(lst1):
    lst2=[]
    for i in lst1:
        if i > 0:
            lst2.append(i)
    return lst2
print(positivenr([1,4,-3,9]))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# ● Primul număr x este mai mare decat al doilea număr y
# ● Al doilea număr y este mai mare decat primul număr x
# ● Numerele sunt egale.

def numbers(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif x < y:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print('Numerele sunt egale')
print(numbers(2,2))

    # 10. Funcție care primește un număr și un set de numere.
# ● Printează ‘am adaugat numărul nou în set’ + returnează True
# ● Printează ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def numberandset(nr, set1):
    if nr not in set1:
        print('Nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set1.add(nr)
        print('Am adaugat numărul nou în set')
        return True
print(numberandset(1,{1,2,3}))


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# 1. Funcție care primește o lună din an și returnează câte zile are acea lună.

def get_monthoftheyear(luna):
    set1 = {1,3,5,7,8,10,12}
    for i in range(12):
        if luna in set1:
            return 31
        elif luna == 2:
            return 28
        elif luna > 12:
            return None
        else:
            return 30
print(get_monthoftheyear(4))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a, b, c, d
#print("Suma: ", a)

a, b, c, d = calculator(10,2)
print(calculator(10,2))
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


# 3. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def countnumberindict(lst):
    b = 0
    for i in range(10):
        if i in lst:
            b = lst.count(i)
        else:
            b = 0
        print(f'{i}:{b}')
print(countnumberindict([1, 3, 1, 5, 9, 7, 7, 5, 5]))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.

def maxofthenumbers(a,b,c):
    return max(a,b,c)
print(maxofthenumbers(7,9,8))

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

def sumofthenumber(nr):
    s = 0
    for i in range(nr+1):
        s = s + i
    return s
print(sumofthenumber(2))

# Exerciții Opționale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def get_intersection(lst1, lst2):
    return set(lst1).intersection(lst2)
print(get_intersection([7, 7, 2, 3], [6, 1, 2, 3]))

# 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.

def reducere_de_pret(p,r):
    if p > 0 and r < 100:
        np= p - (p * r)/100
        print(f'Pretul este {np} lei')
    elif p < 0 or r < 0:
        print(f'Reducerea de {r}% este invalida')
    else:
        print(p)
print(reducere_de_pret(1000,20))
