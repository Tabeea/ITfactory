# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    raza = 5
    culoare = 'rosu'

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        return f'culoarea:{self.culoare}, raza:{self.raza}'

    def aria(self):
        return f'Aria este: {self.raza*self.raza} PI'

    def diametru(self):
        return f'Diametru este: {2*self.raza}'

    def circumferinta(self):
        return  f'Circumferinta este: {2*self.raza} PI'


cerc1 = Cerc(5,'rosu')
print(cerc1.descrie_cerc())
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

# Ex2 : Clasa Dreptunghi
# Atribute: lungime, lățime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Poți verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    lungime = 10
    latime = 5
    culoare = 'alb'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}'

    def aria(self):
        return f'Aria dreptunghiului este {self.lungime*self.latime}'

    def perimetrul(self):
        return f'Perimetrul este {2*(self.latime+self.lungime)}'

    def schimba_culoarea(self):
        return self.descrie()

dreptunghi = Dreptunghi(10,5,'alb')
print(dreptunghi.descrie())
print(dreptunghi.aria())
print(dreptunghi.perimetrul())

dreptunghi1 = Dreptunghi(10,5,'rosu')
print(dreptunghi1.schimba_culoarea())

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = 'Miu'
    prenume = 'Ion'
    salariu = 5000

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f'Avem urmatoarele informatii -> Nume: {self.nume}, Prenume: {self.prenume}, Salariu: {self.salariu}'

    def nume_complet(self):
        return f'Numele complet al angajatului este: {self.nume} {self.prenume}'

    def salariu_lunar(self):
        return f'Salariul lunar al angajatului este: {self.salariu}'

    def salariu_anual(self):
        return f'Salariul anual al angajatului este: {12*self.salariu}'

    def marire_salariu(self, procent):
        #crestere =self.salariu * (procent*0.01)
        noul_salariu = self.salariu + int(self.salariu * (procent*0.01))
        return f'Salariul a crescut cu {int(self.salariu/int(noul_salariu)*100)}%'
a1 = Angajat('Miu', 'Ion', 5000)
print(a1.descrie())
print(a1.nume_complet())
print(a1.salariu_lunar())
print(a1.salariu_anual())

# 3 not done - afisarea procentului
a2 =  Angajat('Miu', 'Ion', 6000)
print(f'{a2.marire_salariu(20)}')


# 4. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = 	'RO49 AAAA 1B31 0075 9384 0000'
    titular_cont = 'Dinica Ana Maria'
    sold = 1000
    plata = 200
    bonus = 300

    def __init__(self, iban, titular_cont, sold, plata, bonus):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
        self.plata = plata
        self.bonus = bonus

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei'

    def debitare_cont(self):
        return f'Titularul {self.titular_cont} a efectuat o plata in valoare de {self.plata}, iar soldul acestuia este in valoare de {self.sold-self.plata}'

    def creditare_cont(self):
        return f'Titularul {self.titular_cont} a primit un bonus in valoare de {self.bonus}, iar soldul acestuia este in valoare de {self.sold+self.bonus}'

c1= Cont('RO49 AAAA 1B31 0075 9384 0000', 'Dinica Ana Maria', 1000, 200, 300)
print(c1.afisare_sold())
print(c1.debitare_cont())
print(c1.creditare_cont())


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# 1. Clasa Factură
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fără serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000

class Factura:
    seria = 'A'
    numar = 100
    nume_produs = 'Ciocolata'
    cantitate = 200
    pret_buc = 5

    def __init__(self, seria, numar, nume_produs, cantitate, pret_buc):
        self.seria = seria
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self):
        print(f'Noua cantitate este: {self.cantitate}')
        print(f'Factura: {self.seria}| {self.numar} | {self.nume_produs} | {self.cantitate} | {self.pret_buc}')

    def schimba_pret(self):
        print(f'Noul pret este: {self.pret_buc} lei')
        print(f'Factura: {self.seria}| {self.numar} | {self.nume_produs} | {self.cantitate} | {self.pret_buc}')

    def schimba_nume_produs(self):
        print(f'Noul nume al produsului este: {self.nume_produs}')
        print(f'Factura: {self.seria}| {self.numar} | {self.nume_produs} | {self.cantitate} | {self.pret_buc}')

    def genereaza_factura(self):
        print(f'Factura seria {self.seria} număr {self.numar}')

        # Import date class from datetime module
        from datetime import date
        # Returns the current local date
        today = date.today()
        print(f'Data:', today)

        # from tabulate import tabulate
        # l1 = PrettyTable[['Produs', 'cantitate', 'pret bucata', 'Total'],
        #                  [self.nume_produs, self.cantitate, self.pret_buc, {self.cantitate * self.pret_buc}] ]
        # table1 = tabulate(l1)
        # table2 = tabulate(l1, headers ='firstrow')
        # print(l1)


        print(f' Produs | cantitate | preț bucată | Total')
        print(f'{self.nume_produs} | {self.cantitate}| {self.pret_buc} | {self.cantitate * self.pret_buc}')

fact1 = Factura('A', 100, 'Ciocolata', 300, 5)
print(fact1.schimba_cantitatea())
fact2 = Factura('A', 100, 'Ciocolata', 300, 6)
print(fact2.schimba_pret())
fact3 = Factura('A', 100, 'Biscuiti', 300, 6)
print(fact3.schimba_nume_produs())

print(fact3.genereaza_factura())

# 2. Clasa Mașină
# Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
# disponibile (set), înmatriculată (bool)
# Culoare = gri - toate mașinile când ies din fabrică sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
# Culori disponibile = alege tu 5-7 culori
# Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
# Înmatriculată = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e
# negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina:
    marca = 'Audi'    # only one
    model = 'R8'
    viteza_maxima = 300
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb', 'negru', 'rosu', 'gri', 'albastru'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        return f'{self.marca}, {self.model}, {self.viteza_maxima}, {self.viteza_actuala}, {self.culoare}, {self.inmatriculata}'

    def schimba_culoare(self, culoare):
            if culoare in self.culori_disponibile:
                return culoare
            return Exception

    def accelereaza(self, viteza):
        if viteza < 0:
            return Exception
        elif viteza > self.viteza_maxima:
            return self.viteza_maxima

    def franeaza(self):
        if self.viteza_actuala == 0:
            return f'Masina se va opri'

m1 = Masina('A3', 150)
print(m1.descrie())
m1.schimba_culoare('rosu')
print(m1.schimba_culoare('argintiu'))
print(m1.accelereaza(200))
print(m1.franeaza())

