from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            PTimestamps.append(datetime.strptime(row, "%Y-%m-%d %H:%M"))
    return None

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    c = 0
    for t in PTimestamps:
        if t.year == PYear:
            c += 1
    return c

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    if PMonth not in MONTHS:
        return 0
    m = MONTHS.index(PMonth) + 1
    c = 0
    for t in PTimestamps:
        if t.month == m:
            c += 1
    return c

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    if PWeekday not in WEEKDAYS:
        return 0
    w = WEEKDAYS.index(PWeekday)
    c = 0
    for t in PTimestamps:
        if t.weekday() == w:
            c += 1
    return c
