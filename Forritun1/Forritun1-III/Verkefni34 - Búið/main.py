print ("--------------------------- Liður 1 ---------------------------")
from pathlib import Path
fin = open(Path(__file__).with_name("nofn_v34.txt"))     #Opnar skrána
nafn = str(input("Sláðu inn nafn sem þú vilt leita að: "))   #Spyr
satt = False    #Breyta sem verður trú ef nafnið finnst
for line in fin:
    word = line.strip()        
    if nafn == word:        #Ef nafnið finnst í skránni
        print("Nafnið", nafn, "fannst")   #Prentast út ef það finnst
        satt = True
if satt == False:            #Ef nafnið hefur ekki fundist
    print ("Nafnið", nafn, "fannst ekki")

print ("--------------------------- Liður 2 ---------------------------")
teljari_max = 0          #Geymir
teljari_min = 1000          #Geymir
from pathlib import Path
fin = open(Path(__file__).with_name("nofn_v34.txt"))     #Opnar skrána
for line in fin:
    word = line.strip()
    if len(word) > teljari_max:     #Ef lengdin á orðinu (word) er stærra en talan í teljari_max
        teljari_max = len(word)     #Þá fer lengdin á orðinu í breytuna
    if len(word) < teljari_min:     #Ef lengdin á orðinu (word) er minni en talan í teljari_min
        teljari_min = len(word)     #Þá fer lengdin á orðinu í breytuna
print ("Lengsta nafnið er:", teljari_max, "stafir að lengd")
print ("Stysta nafnið er:", teljari_min, "stafir að lengd")

print ("--------------------------- Liður 3 ---------------------------")
from pathlib import Path
fin = open(Path(__file__).with_name("nofn_v34.txt"))     #Opnar skrána
for line in fin:
    word = line.strip()
    if len(word) == teljari_max:      #Ef lengdin á orðinu er sá sami og teljari_max
        print ("Þetta er lengsta nafnið:", word)
    elif len(word) == teljari_min:      #Ef lengdin á orðinu er sá sami og teljari_min
        print ("Þetta er stysta nafnið", word)

print ("--------------------------- Búið ---------------------------")