def harmonic_sequence_total(n: int):
    sum = 0
    for i in range(1, n + 1):
        print("i: ", i)
        sum = sum + (1 / i)    
        print("current sum: ", sum)
    return sum
