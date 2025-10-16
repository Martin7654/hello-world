length = 3
width = 2
try:
    output = length / width
except ZeroDivisionError:
    print ("You can't divide by zero!")
    raise #spits out the error message
else:
    print(output)
finally: #always runs with or without an error
    print("Good joob!")