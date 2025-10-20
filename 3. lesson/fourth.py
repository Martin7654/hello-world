A_STRING = 'What a beautiful snake!'
for char in A_STRING: # assigns to an element, W first element
    print(char)
for index, char in enumerate(A_STRING): #firt index is 0, char is W, enumerate for postition
    print(f'{index:2}: {char}') #index:2: 2 makes it two spaces wide
