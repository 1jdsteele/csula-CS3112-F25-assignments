from module import (
    is_prime,
    get_prime_list_spec_len_string,
    get_prime_list_including_string,
    get_prime_factors,
)
import math

# the main
print("\nWelcome to Jake's analysis of algorithms assignment number 1.\n")

print("This assignment has 3 parts.\n")

# ++++++++++ part 1 ++++++++++
input1 = int(
    input(
        "First part: This program will output the first n primes of your input. Please input a positive integer for n.\n"
    )
)

print(
    "You have input ",
    input1,
    " and this program will now show the first ",
    input1,
    " prime numbers starting at 0 and increasing: \n",
)

print(get_prime_list_spec_len_string(input1))

# ++++++++++ part 2 ++++++++++
input2 = int(
    input(
        "Second part: Given your input, this program will output a list of all primes not exceeding your input. Please input a whole number greater than 0.\n"
    )
)

print(
    "You have input ",
    input2,
    "and this program will now show a list of primes not exceeding your input of ",
    input2,
    "\n",
)

print(get_prime_list_including_string(input2))


# ++++++++++ part 3 ++++++++++
input3 = int(
    input(
        "Third part: Given your input, this program will output a list of its prime factorization. Please input a whole number greater than 1.\n"
    )
)

print(
    "You have input ",
    input3,
    "and this program will now show a list of the prime factorization of your input of ",
    input3,
    "\n",
)

print(get_prime_factors(input3))
