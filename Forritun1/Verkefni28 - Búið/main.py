x = True
while x:
    strengur = str(input("Sláðu inn streng: "))
    stafur = str(input("Sláðu inn bókstaf sem þú vilt leita af: "))
    teljari = 0
    for i in strengur:
        if i == stafur:
            teljari += 1
    print ("Strengurinn er", strengur, "og stafurinn", stafur, "kemur", teljari, "sinnum fyrir í orðinu.")
    print ("í öfugri röð er orðið:", strengur[::-1])

    aftur = str(input("Viltu spila aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Takk fyrir að spila")
        print ("------------------------------------------------------------")
        x = False
    else:
        print ("------------------------------------------------------------")