list = []
svar = int(input("Hvað viltu slá inn margar einkunnir? "))
for i in range(0, svar):
    b = int(input("Sláðu inn tölu: "))
    list.append(b)          #

print ()
#Önnur leið til að gera sama hlutinn
medaltal = sum(list)/len(list)
print ("A) Meðaltal talnanna er:", round(medaltal,2))

print ()
#Einföldun
print("B) Meðaltala talnanna er:", round(sum(list)/len(list),2))
print ()