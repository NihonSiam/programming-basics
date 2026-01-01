########################################################
# Task A10_T5
# Developer Nihon Siam
# Date 2026-12-05
########################################################
def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    n = int(input("Insert factorial: "))
    result = recursiveFactorial(n)
    print("Factorial " + str(n) + "!")
    print(str(n) + " = " + str(result))
    print("Program ending.")
    return None

main()
