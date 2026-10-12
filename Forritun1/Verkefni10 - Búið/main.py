x = True
while x:
    svar = int(input("Hvaða töflu viltu reikna? "))
    for i in range (1, 11):
        print (svar, "X", i, "=", svar * i)
    aftur = str(input("Viltu gera aftur? (j/n) "))
    if aftur == "n" or aftur == "N":
        x = False
        print ("Forritið er búið")