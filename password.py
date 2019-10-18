

passord = input("Passord: ")
lengd = len(passord)
if lengd < 10:
    print("Passord er for kort og må ha minst 10 karakterar")
else:
    smaa = 0
    store = 0
    siffer = 0
    andre = 0
    for karakter in passord:
        if karakter.islower():
            smaa += 1
        elif karakter.isupper():
            store += 1
        elif karakter.isdigit():
            siffer += 1
        else:
            andre += 1
    if smaa >= 3 and store >= 2 and siffer >=1 and andre >= 2:
        print("Passordet ditt e altfor komplisert")
    else:
        print("Ugyldig passord. ")


