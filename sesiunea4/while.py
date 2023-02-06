#intro_loop   '''
'''A loop is a sequence of instructions that is continually repeated
until a certain condition is reached.
(O bucla, este o secventa de instructiuni care se repeta incontinuu,
pana o anumita conditie este indeplinita.)

An infinit loop is one that doesn't have an exit.
The result is that the loop repeats until the operating system senses it and terminates the program
with an error.
(O bucla infinita, este una care nu are iesire.
Rezultatul este ca, bucla se va repeta pana cand sistemul de operare o detecteaza, si opreste programul cu o eroare.
'''

#  With the while loop we can execute a set of statements as long as a condition is true.

count = 0
while count < 3:
    count += 1
    print(f'count:{count}')


l = [1, 2, 3, 4, 5]
index = 0
while len(l) > index:
    print(l[index])
    index += 1

print(50*"#")
# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # stops the iteration
    i += 1

print(50*"#")
# continue
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue  # skips the code below
    print (i)

print(50*"#")
# else
count = 0
while count < 3:
    count += 1
    print(count)
else:  # runs when the loop ends
    print('In else block.')

print(50*"#")
# else + break
count = 0
while count < 3:
    count += 1
    print(count)
    if count == 1:
        break
else:  # does not run when a break happened in the loop
    print('In else block.')