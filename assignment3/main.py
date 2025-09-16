from module import *

# problem 1

arr = create_rand_arr()
print(arr)

merge_sort(arr)
print(arr)

#problem 2

print(binary_search(arr[1], arr)) # expect 1

print(binary_search(-3, arr)) # expect -1



# problem 3

print(take_exponenet(2, 2)) # 4
print(take_exponenet(2, 3)) # 8
print(take_exponenet(2, 4)) # 16
print(take_exponenet(2, 5)) # 32
print(take_exponenet(2, 6)) # 64