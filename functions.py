'''
def square(a):
    return a*a
print(square(5))


def numVowels(string):
    string=string.lower()
    count=0
    for i in range(len(string)):
        if string[i] =='a' or string[i] =='e'  or string[i] =='i' or string[i] =='o' or string[i] =='u':
            print (string[i])
            count+=1      
    return count
  
print(numVowels("what the hell are you doingh"))      

def f2c (temp,toscale):
    if toscale.lower == "c":
        return (temp-32) *(5.0/9.0)
        
    else:
        return (temp) *(5.0/9.0) +32.0

print("enter a temp :")
temp=int(input())
print("enter the to scale to convert:")
scale=raw_input()
convertedtemp=f2c(temp,scale)
print(temp, convertedtemp,scale)

'''

'''
def fact(x):
    prod = 1
    for i in range(1,x+1):
        prod*=i
    return str(prod)
    
print("Enter a no:")
num=int(input())
print(str(num) + "! equals " + fact(num))

'''

'''
factorial using recursion

def fact(x):
    if x<=1:
        return 1
    return x * fact(x-1)
    
print("Enter a no:")
num=int(input())
print(str(num) + "! equals " + str(fact(num)))
        
'''
#Anonymoys function
#Lambda very useful -- learn more about it 
'''
square=lambda x: x*x
print (square(3)) 
'''

'''
numbers=[1,2,3,4]
numberssq= list(map(lambda x:x*x,numbers))
print(numberssq)
'''

'''
# how list , map works -> map (function to apply , input on which function should work) --- Add list outside to create a list
def square(a):
   return a*a
numbers=[1,2,3,4]
numberssq= list(map(square,numbers))
print(numberssq)
'''

'''
#Usage of filter to filter the data 
def even(a):
    if a%2 == 0:
        return True
    else:
        return False
        
numbers=range(1,11)
print(numbers)
numeven=list(filter(even,numbers))
print(numeven) 
'''


'''
def sum(x,y):
    return (x+y)
 # OR    
import functools 
numbers= range(1,11)
print (numbers) 
sum= functools.reduce(sum,numbers)
print("Sum is :"+str(sum))
'''

'''
def countletter(words):
    if len(words) == 1:
        return 1
    else:
        return len(words[0]) + countletter(words[1:])
        
sentence=["what","the","hell"]
print (sentence)
print(countletter(sentence))
'''


def firstletter(words):
    return (words[0])
        
sentence=["what","the","hell"]
print (sentence)
''' 
Issue is output is a list and not a string
acro=list(map(firstletter,sentence))
print(acro)
'''

'''
#Join converts the list output to string
acro=''
dot="."
acro=acro.join(list(map(firstletter,sentence))).upper()
print (acro)
'''
#To add a dot in between acronym
'''
import sys
print sys.version
sys.stdout.flush()
for i in acro:
    sys.stdout.write(str(i)+".")

'''

#Above program using function
import sys
print sys.version

def firstletter(words):
    return (words[0])


def acronym(words):
    acro=''
    acronew=''
    acro=acro.join(list(map(firstletter,words))).upper()
    for i in acro:
        acronew=acronew+str(i)+"."
    return acronew

sentence=["what","the","hell"]
print (sentence)
acro1=acronym(sentence)
print(acro1)