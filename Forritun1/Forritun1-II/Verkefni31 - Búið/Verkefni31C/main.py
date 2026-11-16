def fall(s1,s2):
    listi = []
    for stafur in s1:
        if stafur in s2:
            listi.append(stafur)
    print(listi)
    print(list(set(listi)))
strengur1 = str(input("Sláðu inn streng 1: "))
strengur2 = str(input("Sláðu inn streng 2: "))
fall(strengur1, strengur2)