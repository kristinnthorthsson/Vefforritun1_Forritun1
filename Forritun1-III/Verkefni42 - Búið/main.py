print ()
listi = ["ísland", "Kanada", "Bandaríkin", "Færeyjar", "Danmörk", "Svíþjóð", "Rússland", "Þýskaland", "Frakkland", "Bretland"]
print ("Þetta eru löndin sem þér stendur til að fara til:", " og ".join(listi))
print ("-----------------------------------------------------------------------")
print()
fjoldi = int(input("Hvað viltu bæta við mörgum löndum? (lágmark 5): "))

while fjoldi <= 4:
    print ()
    print ("Það þarf fleiri lönd.")
    print ()
    fjoldi = int(input("Hvað viltu bæta við mörgum löndum? (lágmark 5): "))
else:
    print ()
    for i in range(fjoldi):
        listi.append(str(input("Sláðu inn nýtt land sem þig langar til: ")))

print ()
print ("Þetta eru löndin sem þú getur farið til í stafrófsröð: ")
listi.sort()
for i in range(len(listi)):
    print (listi[i])

print ("-----------------------------------------------------------------------")

from random import randint

svar = randint(0, len(listi))
print ("Þú ferð til",listi[svar], "og þú verður þar í", svar, "vikur.")