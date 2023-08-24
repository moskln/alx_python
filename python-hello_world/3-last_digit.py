#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

string_number = str(number)
last_digit = int(string_number[-1])

if number <= 0:
    sign = "-"
    print(f'Last digit of %s is {sign}%d' % (string_number, last_digit), end=" ")

else:
    print('Last digit of %s is %d' % (string_number, last_digit), end=" ")

if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
