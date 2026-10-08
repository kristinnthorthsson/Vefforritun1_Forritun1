from random import randint
x = True
while x:
    tala = randint(1, 5)
    if tala == (1):
        print ("Það verður rok og rigning á morgun.")
    elif tala == (2):
        print ("Það verður þurrt en kalt á morgun.")
    elif tala == (3):
        print ("Það verður þurrt en kalt á morgun.")
    elif tala == (4):
        print ("Það verður logn með smá skúrum á morgun.")
    aftur = str(input("Viltu nýja veðurspá? (j/n): "))
    if aftur == ("n") or aftur == ("N"):
        print ("Forritið búið")
        print ("-----------------------------------")
        x = False
    else:
        print ("-----------------------------------")