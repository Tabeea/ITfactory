# 1. Functie ca argument
def say_hello(name):
    print(f'Hello {name}')

def say_hi(name):
    print(f'Hi {name}')

def greet_bob(greeter_func):
    greeter_func('bob')

greet_bob(say_hello)
greet_bob(say_hi)

# 2. Inner Function - Functie interioara
def parent():
    print('Printing from parent() function')
    def first_child():
        print('printing from first_child() function')
    def second_child():
        print('printing from second_child() function')

    second_child()
    first_child()
parent()

# 3. Returnare de functii

def parent(num):
    def first_child():
        print('printing from first_child() function')
    def second_child():
        print('printing from second_child() function')

    if num == 1:
        return first_child
    else:
        return second_child
f = parent(1)
print(type(f))
f()
