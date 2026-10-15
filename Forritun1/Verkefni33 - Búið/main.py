from pathlib import Path

print ("Liður 1")
counter = 0
ecounter = 0
wordcounter = 0

e=("e")
text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    wordcounter+=1
    if e not in word:
        counter+=1
    if e in word:
        ecounter+=1
print ("Stafurinn e er ekki í", counter, "orðum")
print ("%.0f"%((ecounter/wordcounter)*100)+"% orða innihalda stafinn e")
print ("Orðin eru", wordcounter, "í heildina")

print ("------------------------------------------------------------------------")

print ("Liður 2")
leit = str(input("Sláðu inn einhverja bókstafi: "))
bcounter = 0
text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    fann = False
    for stafur in leit:
        if stafur in word:
            fann = True    
    if fann == False:
        bcounter +=1
print ("Orðin sem ekki innihalda stafina", leit, "eru", bcounter, "tala")

print ("------------------------------------------------------------------------")

print ("Liður 3 ")
acounter = 0
text = open(Path(__file__).with_name("words.txt"))     #opna skrá
for line in text:                                      #les línu fyrir línu
    word = line.strip()                                #tekur stýritákn út
    for stafur in word:
        acounter +=1
print ("Það eru", acounter, "í öllu skjalinu")  

print ("------------------------------------------------------------------------")