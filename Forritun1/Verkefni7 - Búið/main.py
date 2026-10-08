from random import randint
tala = (randint (1, 11))
gisk = int(input("Giskaðu á tölu frá 0 - 10 "))
if gisk == tala:
    print ("Þú giskaðir rétt, talan var:", tala)
elif gisk < tala:
    print ("Þú giskaðir á of lága tölu, talan var:", tala)
elif gisk > tala:
    print ("Þú giskaðir á of háa tölu, talan var:", tala)