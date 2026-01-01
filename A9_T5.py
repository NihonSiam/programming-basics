def askIntByte(PPrompt: str) -> int:
    # Ask for input
    Feed = input(PPrompt)

    # TODO: Use try-except to:
    #   - Convert input to float and int
    #   - Raise an exception if input is not numeric
    #   - Raise an exception if input is not an integer
    #   - Raise an exception if input is not in the range 0–255

    # If all checks pass, return the integer value
    pass

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    # TODO: Return a hex string in the format "#rrggbb"
    # Use string formatting: "{:02x}"
    pass

def main():
    print("Program starting.")

    # TODO: Use try-except here to:
    #   - Call askIntByte for red, green, and blue
    #   - Call createHex to get the hex color
    #   - Print RGB values, hex value, and binary (8-bit) values
    #   - If any exception occurs, print the error and a message like:
    #     "Couldn't perform the designed task due to the invalid input values."

    print("Program ending.")

if __name__ == "__main__":
    main()