import A8_T2_lib

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            print()
            break
        if choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            r = A8_T2_lib.add(a, b)
            print(str(a) + " + " + str(b) + " = " + str(r))
            print()
        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            r = A8_T2_lib.subtract(a, b)
            print(str(a) + " - " + str(b) + " = " + str(r))
            print()
        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            r = A8_T2_lib.multiply(a, b)
            print(str(a) + " * " + str(b) + " = " + str(r))
            print()
        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            r = A8_T2_lib.divide(a, b)
            print(str(a) + " / " + str(b) + " = " + str(r))
            print()
        else:
            print()
    print("Program ending.")
    return None

main()
