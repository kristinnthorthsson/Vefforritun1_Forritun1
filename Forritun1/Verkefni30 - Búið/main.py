listi1 = ["Hundur", "Köttur", "Fiskur", "Fugl", "Mús", "Kanína", "Hamstur", "Skjaldbaka", "Froskur", "Slanga"]
listi2 = []
teljari = 0
stafir = 0

for i in range (0, 5):
    listi2.append(str(input("Sláðu inn dýrategund: ")))

for x in listi1:
    for y in listi2:
        if x == y:
            teljari += 1
print()
print ("Sama dýrið kom", teljari,"sinnum fyrir í báðum listunum.")
for dyr in listi1:
    stafir += len(dyr)
print ()
print ("Það eru", stafir, "stafir í dýralistanum.")
print ("------------------------------------------------------------------------------------------------------")