def main():
    print("Program starting.")
    print("Collect positive integers.")
    values = []
    while True:
        n = int(input("Insert positive integer(negative stops): "))
        if n < 0:
            break
        if n > 0:
            values.append(n)
    print("Stopped collecting positive integers.")
    if len(values) == 0:
        print("No integers to display.")
    else:
        print("Displaying " + str(len(values)) + " integers:")
        for i in range(len(values)):
            print("- Index " + str(i) + " => Ordinal " + str(i + 1) + " => Integer " + str(values[i]))
    print("Program ending.")
    return None

main()
