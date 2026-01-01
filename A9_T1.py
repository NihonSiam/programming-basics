########################################################
# Task A9_T1
# Developer Nihon Siam
# Date 2026-12-01
########################################################
def main() -> None:
    print("Program starting.")
    print()
    total = 0.0
    while True:
        feed = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(feed)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(feed))
            continue
        if value == 0.0:
            break
        total += value
    print()
    print("Final sum is {:.2f}".format(total))
    print("Program ending.")
    return None

main()
