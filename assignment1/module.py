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


def get_prime_list_until(input: int) -> list[int]:
    output = []

    # look at all numbers until input1
    # start at 2 (we will never include 1 or 0)
    for i in range(2, input + 1):  # the +1 bc we want to include the input
        if is_prime(i):
            output.append(i)

    return output


# since this is mostly copy/paste, I need to take the same parts out and call them in their own function
def get_prime_list_until_string(until: int) -> str:
    prime_list = get_prime_list_until(until)
    output_string = ""
    for i in range(len(prime_list)):
        output_string += str(prime_list[i]) + ","
    output_string = output_string[:-1]
    return output_string
