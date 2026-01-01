def readValues(PFilename: str, PValues: list[float]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as f:
        for line in f:
            if line == "\n":
                continue
            PValues.append(float(line.strip()))
    return None

def calcSum(PValues: list[float]) -> float:
    total = 0.0
    for v in PValues:
        total += v
    return total

def calcAverage(PValues: list[float]) -> float:
    if len(PValues) == 0:
        return 0.0
    return calcSum(PValues) / len(PValues)

def main() -> None:
    print("Program starting.")
    values = []
    while True:
        print("Options:")
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            filename = input("Insert filename: ")
            readValues(filename, values)
            print()
        elif choice == "2":
            print("Amount of values " + str(len(values)))
            print()
        elif choice == "3":
            s = round(calcSum(values), 1)
            print("Sum of values " + str(s))
            print()
        elif choice == "4":
            a = round(calcAverage(values), 1)
            print("Average of values " + str(a))
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print()
    values.clear()
    print("Program ending.")
    return None

main()
