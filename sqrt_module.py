import math
def squareroot(number,guess):
    sqrt1 = (1 / 2) * ((number / guess) + guess)
    fn_result = float(math.fabs((square(sqrt1)-number)))
    print("sqrt1 is " + str(sqrt1))
    print ("fn_result is " + str (fn_result))
    if (fn_result < 0.3):
        return sqrt1
    else:
        return squareroot(number,sqrt1)

def square(a):
    return a*a

