
TEMP_MIN = -273.15
TEMP_MAX = 10000.0

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(feed))
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(celsius))
    return celsius

def main() -> None:
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print("You inserted {} °C".format(celsius))
    except Exception as e:
        print(e)
    print("Program ending.")
    return None

main()
