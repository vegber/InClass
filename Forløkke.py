

streng = input("Streng")
fyrste = -1
for i in range(len(streng)-2):
    delstreng = streng[i:i+3]
    if delstreng.isdigit() and fyrste == -1:
        fyrste = i
if fyrste == -1:
    print("Strengen", streng,
          "har ikkje tre etterfylgjande siffer. ")
else:
    print("Fyrste forekomst av tre etterfylgjande siffer "
          "er", streng[fyrste:fyrste + 3])