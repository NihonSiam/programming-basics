from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: int = 0
    consumption: float = 0.0
    price: float = 0.0

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

def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in PTimestamps:
        total = ts.price * ts.consumption
        print(" - {} {:02d}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(ts.weekday, ts.hour, ts.price, ts.consumption, total))
    return None

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    readFile(filename, timestamps)
    displayTimestamps(timestamps)
    timestamps.clear()
    print("Program ending.")
    return None

main()
