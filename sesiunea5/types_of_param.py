###########################################################################
def plus(a,b): # a, b - positional arguments
    return a+b

plus(1,2)
###########################################################################
# default arguments

def plus(a, b=2): # b has default value 2
    return a+b

print(plus(1))
plus(1,3)
###########################################################################
# keyword arguments

def plus(a,b):
    return a+b

plus(a=1, b=2)
plus(b=2, a=1) # specificand argumentele prin nume nu mai este necesar sa
# pastram ordinea lor

###########################################################################
# variable number of arguments

def plus(*args): #args - colecteaza toate elementele intr-un tuplu
    print(args)
    return sum(args)
plus(1,2,3)
plus()
plus(5)
plus(*[1,2,3]) # * despacheteaza lista si ia valorile ca la linia 30
# * -> unpacking

def plus(**kwargs):
    print(kwargs)
    return sum(kwargs.values())

plus(a=1, b=2)
plus()
plus(c=5)
plus(**{'a':1, 'b':2}) # echivalent cu linia 40

def plus(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

plus(1)
plus(1, d=7)
plus()
plus(1,2,3, c=9)
plus(z=13)
# plus(d=7, 1) -> error because positional argument after keyword argument

###########################################################################
def plus(a,b):
    print(a,b)
    return a+b
plus(1,2)
plus(*[1,2])
plus(**{'a':2,'b':2})
plus(a=1, b=2)


