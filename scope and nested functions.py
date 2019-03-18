# Though number is defined outside the def of function the variable is accessible.
# Global variable can be accessed anywhere if defined outside a function or class
'''
def getnumber( ):
    print number
    
number=1
getnumber()
'''

# output is 2 because the fuction uses the local variable value
'''
def getnumber( ):
    number=2
    print number
    
number=1
getnumber()

'''

'''
#nested scope
#Function defined inside another function can have access to variable of outer function
import math
def hyp(a,b):
    def square(c):
        return c*c
    return str(math.sqrt(square(a) + square(b)))

print("Length of side 1 pls :")
s1=int(input())
print("Length of side 2 pls :")
s2=int(input())
hyp=hyp(s1,s2)
print("The hypotenuse is : " + hyp)
'''

'''
### Newtons square root solve
print ("enter the number:")
number = int(input ())
print ("number is " + str (number))
print ("Whats your guess for square root?")
guess = int(input ())
sqrt1 = (1 / 2 ) * ((number/guess)+ guess)
print("Square root is " + str(sqrt1))

'''

import math

def square(a):
    return a*a

def squareroot(number,guess):
    sqrt1 = (1 / 2) * ((number / guess) + guess)
    fn_result = float(math.fabs((square(sqrt1)-number)))
    print("sqrt1 is " + str(sqrt1))
    print ("fn_result is " + str (fn_result))
    if (fn_result < 0.3):
        return sqrt1
    else:
        return squareroot(number,sqrt1)

print ("enter the number:")
in_number = int(input ())
print ("Whats your guess for square root?")
in_guess = float(input ())
result = float(math.fabs((square(in_guess)-in_number)))
if result < 0.1:
    print("Square root is : " + str(in_guess))
else:
    print("Square root is " + str(squareroot(in_number,in_guess)))



