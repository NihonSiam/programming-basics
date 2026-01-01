SEPARATOR = ";"

def readValues(filename):
    f = open(filename, "r")
    values = ""
    lines = f.readlines()
    for i in range(len(lines)):
        n = lines[i].strip()
        if i < len(lines) - 1:
            values += n + SEPARATOR
        else:
            values += n
    f.close()
    return values

def analyseValues(values):
    parts = values.split(SEPARATOR)
    nums = [int(x) for x in parts]
    c = len(nums)
    s = sum(nums)
    g = max(nums)
    a = s / c
    result = "Count;Sum;Greatest;Average\n"
    result += str(c) + SEPARATOR + str(s) + SEPARATOR + str(g) + SEPARATOR + format(a, ".2f") + "\n"
    return result