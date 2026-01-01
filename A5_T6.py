def showOptions():
    """Displays the available options."""
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    """Prompts user for a choice and returns an integer.
       Prints 'Unknown option!' for non-numeric input."""
    choice = input("Your choice: ")
    if not choice.isnumeric():
        print("Unknown option!")
        return -1  
    return int(choice)


def main():
    """Main program logic and menu cycle."""
    print("Program starting.")
    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice == -1:
         
            print()
        else:
        
            print("Unknown option!\n")

    print("\nProgram ending.")


main()