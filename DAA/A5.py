from random import *


def partitionNormal(arr, low, high):
    pivot = arr[high]

    i = low

    for j in range(low, high):
        if (arr[j] < pivot):
            (arr[i], arr[j]) = (arr[j], arr[i])
            i = i + 1
    (arr[i], arr[high]) = (arr[high], arr[i])
    return i


def quickSortNormal(arr, low, high):
    if (low < high):
        p = partitionNormal(arr, low, high)
        quickSortNormal(arr, low, p-1)
        quickSortNormal(arr, p+1, high)


def partitionRandom(arr, low, high):
    pivot = randrange(low, high)
    (arr[pivot], arr[low]) = (arr[low], arr[pivot])
    return partitionNormal(arr, low, high)


def quickSortRandom(arr, low, high):
    if low < high:
        p = partitionRandom(arr, low, high)
        quickSortRandom(arr, low, p-1)
        quickSortRandom(arr, p+1, high)


while(True):
    print("1. Deterministic")
    print("2. Randomized")
    print("0. Exit")
    ch = input("Enter the choice: ")
    if(ch == "0"):
        break
    elif ch == "1":
        num = int(input("Enter number of elements : "))
        arr = []
        for i in range(0, num):
            temp = int(input("Enter element : "))
            arr.append(temp)
        quickSortNormal(arr, 0, len(arr) - 1)
        print("Sorted array : ", arr)
    elif ch == "2":
        num = int(input("Enter number of elements : "))
        arr = []
        for i in range(0, num):
            temp = int(input("Enter element : "))
            arr.append(temp)
        quickSortRandom(arr, 0, len(arr) - 1)
        print("Sorted array : ", arr)
