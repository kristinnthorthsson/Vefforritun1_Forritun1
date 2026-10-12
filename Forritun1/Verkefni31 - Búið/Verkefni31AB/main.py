x = True
while x:
    def hastafir(t):
        print (t.upper())
    def lastafir(t):
        print (t.lower())
    strengur = str(input("Sláðu inn textastreng: "))
    svar = str(input("Viltu breyta strengnum í hástafi eða lástafi? (h/l): "))
    if svar == ("h") or svar == ("H"):
        hastafir(strengur)
    elif svar == ("l") or svar == ("L"):
        lastafir(strengur)
    aftur = input("Viltu spila aftur? (j/n): ")
    if aftur == ("n") or aftur == ("N"):
        print ("Takk fyrir að spila.")
        print ("----------------------------------------------------------------------")
        break
    else:
        print ("----------------------------------------------------------------------")