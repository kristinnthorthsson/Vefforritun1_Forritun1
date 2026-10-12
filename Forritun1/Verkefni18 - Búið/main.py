while True:
    svar = int(input("Hvað viltu skrifa margar línur: "))
    for i in range (0, svar):
        print ("X"*30)
    aftur = str(input("Viltu spila aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("------------------------------------")
        break
    else:
        print ("------------------------------------")