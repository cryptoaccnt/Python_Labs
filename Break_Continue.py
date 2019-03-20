statement = "The quick brown fox jumped over the lazy dogs."
for letter in statement:
    print("Current Letter", letter)
    if letter == "p":
        break

for letter in statement:
    if letter == "q":
        continue
    print("Current letter", letter)