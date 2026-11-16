k = True
while k:
#1.
    print ()
    skoli = ("Fjölbrautaskólinn í Breiðholti")
    skoli2 = ("Menntaskólinn í Kópavogi")
    print (skoli[0:17] + skoli2[13:25])

    print ()

#2.
    nafn = ("Kristinn Þór Þórhallsson")
    for stafur in nafn:
        print (stafur, "+", end=" ")

    print ()

#3.
    print (nafn[::-1])
    print ()

#4.
    x = True
    while x:
        svar = str(input("Hvaða skóla ertu í?: "))
        if svar == ("FB"):
            print ("Rétt")
            x = False
        else:
            x = True
    print ()

#5.
    f = True
    while f:
        aftur = str(input("Viltu gera aftur? (Já/Nei): "))
        if aftur == ("Já") or aftur == ("JÁ"):
            print ("-------------------------------------------------------------------")
            k = True
            f = False
        elif aftur == ("Nei") or aftur == ("NEI"):
            k = False
            f = False
            print ("Forritið er búið")
            print ("-------------------------------------------------------------------")
        else:
            ("?")
            f = True