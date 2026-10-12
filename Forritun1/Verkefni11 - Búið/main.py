x = True
while x:
    svar = str(input("Viltu reikna margfeldi eða veldi? (m/v): "))
    if svar == ("m") or svar == ("M"):
        tala1 = int(input("Hvaða töflu viltu reikna? "))
        for i in range (1,11):
            print (tala1, "X", i, "=", tala1 * i)
    elif svar == ("v") or svar == ("V"):
            tala2 = int(input("Hvaða töflu viltu fá í veldi? "))
            for x in range (1,11):
                print (tala2, "í veldinu", x, "=", tala2 ** x)

    aftur = str(input("Viltu gera aftur? (j/n) "))
    if aftur == ("n") or aftur == ("N"):
        x = False
        print ("Forritið er búið")
    else:
        print ("-------------------------------------")
