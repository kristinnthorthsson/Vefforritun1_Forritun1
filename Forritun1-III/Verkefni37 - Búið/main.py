def fornafn():
    print ("-----------------------------------------------------------")
    svar = str(input("Sláðu inn fornafn sem þú vilt leita að: "))
    listi = []         #Býr til tóman lista
    from pathlib import Path
    fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
    for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
        word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
        listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
        if listi[0] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
            print (word)                          #Prentar út fornafnið

def eftirnafn():
        print ("-----------------------------------------------------------")
        svar = str(input("Sláðu inn eftirnafn sem þú vilt leita að: "))
        listi = []                                             #Býr til tóman lista
        from pathlib import Path                          #Sækja
        fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
        for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
            word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
            listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
            if listi[-1] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
                print (word)                           #Prentar úr efitrnafnið

def baedi():
    fornafn()
    eftirnafn() 

def valmynd():            #Fall sem byrtir upphafsvalmyndina
    while True:
        print ("-----------------------------------------------------------")
        print ()
        print("Veljið:")
        print ("1) Leita eftir fornafn")
        print ("2) Leita eftir eftirnafn")
        print ("3) Leita eftir fornafn of eftirnafn")
        print ("4) Til að hætta")
        print ()
        svar = int(input("Svar: "))
        if svar == 1:
            fornafn()
        elif svar == 2:
            eftirnafn()
        elif svar == 3:
            baedi() 
        elif svar == 4:
            print ("------------------------- Búið -----------------------------")
            break
valmynd()