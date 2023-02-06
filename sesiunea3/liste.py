# lists are used to store multiple items in a single variable
# list items are ordered, changeable and allow duplicates

# Create

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
cars = list(('BMW', 'Audi', 'Tesla'))

# Indexing - accesing elements
print(20 * '-', 'indexing', 20 * '-')
print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])
print(numbers[::-1])

# add element

print(20 * '-', 'add indexing', 20 * '-')
numbers.append(10)
print(numbers) #append adauga la final
numbers.insert(4, 6)
print(numbers)

#remove element
print(20 * '-', 'indexing', 20 * '-')
elem = numbers.pop() #elimina ultimul element si il si returneaza
print(elem)
print(numbers)

numbers.pop(0)
print(numbers)  # elimina primul element

numbers.remove(3)
print(numbers) # scoate un singur element (un singur 3)

# remove all elements
print(20 * '-', 'remove all elements', 20 * '-')
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]
# replace
print(20 * '-', 'replace', 20 * '-')
fruits[1] = 'pear'
print(fruits)

# Count
print(20 * '-', 'count', 20 * '-')
print(numbers.count(3))

# add two list

print(20 * '-', 'add two list', 20 * '-')
numbers2 = [10, 11, 12]
print(numbers + numbers2)

numbers.extend(numbers2)
print(numbers)

# reverse
print(20 * '-', 'reverse', 20 * '-')
print(numbers[::-1])

numbers.reverse() # in place
print(numbers)

# sort
print(20 * '-', 'sort', 20 * '-')
numbers = [ 1, 8, 7 , 4, 3, 8, 18]
numbers.sort() # in place
print(numbers)
numbers.sort(reverse=True)
print(numbers)