# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o.
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note = note_muzicale[::-1]
print(note_muzicale)

note.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?

print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista1 = [3, 1, 0,2]
lista2 = [6, 5, 4]
print(lista1+lista2)
lista1.extend(lista2)
print(lista1)

# 4.
# ● Sortează și afișează lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție. ( ? )
# ● Afișaza iar lista.

lista1.sort(reverse = True)
print(lista1)
lista1.sort()
print(lista1)


# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.


if lista1 == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

lista1.clear()
print(lista1)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if lista1 == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor  NOT YET
# Ex: ‘Ana a luat nota {x}’

print(f'{dict1.keys()} a luat nota {dict1.values()}')
print(f'Ana a luat {dict1.get("Ana")}')
print(f'Gigel a luat {dict1.get("Gigel")}')
print(f'Dorel a luat {dict1.get("Dorel")}')

# Doar nota o vei lua folosindu-te de cheie
#
# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1['Dorel'] = 6
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Dorel')
dict1.update({'Ionica': 9})
print(dict1)


# Exerciții Opționale - grad de dificultate: Mediu spre greu (may need Google)
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:

# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3

# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișază a intrat x, a ieșit y, mai ai z schimbări

# Dacă jucătorul nu e în teren:
# - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori

# Google search hint
# “how to check if item is în list python”

echipa = [ 'Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5']
teren = ['Jucator1', 'Jucator2', 'Jucator3']
x = 'Jucator5'
y = 'Jucator1'
schimbari_efectuate = 5
schimbari_maxime = 3

if x in teren and schimbari_efectuate < 3:
    schimbari_efectuate += 1
    teren.remove(x)
    teren.append(y)
    print(f'A intrat {x} a iesit {y}, mai ai {schimbari_maxime - schimbari_efectuate} schimbari')
else:
    if x not in teren:
        print(f'Nu se poate efectua schimbarea deoarece  {x} nu e în teren')
        print(f'Mai ai {schimbari_maxime - schimbari_efectuate} schimbari')


# . EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ .
# 1. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișează zile_sapt

zile_sapt.add('luni')
print(zile_sapt)

# 2.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

if  weekend.issubset(zile_sapt) == True:
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii')

# 3. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt-weekend)

# 4. Afișează intersecția elementelor din aceste 2 seturi.
print(zile_sapt & weekend)
