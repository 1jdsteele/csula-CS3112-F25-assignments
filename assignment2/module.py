import random


# ++++++++++ SORTING SECTION ++++++++++
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


def selection_sort_show_steps(arr: list[int]) -> list[int]:  # O(n^2)
    print("Here are the selection sort steps:")
    for i in range(len(arr)):
        curr_min = arr[i]
        curr_min_index = i
        for j in range(i, len(arr)):
            if arr[j] < curr_min:
                curr_min = arr[j]
                curr_min_index = j
        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]
        print("selection sorting at index ", i, ". Here is the array now: ", arr)
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


def insertion_sort_show_steps(arr: list[int]) -> list[int]:
    print("Here are the insertion sort steps:")
    for i in range(len(arr)):
        print("starting index i: ", i)
        for j in range(i):
            print("checking index j: ", j)
            if arr[i] < arr[j]:
                temp = arr[i]
                for k in range(i, j, -1):
                    arr[k] = arr[k - 1]
                arr[j] = temp
                print("inserted at index ", j, ". Array is currently: ", arr)
                break

    return arr


# ++++++++++ UI SECTION ++++++++++


def print_case(user_choice: int):
    if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
        return
    arr = generate_rand_array()
    print("\nrandom array:", arr)
    match user_choice:
        case 1:
            arr = selection_sort(arr)
            print("random array after selection sort:", arr, "\n")
        case 2:
            arr = insertion_sort(arr)
            print("random array after insertion sort:", arr, "\n")
        case 3:
            arr = selection_sort_show_steps(arr)
            print("random array after selection sort:", arr, "\n")
        case 4:
            arr = insertion_sort_show_steps(arr)
            print("random array after insertion sort:", arr, "\n")
