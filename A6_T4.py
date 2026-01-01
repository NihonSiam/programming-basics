def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    print('Reading names from "' + filename + '".')
    names = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name != "":
                names.append(name)
    print("Analysing names...")
    count = len(names)
    shortest = min(len(n) for n in names) if count > 0 else 0
    longest = max(len(n) for n in names) if count > 0 else 0
    avg = (sum(len(n) for n in names) / count) if count > 0 else 0.0
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count - " + str(count))
    print("Shortest name - " + str(shortest) + " chars")
    print("Longest name - " + str(longest) + " chars")
    print("Average name - {:.2f} chars".format(avg))
    print("#### REPORT END ####")
    print("Program ending.")
    return None

main()
