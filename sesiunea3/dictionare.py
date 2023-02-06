# dictionary are used to stare data values in key: value pairs

# create
car = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}

# accesing elements
print(20 * '-', 'accesing elements', 20 * '-')
print(car['brand'])
print(car.get('model'))
print(car.get('is_new'))
print(car.get('is_new', True))

# adding elements
print(20 * '-', 'accesing elements', 20 * '-')
car['is_new'] = True #cea mai folosita

print(car)
print(car.setdefault('serie', 12345))
print(car)
print(car.setdefault('is_new', False))
print(car)

# replace elements
print(20 * '-', 'replace elements', 20 * '-')
car['is_new'] = False
print(car)

car.update({'is_new':True, 'price':10000})
print(car)

# remove elements
print(20 * '-', 'remove elements', 20 * '-')
car.pop('is_new')
print(car)

car.popitem() # remove last inserted
print(car)

del car['serie']
print(car)

# remove all elements
print(20 * '-', 'remove all elements', 20 * '-')

a = {1:3, 2:True}
a.clear()
print(a)

# all keys
print(20 * '-', 'all keys', 20 * '-')
print(car.keys())
print(list(car.keys()))

# all values
print(20 * '-', 'all values', 20 * '-')

print(car.values())
print(list(car.values()))

# all items
print(20 * '-', 'all items', 20 * '-')
print(car.items())
print(list(car.items()))



