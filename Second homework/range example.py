for items in range(3,13): #last number is not included
    print(items)

for items in range (1,10,2): #last number is not included, step size of 2
    print(items)

for items in range (10,0,-1): #counting backwards
    print(items)

items=list(range(-100,0,10)) #counting up by tens from -100 to 0
print(items) #to print the list you need a variable

for items in range (5): #if only one number is given, it starts from 0
    print(items)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)): #length is the number of items, is important because you need an integer to read for the range function
    print(i, a[i])

for i in a:
    print(i)

print(sum(range(1,101))) #sums the numbers from 1 to 100