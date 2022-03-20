# Fizz buzz program
# Count from 1 to 100
# IF the number is a multiple (or divisible) by 3
#    THEN print "fizz"
# IF the number is a multiple (or divisible) by 5
#    THEN print "buzz"
# IF the number is divisible by BOTH 3 and 5
#    THEN print "fizzbuzz"


# How do we count from 1 to 100
# for i in range (5) :
#    print (i)

# This is how to find if a number is evenly divisible
# a = 10 % 3
# print (a)

# EXAMPLE IF STATEMENT
# spam = 0
# if spam < 5:
#    print('Hello, world.')
#    spam = spam + 1

for i in range (1, 11):
#    print (i)
    if (i % 3 == 0) and (i % 5 == 0):
        print ("fizzbuzz")
    elif (i % 5 == 0):
        print ("buzz")
    elif (i % 3 == 0):
        print ("fizz") 
    else:
        print (i)
