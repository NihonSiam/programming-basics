def main():
    print("Program starting.")
    print("This program can copy a file.")
    src = input("Insert source filename: ")
    dst = input("Insert destination filename: ")
    print("Reading file '" + src + "' content.")
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    print("File content ready in memory.")
    print("Writing content into file '" + dst + "'.")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)
    print("Copying operation complete.")
    print("Program ending.")
    return None

main()
