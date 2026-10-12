listi = ["Ísland", "Argentína", "Þýskaland", "Frakkland", "England", "Belgía", "Rússland", "Kanada", "Póland", "Úngverjaland"]

num = 0
while num < 5:
    num = int(input("Hvað viltu bæta við mörgum löndum? "))
for i in range (0, num):
    listi.append (str(input("Sláðu inn nýtt land á listann: ")))
print ()
print ("--------------------------------------------------")
print ()
print ("Löndin eru: ", listi)
listi.sort()
print ()
print ("--------------------------------------------------")
print ()
print (len(listi))
print ()
print ("---------------------------------------------------")
print ()
print ("Þriðja hvert land á listanum er: ",end=" ")
for x in range(0, len(listi), 3):
    print (listi[x], end = " ")
print ()
print ()
print ("---------------------------------------------------")
print ()
print ("Landið sem er í miðjunni er: ", listi[(round(len(listi)/2)-1)])
print ()
print ("---------------------------------------------------")
print ()
print ("Fyrsti stafurinn í öllum löndunum er: ", end=" ")
for y in listi:
    print (y[0], end = " ")
print ()
z = round (len(listi)/2)
print ()
for s in range (0, z):
    print (listi[s], listi [-(s + 1)], end = " ")