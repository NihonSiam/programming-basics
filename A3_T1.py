print("Program starting.")

print("Insert two integers.")
a = int(input("Insert first integer: "))
b = int(input("Insert second integer: "))

print("Comparing inserted integers.")
if a == b:
    print("Integers are the same")
elif a > b:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

print("\nAdding integers together")
s = a + b
print(f"{a} + {b} = {s}")

print("\nChecking the parity of the sum...")
if s % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")
