#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

string_number = str(number)
Last_digit = str(string_number[-1])
if number <= 0:
    sign = '-'
    last_digit = int(sign + Last_digit)
    print('Last digit of %s is %d' % (string_number, last_digit), end=" ")
    if last_digit > 5:
        print('and is greater than 5')
    elif last_digit == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
else:
    sign = ''
    last_digit = int(sign + Last_digit)
    print('Last digit of %s is %d' % (string_number, last_digit), end=" ")
    if last_digit > 5:
        print('and is greater than 5')
    elif last_digit == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
