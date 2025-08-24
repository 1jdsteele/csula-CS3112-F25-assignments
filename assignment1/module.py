import math


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    stopping_point = math.floor(num**0.5) + 1
    for i in range(2, stopping_point):
        if num % i == 0:
            return False
    return True


def get_prime_list_spec_len_string(output_len: int) -> str:
    prime_list = get_prime_list_spec_len(output_len)
    return convert_list_to_string(prime_list)


def get_prime_list_spec_len(output_len: int) -> list[int]:
    prime_list = []

    counter = 2
    while len(prime_list) < output_len:
        if is_prime(counter):
            prime_list.append(counter)
        counter += 1

    return prime_list


def get_prime_list_including(input: int) -> list[int]:
    output = []
    for i in range(2, input + 1):  # 2 bc first prime, 1 because include the input
        if is_prime(i):
            output.append(i)
    return output


def get_prime_list_including_string(including: int) -> str:
    prime_list = get_prime_list_including(including)
    return convert_list_to_string(prime_list)


def convert_list_to_string(entry: list[int]) -> str:
    output_string = ""
    for i in range(len(entry)):
        output_string += str(entry[i]) + ","
    output_string = output_string[:-1]
    return output_string


def get_prime_factors(entry: int) -> str:
    output_arr = get_prime_factors_arr(entry)
    output_dict = get_prime_factors_dict(output_arr)
    output_string = get_prime_factors_string(output_dict)

    return output_string


# def get_prime_factors_arr(entry: int) -> list[int]:
#     output = [entry]
#     if is_prime(output[0]) or entry < 2:
#         return output

#     possiblePrimeDivisors = []
#     possiblePrimeDivisors = get_prime_list_including(entry)

#     while not is_prime(output[0]):
#         for k in range(len(possiblePrimeDivisors)):
#             while output[0] % possiblePrimeDivisors[k] == 0:
#                 output.append(possiblePrimeDivisors[k])
#                 output[0] //= possiblePrimeDivisors[k]

#     output.sort()
#     return output


# TO DO: refactor below so like above it keeps rolling through a single prime
def get_prime_factors_arr(entry: int) -> list[int]:
    output = [entry]
    if is_prime(output[0]):
        return output

    possiblePrimeDivisors = get_prime_list_including(entry)

    while not is_prime(output[0]):
        for k in range(len(possiblePrimeDivisors)):
            if output[0] % possiblePrimeDivisors[k] == 0:
                output.append(possiblePrimeDivisors[k])
                output[0] //= possiblePrimeDivisors[k]
                continue

    output.sort()
    return output


def get_prime_factors_dict(entry: list[int]) -> dict:
    output_dict = {}
    for i in range(len(entry)):
        if entry[i] not in output_dict:
            output_dict[entry[i]] = 1
        else:
            output_dict[entry[i]] += 1

    return output_dict


def get_prime_factors_string(prime_occurrunces: dict) -> str:
    output_string = ""
    for prime in prime_occurrunces:
        output_string += str(prime)
        if prime_occurrunces[prime] > 1:
            output_string += "^" + str(prime_occurrunces[prime])
        output_string += "*"
    output_string = output_string[:-1]

    return output_string
