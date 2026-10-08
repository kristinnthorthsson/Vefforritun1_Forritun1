listi = ["Jón", "Kjartan", "Ragnar", "Ólafur", "Kristinn", "Þór", "Hallgrímur", "Steingrímur", "Andri", "Björn"]

print (len((listi[3])))
strengur = "Háfjallaveiki"
listi.sort()
print ("Nöfnin eru:", end=" ")
for i in listi:
    print (i, end = " ")
print ()
print (listi [5:8])
print (listi [-4:])
print (strengur[2:7])
print (strengur[8:14])
print (strengur[0:2], strengur[8:14])