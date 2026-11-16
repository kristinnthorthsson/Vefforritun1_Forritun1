from pathlib import Path

print ("Liður 1")
text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    if len(word) > 20:
        print (word)


print ("--------------------------------------------------")

print ("Liður 2")
leita = str(input("Hverju viltu leita að: "))
text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    if leita in word:
        print (word)

print ("--------------------------------------------------")

print ("Liður 3")
leita2 = str(input("Af hvaða staf vilt þú leita? "))
samtals = 0
text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    for stafur in word:
        if stafur == leita2:
            samtals +=1
print ("Stafurinn", leita2, "fannst", samtals,"sinnum")  

print ("--------------------------------------------------")