spurning = int(input("Veldu 1 fyrir fornafn eða 2 fyrir eftirnafn: "))
if spurning == (1):
    svar = str(input("Sláðu inn fornafn sem þú vilt leita að: "))
    list = []         #Býr til tóman lista
    from pathlib import Path
    fin = open(Path(__file__).with_name("nofn(3).txt"))     #Opnar skrána
    for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
        word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
        listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
        if listi[0] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
            print (word)     
if spurning == (2):
    svar = str(input("Sláðu inn eftirnafn sem þú vilt leita að: "))
    list = []                                             #Býr til tóman lista
    from pathlib import Path                          #Sækja
    fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
    for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
        word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
        listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
        if listi[-1] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
            print (word)
else:
    print ("Ekki hægt")

print ("------------------------------ Búið -------------------------------")                 #Prentar að forritið er búið