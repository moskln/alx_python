#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
print('Last digit of %s is %s' %(string_number, string_number[-1]), end=" ")
Number = int(string_number[-1])
if Number > 5:
    print('and is greater than 5')
elif Number == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
