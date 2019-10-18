

for i in range(1, 11):
    linje = ''
    for j in range(1, 11):
        produkt = i * j
        streng = '%10d' % produkt
        linje += streng
    print(linje)

