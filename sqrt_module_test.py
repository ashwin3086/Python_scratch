from sqrt_module import *
import math

print ("enter the number:")
in_number = int(input ())
print ("Whats your guess for square root?")
in_guess = float(input())
result = float(math.fabs((square(in_guess)-in_number)))
if result < 0.1:
    print("Square root is : " + str(in_guess))
else:
    print("Square root is " + str(squareroot(in_number,in_guess)))


