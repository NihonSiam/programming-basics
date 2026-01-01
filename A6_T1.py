def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print('#### START "' + filename + '" ####')
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
    print()
    print('#### END "' + filename + '" ####')
    print("Program ending.")
    return None

main()
