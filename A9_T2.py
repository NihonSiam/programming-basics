
import sys

def main() -> None:
    print("Program starting.")
    code = int(input("Insert exit code(0-255): "))
    print("Clean exit")
    sys.exit(code)

main()
