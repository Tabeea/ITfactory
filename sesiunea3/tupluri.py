# Tuple are used to store multiple items in a single variable
# Tuples are unchangeable

# create
fruits = ('apple', 'banana','cherry', 'cherry')

# count
print(20 * '-', 'count', 20 * '-')
print(fruits.count('cherry'))

# indexing
print(20 * '-', 'indexing', 20 * '-')
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

# adding element
print(20 * '-', 'adding element', 20 * '-')

fruits += ('pear',)
print(fruits)

fruits2 = ('mango', 'papaya', 'kiwi')
y = list(fruits2)
y.append('orange')
fruits2 = tuple(y)
print(fruits2)

# remove element
print(20 * '-', 'remove element', 20 * '-')
fruits2 = ('mango', 'papaya', 'kiwi')

y = list(fruits2)
y.remove('kiwi')
fruits2 = tuple(y)
print(fruits2)
