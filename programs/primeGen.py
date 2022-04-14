# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# The square root of our target in this example is 775147.
# max_i = 775147
max_i = 100
primes = [2]

# Step 1)
# Come up with a small example to test our program quickly.
# For example, 23 * 3 = 69. (nice)
target = 69

# We want to check every number up to our TARGET to see if it's prime.
# We can tell if a number is prime, if all of the known prime numbers leading up to it are unable to evenly divide into it. 
for num in range(3, max_i)
    for p in primes
        if num % p == 0
            break

# Step 2)
# Start a counter from the number 3.

# Step 3)
# Create a list of prime numbers that we can use to check if other numbers are prime.

# Step 4)
# For each known prime in the list, check each one against the current counter. 
# If the number is evenly divisible (modulus equals zero),
#   then discard the number, and proceed to the next number with the counter.

# Step 5)
# If the number does NOT have any modulus that equals zero from our primes list,
#   then add the number to our list of primes. Continue to the next counter.


