print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

main_choice = input("Your choice: ")

if main_choice == "1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "1":
        meters = float(input("Insert meters: "))
        km = meters / 1000
        print(f"{meters:.1f} m is {km:.1f} km")
    elif choice == "2":
        km = float(input("Insert kilometers: "))
        meters = km * 1000
        print(f"{km:.1f} km is {meters:.1f} m")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif main_choice == "2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice = input("Your choice: ")
    if choice == "1":
        grams = float(input("Insert grams: "))
        pounds = grams / 453.592
        print(f"{grams:.1f} g is {pounds:.1f} lbs")
    elif choice == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.592
        print(f"{pounds:.1f} lbs is {grams:.1f} g")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif main_choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
