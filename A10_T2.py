########################################################
# Task A10_T2
# Developer First_name Last_name
# Date 2026-12-05
########################################################
import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            for line in f:
                row = line.strip()
                if row == "":
                    continue
                PValues.append(int(row))
    except:
        print("Error! Couldn't read file '{}'.".format(PFilename))
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    s = 0
    for v in PValues:
        s += v
    return s

def productOfValues(PValues: list[int]) -> int:
    if len(PValues) == 0:
        return 0
    p = 1
    for v in PValues:
        p *= v
    return p

def main() -> None:
    values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, values)
    print("# --- Sum of numbers --- #")
    print(sumOfValues(values))
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(productOfValues(values))
    print("# --- Product of numbers --- #")
    values.clear()
    print("Program ending.")
    return None

main()
