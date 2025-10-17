# Create a new program using the formulas from Exercises 2 and 5 that first asks the user whether a conversion from Celsius to Fahrenheit or the other way around is desired. 
# Then print a table of values converting one unit to the other. 
# For the conversion from C to F print the range of values from -20 to +40; for conversion from F to C print the values from -10 to +110.

Temperatur_input = input("For C => F enter C, for F => C enter F: ")

if Temperatur_input == "C":
    C= -21
    while C < 40: #while loop until 40
        C += 1 #adds a degree every loop
        F = (9/5)*C+32 #calculate fahrenheit
        print (C, "C =>",round(F,1),"F") #print the way prof wants, repeat loop until C>40
elif Temperatur_input == "F":
    F= -11
    while F < 110:
        F += 1
        C= round(5/9*(F - 32),2)
        print (F, "F =>",round(C,1),"C") #print the way prof wants, repeat loop until F>110

else:
    print("You made a mistake")