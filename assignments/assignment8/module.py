import random

def harmonic_sequence_total(n: int):
    sum = 0
    for i in range(1, n + 1):
        # print("i: ", i)
        sum = sum + (1 / i)    
        # print("current sum: ", sum)
    return sum

def generate_rand_ranked_arr(num_ranks: int) -> list[int]:
    arr = []
    for i in range(1, num_ranks + 1):
        arr.append(i)
    for i in range(num_ranks):
        rand_index = random.randint(i, num_ranks - 1)
        arr[i], arr[rand_index] = arr[rand_index], arr[i]
    print(arr)
    return arr


def check_number_hires(rand_ranked: list[int]) -> int:
    num_hires = 0
    current_hire = len(rand_ranked) + 1
    for i in range(len(rand_ranked)):
        if rand_ranked[i] < current_hire:
            num_hires = num_hires + 1
            current_hire = rand_ranked[i]
    print(num_hires)
    return num_hires

def check_number_hires_10k_avg(applicant_num: int) -> float:
    total_num_hired = 0
    for i in range(10001):
        rand_ranked = generate_rand_ranked_arr(applicant_num)
        total_num_hired = total_num_hired + check_number_hires(rand_ranked)
    avg_num_hired = total_num_hired / 10000
    print("average number hired: ", avg_num_hired)
    return avg_num_hired