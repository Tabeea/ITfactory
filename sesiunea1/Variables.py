# variable -> a container from memory for storing values

# 1.creating a variable

x = 5
y = 'John'
print(x)
print(y)

x = y
print(x)

# 2. Naming a variable
'''
a) a variable must start with a letter or the underscore character: _
b) a variable cannot start with a number
c) a variable name can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, _ )
d) variable names are case-sensitive 
'''
# this  way is correct
myvar = 5
my_var = 5
_my_var = 5
myVar = 5
MYVAR =5
myvar2 = 5

# NOT THIS WAY
# 2myvar2 = 5
# my-var = 5
# my var = 5

# 3. Many values to multiple variables
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
k,h,j = x, 'mere', True
print(k, h, j)  #1 mere True

# 4. One value to multiple variables
x = y = z = 'portocala' #Afiseaza portocala portocala portocala
print(x, y, z)






