from module import *
import math

chosen_n = int(input("Please choose the length of the list that we will permutate and study.\n"))

m = harmonic_sequence_total(chosen_n)

print(m)

# print(1/5)

# generate_rand_ranked_arr(chosen_n)
avg_10k_hired = check_number_hires_10k_avg(chosen_n)
print(avg_10k_hired)

find_avg_hired_all_permutations(chosen_n)

print(math.log(chosen_n))