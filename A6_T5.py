def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    count = 0
    total = 0
    greatest = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            value = int(line.strip())
            count += 1
            total += value
            if count == 1 or value > greatest:
                greatest = value
    avg = total / count if count > 0 else 0.0
    print("Count;Sum;Greatest;Average")
    print(str(count) + ";" + str(total) + ";" + str(greatest) + ";" + "{:.2f}".format(avg))
    print()
    print("#### Number analysis - END ####")
    print("Program ending.")
    return None

main()
