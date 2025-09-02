import random
from module import print_case

# introduction statement
print(
    "Welcome to Jake's assignement number 2 for analysis of algorithms. In this assignement we will sort randomly aorted arrays by two different methods. The arrays can have a length 2-10 and can include any number 0-100.\n"
)

user_option = 1

while user_option:

    user_option = int(
        input(
            "Input 1 to see selection sorting.\nInput 2 to see insertion sorting.\nInput 3 to see selection sorting stepwise.\nInput 4 to see insertion sorting stepwise.\nInput 0 to quit the program.\n"
        )
    )

    print_case(user_option)

print("Thank you for your time. Goodbye world")
