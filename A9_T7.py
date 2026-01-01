########################################################
# Task A9_T7
# Developer Nihon Siam
# Date 2026-12-01
########################################################

import sys
import os

def showHelp() -> None:
    print('Synopsis: python {} <src_file> <dst_file>'.format(sys.argv[0]))
    return None

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True
    if os.path.exists(PDstFile):
        ans = input('Destination file "{}" exists. Overwrite (y/n)?: '.format(PDstFile))
        if ans.lower() != "y":
            proceed = False
    if proceed:
        try:
            with open(PSrcFile, "r", encoding="utf-8") as f:
                data = f.read()
            with open(PDstFile, "w", encoding="utf-8") as f:
                f.write(data)
        except:
            print('Error! Copying file "{}" to "{}" failed.'.format(PSrcFile, PDstFile))
            sys.exit(-1)
    return None

def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        return None
    src = sys.argv[1]
    dst = sys.argv[2]
    print('Source file "{}"'.format(src))
    print('Destination file "{}"'.format(dst))
    print('Copying file "{}" to "{}".'.format(src, dst))
    copyFile(src, dst)
    print("Program ending.")
    return None

main()
