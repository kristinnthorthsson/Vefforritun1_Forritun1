while True:
    svar = int(input("Sláðu inn mánuð í tölustöfum (1-12): "))
    if svar == (1):
        print ("Janúar")
    elif svar == (2):
        print ("Febrúar")
    elif svar == (3):
        print ("Mars")
    elif svar == (4):
        print ("Apríl")
    elif svar == (5):
        print ("Maí")
    elif svar == (6):
        print ("Júní")
    elif svar == (7):
        print ("Júlí")
    elif svar == (8):
        print ("Ágúst")
    elif svar == (9):
        print ("September")
    elif svar == (10):
        print ("Október")
    elif svar == (11):
        print ("Nóvember")
    elif svar == (12):
        print ("Desember")

    aftur = str(input("Viltu spila aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("------------------------------------")
        break
    else:
        print ("------------------------------------")