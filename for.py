'''
numbers=[1,2,3,4,5]
sum = 0
for i in numbers:
    sum=sum+i
print sum
'''

'''
sentence="now is the time for all the good people to come to aid"
count=0
for letter in sentence:
    if letter =="a" or letter =="e" or letter =="i" or letter =="o" or letter =="u":
        count=count +1
        
print("No of vowels :"+str(count))
'''

'''
numbers=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(numbers),2):
    print numbers[i]

'''

'''
numbers=(1,2,3,4,5,6,7,8,9,10)
for i in range(0,len(numbers),2):
    print numbers[i]
'''

'''
words=("now","is", "the","time")
max=0
for i in range(0,len(words)):
    if len(words[i])>max:
        max=i
print ("longest word is " + words[max])
'''

'''
maps={"ashwani":"1","nandini":"2"}
#print (maps.keys())
for i in maps.keys():
    print (i + " extension is :" +maps[i])
'''

#use stdout to remove new line characters at end of output of for loop in 2.7
'''
import sys
print sys.version
sys.stdout.flush()
#from __future__ import print_function
for i in open('grades.txt'):
    sys.stdout.write(i)
'''


print("Enter a number:")
num = int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print (str(num)+"!= "+str(fact))
    