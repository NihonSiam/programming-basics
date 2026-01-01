import time

def main() -> None:
    print("Program starting.")
    pause = 0.0
    while True:
        print("Options:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            pause = float(input("Insert pause duration (s): "))
            print()
        elif choice == "2":
            print("Pausing for " + str(pause) + " seconds.")
            time.sleep(pause)
            print("Unpaused.")
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print()
    print("Program ending.")
    return None

main()
