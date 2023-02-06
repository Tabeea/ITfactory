class CustomException(Exception):
    pass
# Sa se scrie o functie care verifica daca o lista de nr intregi contine nr negative.
# daca da, sa se arunce o exceptie specifica

def ContainsNegativeNumberException(Exception):
    pass

def check_negative_numbers(numbers):
    for number in numbers:
        if number  < 0:
            raise ContainsNegativeNumberException(f'Contine {number}')
check_negative_numbers([5, 0 , -8, -1, 7])
