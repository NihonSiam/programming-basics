from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                # TODO: Prompt for square parameters and call drawSquare
                # Example: left = askValue1("Left edge position")
                pass
            case 2:
                print('Insert circle')
                # TODO: Prompt for circle parameters and call drawCircle
                pass
            case 3:
                # TODO: Prompt for filename and confirm before saving
                pass
            case 0:
                print("Exiting program.\n")
                break
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()