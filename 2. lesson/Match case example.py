# new if statement that uses match and case
LANG="en"
match LANG:
    case "en":
        print("Good morning!")
    case "fr":
        print("Bonjour!")
    case "es":
        print("¡Buenos días!")
    case _: #_ is the else in this version
        print("Hello!")