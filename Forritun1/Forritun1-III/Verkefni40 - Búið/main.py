listi1 = []     #Býr til tóman lista
listi2 = []     #Býr til tóman lista

from pathlib import Path
fin = open(Path(__file__).with_name("nofn.txt"))     #Opnar skrá
for line in fin:
    word = line.strip()      #Setur nafn í breytuna "word"
    if "e" in word:      #Ef það er e í nafninu þá
        listi1.append(word)      #bætir hann nafnið í listann
    if word[2]=="a":           #Ef að stafur númer 3 er þá gerir hann næstu línu
        listi2.append(word)        #Þá fer nafnið í lista2

#Prentar út niðurstöður
print ("Nöfnin sem innihalda stafinn e eru:", len(listi1))
print (listi2)
print ("Fjöldi nafnana sem eru með a sem þriðja staf eru:", len(listi2))