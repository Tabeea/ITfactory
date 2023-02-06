# exceptions are events that might happen during the execution of the code
# that Python does not know to treat
# (exceptiile sunt evenimente care s-ar putea intampla in timpul
# executiei unei bucati de cod pe care Python nu le stie trata)

try: # tests a block of code for errors
    print(x)
except: # treats different types of errors
    print('A aparut o eroare.')

##########################################################
try:
    a = 1/0
    l = [1,2,3]
    l.add(5)
    print(x)
except NameError:
    print('A aparut NameError.')
except AttributeError as ex:
    print(f'Eroare: {ex}')
except:
    print('Alt tip de eroare')

##########################################################
try:
    print('Hello')
except:
    print('A aparut o eroare.')
else: # executes if there was not error
    print('Nicio eroare.')
##########################################################
try:
    print('x')
except:
    print('A aparut o eroare')
finally: #always executes at the end.
    print('Finished')
##########################################################
x = int(input('Introdu un numar: \n'))
if x < 0:
    raise Exception(f'{x} is below 0.')

"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: <-- Prinderea tuturor exceptiilor de tipul NumeEroare
    se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multe tipuri de Exceptii
    se executa daca se prinde AltNumeEroare sau IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei 'ex')
    se poate accesa mesajul de Eroarea4 prin variabila ex
except:
    se executa la orice alt tip de eroare nespecificat
else:
    se executa doar daca nu se arunca eroare in blocul try
finally:
    se executa indiferent daca se arunca eroare sau nu
"""
