import math

#functions
def isPrime(num: int) -> bool:
    if num < 2: return False
    stopping_point = math.floor(num ** 0.5) + 1
    for i in range(2, stopping_point):
        if num % i == 0: return False
    return True

#the main
print("\nWelcome to Jake's analysis of algorithms assignment number 1.\n")

print("This assignment has 3 parts.\n")

# ++++++++++ part 1 ++++++++++
input1 = int(input("First part: This program will output the first n primes of your input. Please input a positive integer for n.\n"))

print("You have input ", input1, " and this program will now show the first ", input1, " prime numbers starting at 0 and increasing: \n")

output1 = []

counter = 2
while len(output1) < input1:
    if isPrime(counter): output1.append(counter)
    counter += 1

print(output1, "\n")

# ++++++++++ part 2 ++++++++++
input2 = int(input("Second part: Given your input, this program will output a list of all primes not exceeding your input. Please input a whole number greater than 0.\n"))

print("You have input ", input2, "and this program will now show a list of primes not exceeding your input of ", input2, "\n")

output2 = []

# look at all numbers until input1 
# start at 2 (we will never include 1 or 0)
for i in range(2, input2 + 1): #the +1 bc we want to include the input
    if isPrime(i): output2.append(i)
   

print(output2, "\n")

# ++++++++++ part 3 ++++++++++
input3 = int(input("Third part: Given your input, this program will output a list of its prime factorization. Please input a whole number greater than 1.\n"))

print("You have input ", input3, "and this program will now show a list of the prime factorization of your input of ", input3, "\n")


output3Arr = [input3]
print("here is the initial input3 array: ", output3Arr)


isFullyPrimeFactored = False
while not isFullyPrimeFactored:
    nonPrimeTriggered = False
    for i in range(len(output3Arr)):
        if not isPrime(output3Arr[i]): nonPrimeTriggered = True
    if not nonPrimeTriggered: 
        isFullyPrimeFactored = True
        continue
    #otherwise there was a non prime and we must deal with it
    for i in range(len(output3Arr)):
        #loop through until we find a non prime
        if not isPrime(output3Arr[i]):
            #then we figure out what two numbers it is possible to be divisible by
            # question: should I use a list of primes up to the square root to find divisors?
            #yes - adapt from part 2! turn it into a function and then use that here
            possiblePrimeDivisors = []
            for j in range(2, math.floor(math.sqrt(output3Arr[i])) + 1): #the +1 bc we want to include the input
                if isPrime(j): possiblePrimeDivisors.append(j)
            #now I have filled a list of possible Prime Divisors. Now go through the list from the beginning until you find one that gives a mod == 0
            for k in range(len(possiblePrimeDivisors)):
                if output3Arr[i] % possiblePrimeDivisors[k] == 0:
                        #at this point we have found a prime divisor
                        #then we replace the non prime with one divisor and append the other divisor - maybe that is backwards order?
                        # I ACCIDENTALLY DID SOMETHING REALLY SMART HERE
                        # BY APPENDING THE PRIME DIVISOR, THE NON PRIME IS ALWAYS FIRST
                        # THEREFORE, I DO NOT HAVE TO LOOP, JUST LOOK AT THE FIRST INDEX!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        output3Arr.append(possiblePrimeDivisors[k] )
                        output3Arr[i] /= possiblePrimeDivisors[k] 
                        output3Arr[i] = int(output3Arr[i] )
                        #then we continue to because we just messed with the length of the array
                        continue

#at this point we have an array of all the prime factors
# print(output3Arr)
#convert that array to the specifed output type via a map
output3Arr.sort()
print(output3Arr)

output3_dict = {}
for i in range(len(output3Arr)):
    if output3Arr[i] not in output3_dict:
        output3_dict[output3Arr[i]] = 1
    else: output3_dict[output3Arr[i]] += 1

print(output3_dict)

# now let's take that map that is nicely ordered and make his string
output3_string = ""
for entry in output3_dict:
    output3_string += str(entry)
    if output3_dict[entry] > 1:
        output3_string += "^" + str(output3_dict[entry])
    output3_string += "*"
output3_string = output3_string[:-1]

print(output3_string)


