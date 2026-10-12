while True:
    svar = int(input("Sláðu inn lengd: "))
    svar2 = int(input("Sláðu inn breidd: "))
    svar3 = int(input("Sláðu inn hæð: "))
    print ("Flatamálið er", svar * svar2)
    print ("Ummálið er", svar + svar + svar2 + svar2)
    print ("Rúmmálið er", svar*svar2*svar3)
    print ("-----------------------------------------")

    aftur = str(input("Viltu spila aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("-----------------------------------------")
        break