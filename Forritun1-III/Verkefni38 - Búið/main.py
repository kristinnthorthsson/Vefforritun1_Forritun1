def summa():                              #Fall sem gefur summu
    samtals = 0
    for i in range (0,len(listi)):              #Gerir jafn oft og lisinn er langur
        samtals += listi[i]                    #Leggur hverja tölu við samtals breytuna
    return samtals                    #Sendir töluna í samtals niður í forritið

def safntidni():           #Fall sem býr till safntíðni
    summ = 0
    safnt = []           #Tómur listi sem notandi fyllir inn í
    for i in range (0, len(listi)):     #Gerir jafn oft og lisinn er langur
        summ += listi[i]          
        safnt.append(summ)   #Bætir tölunni í listann safnt
    return (safnt)    

def rada():          #Fall sem raðar listanum
    listi.sort() 
    return listi       #Skilar listanum röðuðum niður í forritið
    
#Forritið byrjar hér
listi = []      #Tómur listi sem notandi fyllir inn í
svar = int(input("Hvað viltu slá inn margar tölur í listann?: "))       
for i in range (0, svar): 
    listi.append(int(input("Sláðu inn tölu: ")))
print ()
print ("Listinn er", svar, "og tölurnar eru:", listi)
print ()
print ("Summan er:", summa())
print ()
print ("Safntíðni er:", safntidni())
print ()
print ("Listinn raðaður:", rada())
print ("------------------------------ Búið ------------------------------")