import math

def isPrime(num: int) -> bool:
    if num < 2: return False
    stopping_point = math.floor(num ** 0.5) + 1
    for i in range(2, stopping_point):
        if num % i == 0: return False
    return True