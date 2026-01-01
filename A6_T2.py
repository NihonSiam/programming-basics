def main():
    print("Program starting.")
    first = input("Insert first name: ")
    last = input("Insert last name: ")
    filename = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(first + "\n")
        f.write(last + "\n")
        f.write("\n")
    print("Program ending.")
    return None

main()
