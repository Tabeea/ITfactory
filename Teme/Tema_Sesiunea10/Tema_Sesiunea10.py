# Ex. 1 Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import csv
from time import perf_counter
def timer(func):
    def wrapper():
        start = perf_counter()
        func()
        stop = perf_counter()
        t = stop - start
        print(f'Timpul necesar executiei unei functii este de {t:06f}')

    return wrapper

@timer
def say_timer():
    print('Time')
say_timer()

# Ex. 2
# a) Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator.
# b) Comparati diferenta de timp necesara generarii.

# Lists:
def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
primes_list = prime_numbers(100)
print(primes_list)

# Time for function prime_numbers function
import time
start_primes = time.perf_counter()
prime_numbers(100)
end_primes = time.perf_counter()
ms = end_primes-start_primes
print(f'Elapsed {ms:06f}')

# Generator:
def primes(n):
    prime = [True] * n
    for i in range(2,n):
        if prime[i]:
            yield i
            for c in range(i*i, n, i):
                prime[c] = False
for j in primes(100):
    print(j)

# Time for function primes function
import time
start_primes = time.perf_counter()
primes(100)
end_primes = time.perf_counter()
ms = end_primes-start_primes
print(f'Elapsed {ms:06f}')


# Ex. 3 Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata,
# el va scrie in acel fisier numele functiei, lista de argumente ca si string si rezultatul apelului.
# Fisierul este de tip csv. Functiile decorate pot primi oricate argumente


import functools

def write_function_details_in_csv(file_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            name_function = func.__name__
            arg_function = str(func.__code__.co_varnames)
            res_function = func(*args, **kwargs)
            data = [[name_function,res_function,arg_function]]
            with open(file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)

        return wrapper

    return decorator

@write_function_details_in_csv('ex3.csv')
def say_hello(name):
    return f'Hello {name}'

say_hello('Bob')

@write_function_details_in_csv('ex3.csv')
def say_hi(name_1, name_2):
    return f'Hello {name_1,name_2}'

say_hi('Ana', 'Maria')
