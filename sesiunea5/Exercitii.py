# 1. Sa se scrie o functie care primeste oricati parametrii si de orice fel si returneaza
# lista valorilor argumentelor.

def list_all_parameters_values(*args,**kwargs):
    return list(args) + list(kwargs.values())

print(list_all_parameters_values(2,8,-18, a = 55))

# 2. Sa se scrie o functie care primeste ca parametru o lista
# si returneaza inversul acelei liste

def get_list_reverse(lst):
    return lst[::-1]

print(get_list_reverse([1,8,13,55,-14,0]))

# 3. Sa se scrie o functie care primeste ca parametru 2 numere
# si il returneaza pe cel mai mare.

def max_between(a,b):
    return a if a>b else b
print(max_between(5, 0))
print(max_between(5, 6))

# 4 Sa se scrie o functie care primeste ca parametru o lista si un numar
# Functia va returna de cate ori apare acel nr in lista
# iar daca nu apare deloc va arunca o eroare

def get_count_in_list(lst, a):
    counter = lst.count(a)
    if not counter:
        raise Exception(f'{a} nu se afla in lista')
    return counter

print(get_count_in_list([1,5,8,13,-14,2,15,1,16,1], 1))

#Ex 5 Sa se scrie o functie care citeste un string de la tastatura si returneaza to
# toate caracterele folosite in acel string

def get_unique_characters():
    exemplu = input('Scrie-mi ceva frumos: ')
    return list(set(exemplu))

print(get_unique_characters())

# 4 Sa se scrie o functie care citeste de la tastatura un text si returneaza
# toate caracterele folosite in text ordonat alfabetic

def get_sorted_unique_characters():
    chars = get_unique_characters()
    chars.sort()
    return chars

print(get_sorted_unique_characters())