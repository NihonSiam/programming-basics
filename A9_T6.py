def showOptions() -> None:
    # TODO: Print the menu options
    pass

def askChoice() -> int:
    # TODO: Ask user for a menu choice and return it as an integer
    # Students should use try-except to handle invalid input
    return -1

def saveLines(PLines: list[str]) -> None:
    # TODO: Ask for filename and save lines to the file
    # Students should use try-except to handle file errors
    pass

def insertLine(PLines: list[str]) -> None:
    # TODO: Ask user to input a line and add it to PLines
    pass

def onInterrupt(PLines: list[str]) -> None:
    # TODO: Handle KeyboardInterrupt when there are unsaved lines
    # Students should use try-except to handle input errors
    pass

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    while Choice != 0:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            insertLine(Lines)
        elif Choice == 2:
            saveLines(Lines)
        elif Choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
        print("")
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()