from pathlib import Path

text = open(Path(__file__).with_name("words.txt"))
for line in text:
    word = line.strip()
    if len(word) > 20:
        print (word)