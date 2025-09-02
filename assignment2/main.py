import random
from module import generate_rand_array, selection_sort, insertion_sort

# introduction statement
print(
    "Welcome to Jake's assignement number 2 for analysis of algorithms. In this assignement we will sort randomly aorted arrays by two different methods. The arrays can have a length 2-10 and can include any number 0-100.\n"
)

user_option = 1

while user_option:

    user_option = int(
        input(
            "Input 1 to see selection sorting.\nInput 2 to see insertion sorting.\nInput 0 to quit the program.\n"
        )
    )

    match user_option:
        case 1:
            rand_arr1 = generate_rand_array()
            print("random array:", rand_arr1)
            rand_arr1 = selection_sort(rand_arr1)
            print("random array after selection sort:", rand_arr1, "\n")
        case 2:
            rand_arr2 = generate_rand_array()
            print("array 2:", rand_arr2)
            rand_arr2 = insertion_sort(rand_arr2)
            print("array 2 after insertion sort:", rand_arr2, "\n")

print("Thank you for your time. Goodbye world")
