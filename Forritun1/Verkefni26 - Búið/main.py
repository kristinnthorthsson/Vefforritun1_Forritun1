from random import randint
x = True
while x:
    strakur = str(input("Strákur: "))
    stelpa = str(input("Stelpa: "))
    tala = randint (0,100)
    print ("Það eru", str(tala) + "% líkur á að", strakur, "og", stelpa, "byrji saman.")
    kk = len(strakur) // 2
    kvk = len(stelpa) // 2
    print ("Barnið þeirra mun heita: ", strakur[0: kk]+stelpa[kvk:])

    aftur = str(input("Viltu spila, viltu spila aftur? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("-----------------------------------")
        print ()
        x = False
    else:
        print ("-----------------------------------")
        print ()