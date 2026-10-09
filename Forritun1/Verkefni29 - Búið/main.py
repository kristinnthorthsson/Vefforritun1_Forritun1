x = True
while x:
    nafn = str(input("Sláðu inn nafn: "))
    print ()
    listi = []
    for i in range (0, len(nafn)): 
        if nafn[i] == " ":
            listi.append(i)
    print (listi)
    print ()
    if len(listi) == 1:
        print ("Fornafnið er:", nafn[0:listi[0]])
        print ()
        print ("Eftirnafnið er:", nafn[listi[0]:])
        print ()
    elif len(listi) == 2:
            print ("Fornafnið er:", nafn[0:listi[0]])
            print ()
            print ("Millinafnið er:", nafn[listi[0] + 1:listi[1]])
            print ()
            print ("Eftirnafnið er:", nafn[listi[1] + 1 :])
            print ()
    aftur = input("Viltu spila aftur? (j/n): ")
    if aftur == ("n") or aftur == ("N"):
        print ()
        print ("Takk fyrir að spila.")
        print ("------------------------------------------------------------")
        x = False