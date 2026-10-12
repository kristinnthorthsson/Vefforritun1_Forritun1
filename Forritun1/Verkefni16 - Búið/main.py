x = True
while True:
    for i in range (200, 149, - 1):
        print (i)

    aftur = str(input("Viltu fara á næsta? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("------------------------------------")
        break
    else:
        print ("------------------------------------")
    
    for k in range (50, 101, + 5):
        print (k)
    aftur = input("Viltu fara í næsta? (j/n): ")
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("------------------------------------")
        break
    else:
        print ("------------------------------------")

    svar = str(input("Sláðu á lyklaborðið: "))
    if svar == ("q") or svar == ("Q"):
        print ("Forritið búið")
        print ("------------------------------------")
        break
    print ("Þú slóst", svar, "á lyklaborðið")
    aftur = input("Viltu fara á næsta? (j/n): ")
    if aftur == ("n") or aftur == ("N"):
        break
        print ("------------------------------------")
    else:
        print ("------------------------------------")

    aldur = int(input("Hvað ertu gamall/gömul? "))
    faedingarAr = (2026 - aldur)
    print ("Þú ert fæddur árið", faedingarAr)
    print ("Forritið búið")
    print ("------------------------------------")
    break