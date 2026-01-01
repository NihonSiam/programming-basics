def main():
    print("Program starting.")
    raw = input("Insert comma separated integers: ")
    parts = raw.split(",")
    values = []
    for p in parts:
        s = p.strip()
        if s == "":
            print('Invalid value "" detected.')
        else:
            try:
                values.append(int(s))
            except:
                print('Invalid value "' + s + '" detected.')
    if len(values) == 0:
        print("There are no values to analyze.")
    else:
        total = 0
        for v in values:
            total += v
        print("There are " + str(len(values)) + " integers in the list.")
        if total % 2 == 0:
            print("Sum of the integers is " + str(total) + " and it's even")
        else:
            print("Sum of the integers is " + str(total) + " and it's odd")
    print("Program ending.")
    return None

main()
