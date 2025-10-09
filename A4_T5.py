print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

# Check rules
error = False

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    error = True

if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    error = True

# If there were errors, skip the loops
if not error:
    print("\nFirst loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        print(i, end=" " if i < inspect - 1 else "")
    print()  # move to next line

    print("Second loop - inspection with continue:")
    first = True
    for i in range(start, stop):
        if i == inspect:
            continue
        if not first:
            print(" ", end="")
        print(i, end="")
        first = False
    print()

print("\nProgram ending.")
