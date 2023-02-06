def produsul(a,b):
    return  a*b

p = produsul(5, 6)
print(p)

def patratul_primelor_nr(n):
    result = []
    for i in range(n):
        patrat = produsul(i,i)
        result.append(patrat)
    return result

print(patratul_primelor_nr(10))

def get_all_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return  even_numbers
print(get_all_even_numbers([1,3,4,52,6,2,-23]))
