########################################################
# Task A9_T3
# Developer Nihon Siam
# Date 2026-12-01
########################################################
import sys

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("## " + filename + " ##")
            for line in f:
                print(line, end="")
            print("## " + filename + " ##")
    except FileNotFoundError:
        print("Error! File '" + filename + "' doesn't exist.")
        sys.exit(1)
    print("Program ending.")
    return None

main()
