from random import randint
x = True
while x:
    for i in range(1,14):
        tala = randint (1,3)
        if tala == 1:
            print ("Leikur", i, "=> 1 ")
        elif tala == 2:
            print ("Leikur", i, "=> 2 ")
        elif tala == 3:
            print ("Leikur", i, "=> X ")

    aftur = str(input("Viltu gera aftur? (j/n) "))
    if aftur == ("n") or aftur == ("N"):
        x = False
        print ("Forritið er búið")
    else:
        print ("-----------------------------------------")