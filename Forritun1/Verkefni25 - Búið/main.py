from random import randint
x = True
while x:
    listi = ["Kristinn", "Hallgrímur", "Steingrímur", "Andri", "Jón"]
    tala = randint (0, 4)
    print ("Til hamingju", listi[tala], "Þú hefur unnið milljón í happadrætti FB")
    print ("Þessir unnu ekkert: ", end=" ",)
    for i in range (0, len(listi)):
        if i !=tala:
            print  (listi[i], end=" ")
            if i < len(listi) - 1:
                print (", ", end=" ")
    print()
    print ("----------------------------------------------------")
    aftur = str(input("Viltu draga aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Takk fyrir að spila.")
        print ("----------------------------------------------------")
        x = False
    else:
        print ("----------------------------------------------------")