import random


def generate_rand_array() -> list[int]:
    arr = []
    rand_size = random.randint(2, 10)

    for i in range(0, rand_size):
        arr.append(random.randint(2, 100))

    return arr


def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        curr_min = arr[i]
        curr_min_index = i
        for j in range(i, len(arr)):
            if arr[j] < curr_min:
                curr_min = arr[j]
                curr_min_index = j
        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]
    return arr
