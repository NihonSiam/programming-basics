ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def readConfig(PFilename: str) -> tuple[list[str], str]:
    rotors = ["", "", ""]
    reflector = ""
    with open(PFilename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row.startswith("Rotor1:"):
                rotors[0] = row.split(":", 1)[1]
            elif row.startswith("Rotor2:"):
                rotors[1] = row.split(":", 1)[1]
            elif row.startswith("Rotor3:"):
                rotors[2] = row.split(":", 1)[1]
            elif row.startswith("Reflector:"):
                reflector = row.split(":", 1)[1]
    return rotors, reflector

def stepPositions(PPositions: list[int]) -> None:
    PPositions[0] = (PPositions[0] + 1) % 26
    if PPositions[0] == 0:
        PPositions[1] = (PPositions[1] + 1) % 26
        if PPositions[1] == 0:
            PPositions[2] = (PPositions[2] + 1) % 26
    return None

def forwardRotor(PIndex: int, PRotor: str, PPos: int) -> int:
    shifted = (PIndex + PPos) % 26
    wired_char = PRotor[shifted]
    out_index = (ord(wired_char) - 65 - PPos) % 26
    return out_index

def reverseRotor(PIndex: int, PRotor: str, PPos: int) -> int:
    shifted = (PIndex + PPos) % 26
    letter = chr(shifted + 65)
    wired_index = PRotor.find(letter)
    out_index = (wired_index - PPos) % 26
    return out_index

def reflect(PIndex: int, PReflector: str) -> int:
    return ord(PReflector[PIndex]) - 65

def scrambleChar(PChar: str, PRotors: list[str], PPositions: list[int], PReflector: str) -> str:
    if PChar not in ALPHABET:
        return PChar
    stepPositions(PPositions)
    idx = ord(PChar) - 65
    idx = forwardRotor(idx, PRotors[0], PPositions[0])
    idx = forwardRotor(idx, PRotors[1], PPositions[1])
    idx = forwardRotor(idx, PRotors[2], PPositions[2])
    idx = reflect(idx, PReflector)
    idx = reverseRotor(idx, PRotors[2], PPositions[2])
    idx = reverseRotor(idx, PRotors[1], PPositions[1])
    idx = reverseRotor(idx, PRotors[0], PPositions[0])
    return chr(idx + 65)

def main():
    filename = input("Insert config(filename): ")
    plugs = input("Insert plugs (y/n)?: ")
    if plugs.lower() == "n":
        print("No extra plugs inserted.")
    else:
        print("Plugboard not implemented.")
    rotors, reflector = readConfig(filename)
    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print()
            print("Enigma closing.")
            return None
        positions = [0, 0, 0]
        converted = ""
        for ch in row:
            out = scrambleChar(ch, rotors, positions, reflector)
            converted += out
            print('Character "' + ch + '" illuminated as "' + out + '"')
        print('Converted row - "' + converted + '".\n')

main()
