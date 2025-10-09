# make a python program which promts user to insert two integers and then prints the sum of those two integers
# use these integers together with the while loop structure to create behaviour like in the exple program run below
# note! the autugrading tool will test the correct structure has been applied

print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

i = start
while i <= stop:
    print(i, end=" ")
    i += 1

print("\n\nProgram ending.")
