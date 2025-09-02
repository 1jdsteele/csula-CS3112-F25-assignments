import random


def generate_rand_array() -> list[int]:
    arr = []

    for i in range(0, random.randint(2, 10)):
        arr.append(random.randint(2, 100))

    return arr


# notes: this is unstable - as in it reorders same value elements
# to fix: romove the min and insert it at i, shifting all else, like in insertion sort
def selection_sort(arr: list[int]) -> list[int]:  # O(n^2)
    for i in range(len(arr)):
        curr_min = arr[i]
        curr_min_index = i
        for j in range(i, len(arr)):
            if arr[j] < curr_min:
                curr_min = arr[j]
                curr_min_index = j
        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                for k in range(i, j, -1):
                    arr[k] = arr[k - 1]
                arr[j] = temp
                break
    return arr
