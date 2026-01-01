########################################################
# Task A10_T1
# Developer nihon Siam
# Date 2026-12-05
########################################################
def readValues(PFilename: str) -> list[str]:
    values = []
    with open(PFilename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            values.append(row)
    return values

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")
    values.clear()
    print("Program ending.")
    return None

main()
