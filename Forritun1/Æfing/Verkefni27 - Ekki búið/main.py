from random import randint
aftur = True
while aftur:                            #Keyrir á meðan breytan er True
    samtals1 = 0                        #Samtals stig fyrir spilara 1
    samtals2 = 0                        #Samtals stig fyrir spilara 2
    running = True                      #Þessi breyta er True á meðan spilarar vilja halda áfram
    spilari1 = "j"                      #Þessi er True á meðan spilari 1 vill halda áfram
    spilari2 = "j"                      #Þessi er True á meðan spilari 2 vill halda áfram

    while running:                           #Keyrir á meðan breytan er True
        if spilari1 == ("j"):                #Ef spilari 1 velur j (halda áfram)
            tala1 = randint (1, 13)          #Velur tölu frá 1-13
            samtals1 = samtals1 + tala1         #Leggur töluna við samtals
            print ("Spilari 1 dró spilið", tala1)  #Prentar úr random töluna sem tölvan valdi
        if spilari2 == ("j"):                #Ef spilari 2 velur j (halda áfram)
            tala2 = randint (1, 13)          #Velur tölu frá 1-13
            samtals2 = samtals2 + tala2         #Leggur töluna við samtals
            print ("Spilari 2 dró spilið", tala2)  #Prentar úr random töluna sem tölvan valdi
        print ("Spilari 1 er nú kominn með", samtals1)    #Prentar út hvað spilari 1 er kominn með mikið
        print ("Spilari 2 er nú kominn með", samtals2)    #Prentar út hvað spilari 2 er kominn með mikið

        if samtals1 <=21 and samtals2 <=21:  #Athugar hvort að þeir séu komnir yfir 21, geir bara ef þeir eru ekki sprungnir
            if spilari1 == ("j"):            #Athugar hvort spilari 1 er hættur
                spilari1 = str(input("Vill spilari 1 halda áfram? (j/n): "))    #Athugar hvort spilari 1 vilji halda áfram að draga
            if spilari2 == ("j"):            #Athugar hvort spilari 1 er hættur
                spilari2 = str(input("Vill spilari 2 halda áfram? (j/n): "))    #Athugar hvort spilari 2 vilji halda áfram að draga
        
        #Athugar hvort einhver sé kominn yfir 21 og er sprunginn
        if samtals1 >=21 and samtals2 >=21:    #Ef báðir eru sprungnir
            print ("Báðir sprungu, jafntefli! Spilari 1 var komin í", samtals1, "og spilari 2 var komin í", samtals2)    #Prentar út að báðir eru sprungir
            running = False       #Stoppar while skipunina

        if samtals1 >=21 and samtals2 <=21:    #Ef spilari 1 sprakk og spilari 2 vann
            print ("Spilari 1 sprakk með", samtals1)    #Prentar út að spilari 1 sprakk
            print ("Spilari 2 vann með", samtals2)      #Prentar út að spilari 2 vann
        elif samtals1 >=21:                             #Ef spilari 1 er sprunginn
            print ("Spilari 1 sprakk með", samtals1)
            print ("Spilari 2 vann!")    #Prentar út að spilari 1 sprakk og spilari 2 vann
            running = False        #Stoppar while skipunina 
        elif samtals2 >=21:                             #Ef spilari 2 er sprunginn            
            print ("Spilari 2 sprakk!")    #Prentar út að spilari 2 er sprunginn
            print ("Spilari 1 vann!")   #Prentar út að spilari 2 vann
            running = False        #Stoppar while skipunina

        #Ef báðir vilja ekki draga fleiri spil
        if spilari1 == ("n") and spilari2 == ("n"):          #Ef báðir hafa valið að hætta
            
            #Jafntefli
            if samtals1 == samtals2:                     #Ef það var jafntefli
                print ("Jafntefli! Báðir voru með", samtals2)      #Prentar út jafntefli
                running = False          #Stoppar while skipunina

            #Ef spilari 1 vann
            if samtals1 > samtals2:        #Ef samtals spilara 1 er með hærri en spilara 2
                print ("Spilari 1 vann!")
                running = False          #Stoppar while skipunina

            #Ef spilari 2 vann
            elif samtals1 < samtals2:        #Ef samtals spilara 2 er með hærri en spilara 1
                print ("Spilari 2 vann!")
                running = False         #Stoppar while skipunina

    aftur = input("Viltu nýjan leik? (j/n): ")
    if aftur == ("n") or aftur == ("N"):
        print ("Takk fyir að spila")
    running = False
    break
    if aftur == ("j") or aftur == ("J"):
        print ("--------------------------------------------------------------")
        running = True            #Þessi breyta er True á meðan spilarar  vilja halda áfram