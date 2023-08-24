#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Convert the number to a string
string_number = str(number)

# Get the absolute value of the last digit
last_digit = abs(int(string_number[-1]))

# Print the last digit of the number
print('Last digit of %s is %d' % (string_number, last_digit), end=" ")

# Check the properties of the last digit and print additional information
if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')

