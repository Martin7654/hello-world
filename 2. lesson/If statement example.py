#if statement example
language = input("Enter your language: ")
if language == "english":
    print("Good morning")
elif language == "french":
    print("Bonjour")
elif language == "spanish":
    print("Buenos dias")
elif language == "italian":
    print("Buongiorno")
else:
    print("This program does not support this language")