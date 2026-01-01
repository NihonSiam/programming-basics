WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    with open(PFilename, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            if line == "\n":
                continue
            PRows.append(line.rstrip("\n"))
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    counts = [0, 0, 0, 0, 0, 0, 0]
    for row in PRows:
        for j in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[j]):
                counts[j] += 1
                break
    for i in range(len(WEEKDAYS)):
        PResults.append(" - " + WEEKDAYS[i] + " " + str(counts[i]) + " stamps")
    counts.clear()
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for r in PResults:
        print(r)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    rows = []
    results = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

main()
