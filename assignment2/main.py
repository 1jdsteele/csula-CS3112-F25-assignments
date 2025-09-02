import random
from module import generate_rand_array, selection_sort

print("hello cruel world")


rand_arr1 = generate_rand_array()
rand_arr2 = generate_rand_array()


print("array 1:", rand_arr1)
print("array 2:", rand_arr2)


rand_arr1 = selection_sort(rand_arr1)
print("array 1 after selection sort:", rand_arr1)


# now use insertion sort to sort second array
for i in range(len(rand_arr2)):
    # we have a window that is sorted from 0 to i - 1 and we are inserting the i - 1 position
    for j in range(i):
        if rand_arr2[i] < rand_arr2[j]:
            temp = rand_arr2[i]
            for k in range(i, j, -1):
                rand_arr2[k] = rand_arr2[k - 1]
                # print("if statement k looping, arr 2 rn: ", rand_arr2)
            rand_arr2[j] = temp
            # print("if statement hit done. array 2 rn: ", rand_arr2)
    # next element: insert into correct spot of sorted section
    # continue growing sorted section and inserting in correct place

print("array 2 after insertion sort:", rand_arr2)
