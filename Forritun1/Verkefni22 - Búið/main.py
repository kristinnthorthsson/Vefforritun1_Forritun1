listi = ["Hestur","Kýr","Köttur","Hundur","Björn"]

print (len(listi[3]))
print ("Þessi dýr eru:", end=" ")
for i in listi:
    print (i, end = " ")
print ()
print ("-----------------------------------------------")
for i in range (0, 3):
    listi.append (str(input("Sláðu inn nýtt dýr: ")))
print ("Listinn minn lítur þá svona út: ", listi)
listi.sort()
print ("Svona lítur listinn raðaður í stafrósröð")
for i in range (0, len(listi)):
    print ("Dýr nr", i + 1, "á listanum er", listi[i])