import random
from module import generate_rand_array, selection_sort, insertion_sort

# introduction statement
print(
    "Welcome to Jake's assignement number 2 for analysis of algorithms. In this assignement we will sort randomly aorted arrays by two different methods. The arrays can have a length 2-10 and can include any number 0-100.\n"
)

rand_arr1 = generate_rand_array()
print("array 1:", rand_arr1)
rand_arr1 = selection_sort(rand_arr1)
print("array 1 after selection sort:", rand_arr1, "\n")


rand_arr2 = generate_rand_array()
print("array 2:", rand_arr2)
rand_arr2 = insertion_sort(rand_arr2)
print("array 2 after insertion sort:", rand_arr2, "\n")
