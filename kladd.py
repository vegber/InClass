
""" skriv ut  om eit innlest navm er langt,
passeleg langt eller kort
"""

namn = input()
print(namn) 
lengd = len(namn)
if lengd > 10:
    print(" Navnet er langt")
elif lengd > 6:
    print("Navnet er passeleg langt. ")
else:
    print("Navnet er kort")
