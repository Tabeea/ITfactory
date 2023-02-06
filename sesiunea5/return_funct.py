def say_hi():
    return 'Hello!' # terminates the execution of the function
    print('Hi')

text = say_hi()
print(text)

def print_first_50():
    for i in range(51):
        print(i)
    # return None / return -> is by default for every function

elem = print_first_50()
print(elem)