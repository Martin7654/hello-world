a_string = 'What a beautiful snake!'
a_string.upper() #new string, with uppercase letters, does not assign the string to a variable, nothing happens here
print(a_string)
a_string = a_string.upper() #new string assigned to a_string, the original remains unchanged, but no more accest
print(a_string)

print()
print(a_string.split())
a_string = 'Steve, Paul, Susan, Anna, Peter, Amy'
print(a_string.split(', ')) #make a list of alle the names
