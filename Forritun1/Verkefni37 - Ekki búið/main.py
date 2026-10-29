print ("Veljið:")
print ("1) leita eftir fornafni \n2) leita eftir eftirnafni \n3) leita eftir fornafn og eftirnafn \n4) til að hætta")  #\n gerir aðra línu
print ()                         #Bil
svar = int(input("Svar: "))

if svar == (1):
    print ("------------------------------ 1 --------------------------------")
    svar = str(input("Sláðu inn fornafn sem þú vilt leita að: "))
    list = []         #Býr til tóman lista
    from pathlib import Path
    fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
    for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
        word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
        listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
        if listi[0] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
            print (word)
     
elif svar == (2):
    print ("------------------------------ 2 --------------------------------")
    svar = str(input("Sláðu inn eftirnafn sem þú vilt leita að: "))
    list = [0]                                             #Býr til tóman lista
    from pathlib import Path                          #Sækja
    fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
    for line in fin:                                      #Les í gegnum allar línurnar í textaskránni
        word = line.strip()                            #Eyðir stýritáknum úr línu (t,d) enter 
        listi = word.split(" ")                          #Splitar nafninu upp þar sem er bil
        if listi[-1] == svar:                        #Ef að svar er 0 - 1 í listanum er það sama og nafnið sem við leitum að
            print (word)

elif svar == (3):
    print ("------------------------------ 3 --------------------------------")
    svar1 = str(input("Sláðu inn fornafn sem þú vilt leita að: "))
    svar2 = str(input("Sláðu inn eftirnafn sem þú vilt leita að: "))
    list = [0]                #Býr til tóman lista
    from pathlib import Path
    fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrána
    for line in fin:
        word = line.strip()
        listi = word.split(" ")
        if list[0] == svar1 and list[-1] == svar2:
            print (word)

elif svar == (4):
    print ("Hættur í forritinu")

print ("------------------------------ Búið --------------------------------")          #Prentar að forritið er búið