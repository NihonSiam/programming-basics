from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: int = 0
    consumption: float = 0.0
    price: float = 0.0

@dataclass
class DAY_USAGE:
    weekday: str = ""
    usage: float = 0.0
    cost: float = 0.0

def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            if line == "\n":
                continue
            row = line.rstrip("\n")
            cols = row.split(DELIMITER)
            ts = TIMESTAMP()
            ts.weekday = cols[0]
            ts.hour = int(cols[1])
            ts.consumption = float(cols[2])
            ts.price = float(cols[3])
            PTimestamps.append(ts)
            cols.clear()
    return None

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PHelper: list[DAY_USAGE], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PHelper.clear()
    PResults.clear()
    for wd in WEEKDAYS:
        PHelper.append(DAY_USAGE(wd, 0.0, 0.0))
    for ts in PTimestamps:
        for i in range(len(WEEKDAYS)):
            if ts.weekday == WEEKDAYS[i]:
                PHelper[i].usage += ts.consumption
                PHelper[i].cost += ts.consumption * ts.price
                break
    for d in PHelper:
        PResults.append(" - {} usage {:.2f} kWh, cost {:.2f} €".format(d.weekday, d.usage, d.cost))
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for r in PResults:
        print(r)
    print("### Electricity consumption summary ###")
    return None

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    helper = []
    results = []
    readFile(filename, timestamps)
    analyseTimestamps(timestamps, helper, results)
    displayResults(results)
    timestamps.clear()
    helper.clear()
    results.clear()
    print("Program ending.")
    return None

main()
