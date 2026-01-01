LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def writeFile(filename, content):
    f = open(filename, "w", encoding="UTF-8")
    f.write(content)
    f.close()

def askRows():
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    return "\n".join(rows)

def shiftCharacter(c, alphabets, shift=13):
    if c in alphabets:
        i = alphabets.index(c)
        i = (i + shift) % len(alphabets)
        return alphabets[i]
    return c

def rot13(content):
    result = ""
    for c in content:
        if c in LOWER_ALPHABETS:
            result += shiftCharacter(c, LOWER_ALPHABETS)
        elif c in UPPER_ALPHABETS:
            result += shiftCharacter(c, UPPER_ALPHABETS)
        else:
            result += c
    return result

def main():
    print("Program starting.")
    print()
    print("Collecting plain text rows for ciphering.")
    rows = askRows()
    print()
    print("#### Ciphered text ####")
    ciphered = rot13(rows)
    print(ciphered)
    print()
    print("#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
        print("Program ending.")
        return
    writeFile(filename, ciphered)
    print("Ciphered text saved!")
    print("Program ending.")

if __name__ == "__main__":
    main()