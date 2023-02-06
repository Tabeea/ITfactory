# 1. operatori de identitate

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'

print(x1 is y1)
print(x2 is not y2)
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3 == y3)
print(x3 is y3)
print(x3 is x3)
# Pentru tipuri de date complexe is -> verifica daca cei 2 operanzi sunt exact acelasi obiect

# 2. membership operators (operatori de apartenenta)
x = 'Ana are mere'
print('a' in x)
print('t' not in x)

