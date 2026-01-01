def askDimension(PPrompt: str) -> float:
    feed = float(input("Insert " + PPrompt + ": "))
    return feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area

def main():
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")
    area = calcRectangleArea(width, height)
    print()
    print("Area is " + str(area) + "²")
    print("Program ending.")
    return None

main()
