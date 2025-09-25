print("Program starting.")

Temp = float(input("Insert fahrenheits: "))
celsius = (Temp - 32) / 1.8
celsius = round(celsius, 1)

print(f"{Temp}°F is {celsius}°C")

print("Program ending.")