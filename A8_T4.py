import A8_T4_lib

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    A8_T4_lib.readTimestamps(filename, timestamps)
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            year = int(input("Insert year: "))
            amount = A8_T4_lib.calculateYears(year, timestamps)
            print("Amount of timestamps during year '" + str(year) + "' is " + str(amount))
            print()
        elif choice == "2":
            month = input("Insert month: ")
            amount = A8_T4_lib.calculateMonths(month, timestamps)
            print("Amount of timestamps during month '" + month + "' is " + str(amount))
            print()
        elif choice == "3":
            weekday = input("Insert weekday: ")
            amount = A8_T4_lib.calculateWeekdays(weekday, timestamps)
            print("Amount of timestamps during weekday '" + weekday + "' is " + str(amount))
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print()
    timestamps.clear()
    print("Program ending.")
    return None

main()
