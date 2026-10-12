from random import randint
x = True
while x:
    samtals1=0
    samtals2=0
    running=True
    spilari1="j"
    spilari2="j"

    while running:
        if spilari1 =="j":
            tala1 = randint (1, 13)
            samtals1 = samtals1 + tala1
            print ("Spilari 1 dró spilið:", tala1)
        if spilari2 =="j":
            tala2 = randint (1, 13)
            samtals2 = samtals2 + tala2
            print ("Spilari 2 dró spilið:", tala2)
        print ("Spilari 1 er kominn í", samtals1)
        print ("Spilari 2 er kominn í", samtals2)

        if samtals1<=21 and samtals2<=21:
            if spilari1 == "j":
                spilari1 =str(input("Vill spilari 1 halda áfram (j/n): "))
            if spilari2 == "j":
                spilari2 =str(input("Vill spilari 2 halda áfram (j/n): "))

        if samtals1 > 21 and samtals2 > 21:
            print ("Báðir sprungu, jafntefli!")
            print ("--------------------------------------------")
            running = False
        elif samtals1 > 21:
            print ("Spilari 1 sprakk, spilari 2 vann")
            print ("--------------------------------------------")
            running = False
        elif samtals2 > 21:
            print ("Spilari 2 sprakk, spilari 1 vann")
            print ("--------------------------------------------")
            running = False

        if spilari1 == ("n") or spilari1== ("N") and spilari2 == ("n") or spilari2 == ("N"):

            if samtals1 == samtals2:
                print ("Jafntefli!")
                print ("--------------------------------------------")
                running = False
            elif samtals1 > samtals2:
                print ("Spilari 1 vann!")
                print ("--------------------------------------------")
                running = False
            elif samtals1 < samtals2:
                print ("Spilari 2 vann!")
                print ("--------------------------------------------")
                running = False

    aftur = str(input("Viltu nýjan leik? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Takk fyrir að spila")
        print ("--------------------------------------------")
        break
    else:
        print ("--------------------------------------------")
        running = True