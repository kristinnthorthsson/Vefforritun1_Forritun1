x = True
while True:
    svar = int(input("Sláðu inn póstnúmer: "))
    if svar > (101) and svar < (117):
        print ("Reykjavík")
        print ("------------------------------------")
    elif svar > (169) and svar < 173:
        print ("Seltjarnarnes")
        print ("------------------------------------")
    elif svar == 190:
        print ("Vogar")
        print ("------------------------------------")
    elif svar > 199 and svar < 204:
        print ("Kópavogur")
        print ("------------------------------------")
    elif svar > 209 and svar < 213:
        print ("Garðarbær")
        print ("------------------------------------")
    elif svar > 219 and svar < 223:
        print ("Hafnafjörður")
        print ("------------------------------------")
    elif svar == (225):
        print ("Álftarnes")
        print ("------------------------------------")
    elif svar > 229 and svar < 236:
        print ("Reykjanesbær")
        print ("------------------------------------")
    elif svar == (240):
        print ("Sandgerði")
        print ("------------------------------------")
    elif svar == (250):
        print ("Garði")
        print ("------------------------------------")
    elif svar == (260):
        print ("Reykjanesbær")
        print ("------------------------------------")
    elif svar > (269) and svar < (277):
        print ("Mosfellsbær")
        print ("------------------------------------")
    else:
        print ("Ekki til")
        print ("------------------------------------")
    aftur = str(input("Viltu gera aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið er búið")
        print ("------------------------------------")
        break
