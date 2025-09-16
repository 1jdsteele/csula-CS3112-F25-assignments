import random
# ++++++++++++ #problem 1: merge sort ++++++++++++

def create_rand_arr() -> list[int]:
    return_arr = []
    size = random.randint(3, 10)
    for i in range(size):
        return_arr.append(random.randint(0, 100))
    return return_arr


def merge_sort(arr: list[int]):
    merge_sort_helper(arr, 0, len(arr) - 1)


def merge_sort_helper(arr: list[int], start: int, end: int):

    if start >= end: return # basey casey
    half = (start + end) // 2
    merge_sort_helper(arr, start, half)
    merge_sort_helper(arr, half + 1, end)
    merge(arr, start, end)


def merge(arr: list[int], start: int, end: int):
    if start >= end: return # basey casey

    ordered_arr = []
    midpoint =  (start + end) // 2 
    j = start
    k = midpoint + 1

    for i in range(start, end + 1):
        if j > midpoint:                     
            ordered_arr.append(arr[k])
            k += 1
        elif k > end:                    
            ordered_arr.append(arr[j])
            j += 1
        #starting here we know we do not overindex
        elif arr[j] <= arr[k]:          
            ordered_arr.append(arr[j])
            j += 1
        else:
            ordered_arr.append(arr[k])
            k += 1

    arr[start:end + 1] = ordered_arr








# problem 2: binary search

def binary_search(target: int, arr: list[int]) -> int:
    
    return binary_search_helper(target, arr, 0, len(arr) - 1)

def binary_search_helper(target: int, arr: list[int], start: int, end: int) -> int:
    if start > end: return -1

    midpoint = (start + end) // 2

    #found it
    if arr[midpoint] == target:
        return midpoint
    #less than
    elif arr[midpoint] < target:
        return binary_search_helper(target, arr, midpoint + 1, end)
    #more than
    elif arr[midpoint] > target:
        return binary_search_helper(target, arr, start, midpoint - 1)
    
    return -1
        


# problem 3 divide and conquer exponents
def take_exponenet(base: int, exponent: int) -> int:
    if exponent == 0: return 1
    if exponent == 1: return base
    # to make next parts more efficient, turn the half into avar and then multiply to itself
    if exponent % 2 == 1:
        return base * take_exponenet(base, int((exponent - 1) / 2)) * take_exponenet(base, int((exponent - 1) / 2))
    return take_exponenet(base, exponent // 2) * take_exponenet(base, exponent // 2)