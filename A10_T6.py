########################################################
# Task A10_T6
# Developer Nihon Siam
# Date 2026-12-05
########################################################
import copy
import time
from typing import Callable

def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            PValues.append(int(row))
    return None

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
                swapped = True
        if not swapped:
            break
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = []
    mid = []
    right = []
    for v in PNums:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            mid.append(v)
    return quickSort(left) + mid + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    start = time.perf_counter_ns()
    if PSortingAlgorithm is sorted:
        PSortingAlgorithm(PArr)
    else:
        PSortingAlgorithm(PArr)
    end = time.perf_counter_ns()
    return end - start

def main() -> None:
    print("Program starting.")
    values: list[int] = []
    results: list[str] = []
    dataset = ""
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            dataset = input("Insert dataset filename: ")
            readValues(dataset, values)
            print()
        elif choice == "2":
            if dataset == "" or len(values) == 0:
                print()
                continue
            b1 = measureSortingTime(sorted, copy.deepcopy(values))
            b2 = measureSortingTime(bubbleSort, copy.deepcopy(values))
            b3 = measureSortingTime(quickSort, copy.deepcopy(values))
            print("Measured speeds for dataset '" + dataset + "':")
            print(" - Built-in sorted " + str(b1) + " ns")
            print(" - Buble sort " + str(b2) + " ns")
            print(" - Quick sort " + str(b3) + " ns")
            print()
            results.clear()
            results.append("Measured speeds for dataset '" + dataset + "':")
            results.append(" - Built-in sorted " + str(b1) + " ns")
            results.append(" - Buble sort " + str(b2) + " ns")
            results.append(" - Quick sort " + str(b3) + " ns")
        elif choice == "3":
            filename = input("Insert results filename: ")
            with open(filename, "w", encoding="utf-8") as f:
                for r in results:
                    f.write(r + "\n")
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print()
    values.clear()
    results.clear()
    print("Program ending.")
    return None

main()
