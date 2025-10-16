length = 3
width = 2
try:
    output = length / width
except ZeroDivisionError:
    print ("You can't divide by zero!")
    raise

print(output)