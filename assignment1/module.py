import math


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    stopping_point = math.floor(num**0.5) + 1
    for i in range(2, stopping_point):
        if num % i == 0:
            return False
    return True


def get_prime_list_spec_len_string(output_len: int):
    prime_list = get_prime_list_spec_len(output_len)
    output_string = ""
    for i in range(len(prime_list)):
        output_string += str(prime_list[i]) + ","
    output_string = output_string[:-1]
    return output_string


def get_prime_list_spec_len(output_len: int) -> list[int]:
    prime_list = []

    counter = 2
    while len(prime_list) < output_len:
        if is_prime(counter):
            prime_list.append(counter)
        counter += 1

    return prime_list
