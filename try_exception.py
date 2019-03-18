
'''
try:
    statements
except:
    stateements
finally:
    statements
    #wil be executed no matter what
    #ex close files etc

'''

## Raising own exception

'''
class rational:
    def __init__ (self,x,y):
        numer=x
        if y==0:
            raise zerodivisionerror()
        else:
            denom=y

try:
    rat1 = rational(4,1)
    rat2 = rational(4,0)
except:
    print("cannot have 0 as denominator")
'''

'''
def calc(op1,op2,op):
    if op=='+':
        return op1 + op2
    elif op=='-':
        return op1 - op2
    elif op=='*':
        return op1 * op2
    elif op=='/':
        return op1 / op2

cont='y'
while cont != 'n':
    print ("Enter the first number")
    num1=int(input())
    print ("Enter the second number")
    num2 = int (input ())
    print ("Enter the operation")
    op = str (input ())

    if op == '/' and num2 == 0:
        print ("cannot divide by 0")
        continue
    else:
        print (calc(num1,num2,op))
    print ("do you want to continue (y/n)?")
    cont=input()
'''

def calc(op1,op2,op):
    if op=='+':
        return op1 + op2
    elif op=='-':
        return op1 - op2
    elif op=='*':
        return op1 * op2
    elif op=='/':
        return op1 / op2

import os
print ("Enter the file name to open:")
name=input()
while not os.path.isfile(name):
    print ("File doesnt exist")
    print ("Enter file name to open:")
    name=input()

file=open(name,'r')
for line in file:
    print(line,end='')

