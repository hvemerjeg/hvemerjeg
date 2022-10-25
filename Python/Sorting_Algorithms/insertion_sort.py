#!/usr/bin/python3
#THIS IS AN IMPLEMENTATION OF AN EASY WELL-KNOWN SORTING ALGORITHM CALLED "INSERTION SORT"
#This algorithm is efficient with small set of numbers, and works almost the same as we normally sort a hand of playing cards

def insertionSort(arr: list):

    for indx in range(1, len(arr)):
        current = arr[indx]
        while indx > 0 and arr[indx - 1] > current:
            arr[indx] = arr[indx - 1]
            indx -= 1
        arr[indx] = current
    return arr

if __name__ == '__main__':
    #TESTS
    tests = {(3, 2, 1): [1, 2, 3], (9,): [9], (8, 1, 4, 2, 6): [1, 2, 4, 6, 8]}
    for test in tests:
        result = insertionSort(list(test))
        if tests[test] != result:
            print(f"\033[1;31;40m[+] Not passed:\033[0m Test: {list(test)}\tResult: {result}")
        else:
            print(f"\033[1;32;40m[+] Passed!:\033[0m Test: {list(test)}\tResult: {result}")
