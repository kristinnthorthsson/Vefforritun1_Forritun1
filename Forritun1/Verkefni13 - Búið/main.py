x = True
while x:
    nafn = str(input("Sláðu inn nafn: "))
    print ("Þú heitir", nafn)
    aftur = str(input("Viltu halda áfram? (j/n) "))
    if aftur == ("n") or aftur == ("N"):
        x = False
        print ("Forritið er búið.")
    else:
        print ("---------------------------------------------")

    aldur = int(input("Hvað ertu gamall/gömul?: "))
    print ("Þú ert", aldur, "ára. ")
    aftur1 = str(input("Viltu halda áfram? (j/n) "))
    if aftur1 == ("n") or aftur1 == ("N"):
        x = False
        print ("Forritið er búið.")
    else:
        print ("---------------------------------------------")

    print ("Þú heitir", nafn, "og þú ert", aldur, "ára.")
    x = False
    print ("---------------------------------------------")

    for i in range (1,11):
        print (i)