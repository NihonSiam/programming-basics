def readfile();
file=open("data.txt","r")
while True:
    line=file.readline()
    if len(line)==0:
        break
    print(line,end="")
    file.close()

    def main(): -> None:
        print("program starting")
        print("this program can read files")
        Filename =input("insert the file name:")
        FileContent =readfile()

        if __name__ == "__main__":
            main()