list=[]

def valmynd():    
    print(" ---- ")
    print("1. Bæta vöru á innkaupalistann")
    print("2. Eyða vöru af innkaupalista")
    print("3. Prenta innkaupalista")
    print("4. Hætta")
    print(" ---- ")

def add():
    s = True
    while s:
        print ()
        svar = str(input("Viltu bæta við vörru? (j/n): "))
        if svar == ("n") or svar == ("N"):
            s = False
        elif svar == ("j") or svar == ("J"):
            print ()
            vara = str(input("Hvað viltu bæta við? "))
            list.append(vara)

def remove():
    print ()
    s = True
    while s:
        svar = False
        delete = str(input("Hvaða vöru viltu eyða af listanum?: "))
        for i in range (0, len(list) -1):
            if list[i] == delete:
                del list[i]
                svar = True
            if svar == False:
                print ()
                print("Varan fannst ekki!")
        svar = str(input("Viltu eyða annari vöru? (j/n): "))
        if svar == ("n") or svar == ("N"):
            s = False

def prenta():
    print ()
    print ("Þetta er innkaupalistinn:")
    for item in list:
        print (item)

x = True
while x:
    valmynd()
    val = int(input("Veldu tölu: "))
    if val == (1):
        add()
    elif val == (2):
        remove()
    elif val == (3):
        prenta()
    elif val == (4):
        x = False
    else:
        print ("Þú valdir ekki rétt")
print ()
print ("Forritið er búið")
print (" ---- Búið ---- ")
