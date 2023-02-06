# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# 1.Având lista:
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

# for
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# for each
print(30*"#")
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
print(30*"#")
index = 0
while len(masini) > index:
    print(f'Masina mea preferata este {masini[index]}')
    index += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
#Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

print(30*"#")
for i in range(len(masini)):
    masini[i] = masini[i].upper()
    i += 1
    masini[0] = 'Audi'
    masini[-1] = 'Opel'
else:
    print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

print(30*"#")
i=0
for i in range(len(masini)):
    if masini[i] == 'MERCEDES':
#while masini[i] == 'MERCEDES'
        i +=1
        print('Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masini[i]}. Mai cautam')

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

print(30*"#")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    a = masini[i]
    if a == 'Trabant':
            continue
    elif a == 'Lastun':
        continue
    print(f'S-ar putea sa va placa {masini[i]}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Iterează prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

print(30*"#")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        masini_vechi.append(masina)
        masini = [item.replace('Trabant', 'Tesla') for item in masini]
        masini = [item.replace('Lastun', 'Tesla') for item in masini]
print(f'Masini vechi: {masini_vechi}')
print(f'Masini noi: {masini}')


# 6. Având dict:
print(30*"#")
pret_masini = {'Dacia': 6800, 'Lăstun': 500,'Opel': 1100, 'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Iterează prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

buget = 15000
for key, value in pret_masini.items():
  if value <= buget:
    print(key)

for key, value in pret_masini.items():
  if value <= buget:
    print(f'{key} {value}')

for key, value in pret_masini.items():
    if value <= buget:
         print(f'Pentru un {buget} de sub 15 000 euro puteți alege mașina {key}')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

print(30*"#")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
a = 0
for i in range (len(numere)):
   if numere[i] == 3:
       a +=1
print(a)


# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

print(30*"#")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere:
    suma += i
print(suma)

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max)

print(30*"#")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = 0
for i in numere:
    if i > max:
        max = i
print(max)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

print(30*"#")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.
# 1.
print(30*"#")
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
print(numere_pare)

for i in alte_numere:
    if i % 2 != 0:
        numere_impare.append(i)
print(numere_impare)

for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
print(numere_pozitive)

for i in alte_numere:
    if i < 0:
        numere_negative.append(i)
print(numere_negative)