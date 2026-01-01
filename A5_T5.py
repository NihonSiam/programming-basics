def main():
    print("Program starting.")
    word = ""
    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            word = input("Insert word: ")
            print()
        elif choice == "2":
            print('Current word - "' + word + '"')
            print()
        elif choice == "3":
            print('Word reversed - "' + word[::-1] + '"')
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown option.")
            print()
    print("Program ending.")
    return None

main()
