from pathlib import Path

print ("Liður")
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
print ("Stafurinn e er EKKI í", counter, "orðum")
print ("%.0f"%((ecounter/wordcounter)*100)+"% orða innihalda stafinn e")
print ("Orðin eru", wordcounter, "í heildina")

print ("------------------------------------------------------------------------")
print ("liður 2")
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
print ("Orðin sem EKKI innihalda stafina", leit, "eru", bcounter, "tala")

print ("------------------------------------------------------------------------")
print ("Liður 3 ")
acounter = 0
print ("%.0f"%((ecounter/wordcounter)*100)+"% orða innihalda stafinn e")
for line in text