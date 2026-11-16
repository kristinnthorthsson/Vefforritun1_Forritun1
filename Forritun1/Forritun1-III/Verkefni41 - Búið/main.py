from pathlib import Path
fin = open(Path(__file__).with_name("nofn2_v41.txt"))
teljari = 0    #Teljari
for line in fin:
    word = line.strip()       #Setur nafn í breytuna word
    if len(word) > 30:        #Ef lengdin á nafninu er stærri en 30
        teljari += 1          #Hækkum teljaran um 1
        print (word)          #Prentum nafnið

print ()
print ("Nöfnin sem eru lengri en 30 eru:", teljari)
print ("--------------------------------------")
print ()

from pathlib import Path
fin = open(Path(__file__).with_name("nofn2_v41.txt"))
count = 0
teljari = 0    #Teljari
for line in fin:
    teljari2 = 0
    word = line.strip()       #Setur nafn í breytuna word
    for stafur in word:       #Les staf fyrir staf í nafninu
        if stafur == " ":     #Ef stafur er bil
            teljari2 += 1     #Hækkar um 1
    if teljari2 == 3:         #Ef teljarinn er 3 þá hefur hún fundið 3 bil í nafninu
        print (word)          #
        count+=1              #Hækkar teljara um 1 teljari telur hvað það eru mörg nöfn sem eru 4 nöfn

print ()
print (("Fjöldi nafna sem eru 4:", count))
print ("--------------------------------------")