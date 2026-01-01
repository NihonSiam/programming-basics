########################################################
# Task A10_T7
# Developer Nihon Siam
# Date 2026-12-05
########################################################
import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        if PMineField[rr][cc] == 9:
                            count += 1
            PMineField[r][c] = count
    return None

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    PMineField.clear()
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
    if PRows > 0 and PCols > 0 and PMines > 0:
        max_mines = PRows * PCols
        if PMines > max_mines:
            PMines = max_mines
        layMines(PMineField, PMines)
        calculateNearbys(PMineField)
    return None

def showBoard(PMineField: list[list[int]]) -> None:
    for row in PMineField:
        print(row)
    return None

def saveBoard(PFilename: str, PMineField: list[list[int]]) -> None:
    with open(PFilename, "w", encoding="utf-8") as f:
        for r in range(len(PMineField)):
            line = ""
            for c in range(len(PMineField[r])):
                line += str(PMineField[r][c])
                if c != len(PMineField[r]) - 1:
                    line += ","
            f.write(line + "\n")
    return None

def main() -> None:
    print("Program starting.")
    minefield: list[list[int]] = []
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(minefield, rows, cols, mines)
            print()
        elif choice == "2":
            showBoard(minefield)
            print()
        elif choice == "3":
            filename = input("Insert filename: ")
            saveBoard(filename, minefield)
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print()
    minefield.clear()
    print("Program ending.")
    return None

main()
