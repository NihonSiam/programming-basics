########################################################
# Task A9_T2
# Developer Nihon Siam
# Date 2026-12-01
########################################################
import sys

def main() -> None:
    print("Program starting.")
    code = int(input("Insert exit code(0-255): "))
    print("Clean exit")
    sys.exit(code)

main()
