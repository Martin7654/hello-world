msg1 = "I am a file."
msg2 = "I am better then the README file somehow."
print (msg1)
print (msg2)    
a = 5
b = 7
c= 2
print (a-b*c)
print("This is the best file everrrr")
# My first comment yeahh
print (4/7*(4+7)) #float 0.1 vs integer 0 number 
print (int (6.285714285714286))
print (7//3) #floor division for integer result
print (7%3) #remainder of the division
print (5**2) #exponentiation Hochzahlen 
variable=45 #equal sign makes variables 
variable2=3
print (variable+variable2)
print (7+8+5)
_=20
print(_*4) #underscore is the last result, only works in interactive mode
print('Single quotes work too') #string data type, also numbers become strings with quotes
print('"This is crazy" he said') #for quotes use the other quotations or \
print('"This isn\'nt crazy" he said')
print("First line\nSecond line") #\n new line and print does understand special characters
print(r"First line\nSecond line") #r raw string, prints out everything exactly
#somehow an odd number of \Backlashes doesn't work use \\ instead
print(3*"unz"+"uuu")
print(7*"7"+"777") #you can add and multiply strings
print("""\
This is a multi line string
But also more somehow""") #\prevents the new line at the beginning
# """ for multi line strings
print("Hello" "world") #automatic string concatination (addition), good to break long strings
print ("77777777777777777777777777777777777777777777777777777777777777777777777777"
       "777777777777777777777777777777777777777777777777777777777777777777777777777")
text="Something will stand here" #this is a variable
print(text)
print(text+" This is the answer") #variable and string need a + to combine, , adds a space
print(text[8]) #indexing starts at 0, prints the 9th character
print(text[-1]) #last character
print(text[0]) #0 here is 1st character
print(text[0:-1]) #slicing, up to but not including the last character
print(text[:9]+text[9:]) #slicing, from beginning to 9th character and from 9th character to end
#the first character is always included the last one alwayss excluded, slicing is between the characters
print(text[4:10]+text[-10:-5])
print(text[4:100]) #no error if the end index is out of range
#strings are immutable, you can't change them by indexing, instead create a new string
print("L"+text[1:]) #change first character
print(len(text)) #length of the string
list1=[1,2,3,4,5] #list data type, can contain different data types
list2=["milk","eggs","bread"] #list of strings
print(list1)
print(list2)    
print(list1 [3:]) #slicing works too, returns a new list
print(list1 + list2) #concatenation works too
list1[4]= 6 #change an element of the list, 0 is the first element, not possible for strings in lists
print(list1)
list2.append("cheese") #add an element to the end of the list
print(list2)
list100=list1 #not a copy, just another name for the same list
list100.append(7) #add an element to the copy
print(list1)
print(list1 == list100) #check if lists are equal
list100[4]=5 #change an element of the copy
print(list1)
print(list100)
copylist1=list1[:] #make a real copy of the list with slicing
copylist1[5]=6
print(list1)
print(copylist1) 
copylist1[1:3]=[3,2] #change an element of the copy with slicing
copylist1[4:8]=[] #delete elements with empty list
print(copylist1)
print(len(copylist1)) #length of the list
list3=[list1,list2,copylist1] #list of lists, which are called nested lists
print(list3)
print(list3[1][3]) #indexing nested lists
a,b=0,1 #multiple assignment
while a<100: #while loop
    print(a, end=",") #end prevents new line
    a,b=b,a+b #Fibonacci numbers

print(4!=5)
print(4==4)
import math #importing a module
print(math.sqrt(16))
