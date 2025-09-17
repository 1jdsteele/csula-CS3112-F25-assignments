from module import *



print(
    "Welcome to Jake's assignement number 3 for analysis of algorithms. In this assignement we will sort randomly generated arrays by via merge sort and then use binary search to find a target. The arrays can have a length 3-10 and can include any number 0-100. Then we will take solve exponential problems via divide and conquer.\n"
)

user_option = 1

while user_option:

    user_option = int(
        input(
            "Input 1 to see see binary search after merge sort.\nInput 2 to see taking powers by divide and conquer."#\nInput 3 to see binary search after merge sort stepwise.\nInput 4 to see  taking powers by divide and conquer stepwise.
            "\nInput 0 to quit the program.\n"
        )
    )

    print_case(user_option)

print("Thank you for your time. Goodbye world")


# # problem 1

# arr = create_rand_arr()
# print(arr)

# merge_sort(arr)
# print(arr)

# #problem 2

# print(binary_search(arr[1], arr)) # expect 1

# print(binary_search(-3, arr)) # expect -1



# # problem 3

# print(take_exponenet(2, 2)) # 4
# print(take_exponenet(2, 3)) # 8
# print(take_exponenet(2, 4)) # 16
# print(take_exponenet(2, 5)) # 32
# print(take_exponenet(2, 6)) # 64