'''
numbers=[1,2,3,4,5]
it=iter(numbers)
#print(it.__next__()) -- doesnt work in 2.7
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # fails traceback error as list is over
'''

'''
numbers=[1,2,3,4,5]
it=iter(numbers)
i=0
y=len(numbers)
#print i
while (i<y):
    print(next(it))
    i=i+1
    '''
    
'''
maps={"ashwani":"1","nandini":"2"}
for key in maps.keys():
    print(key,maps[key])
'''

'''
maps={"ashwani":"1","nandini":"2"}
it=iter(maps)
for key in it:
    print(key,maps[key])

'''

'''
numbers=range(1,10)
it=iter(numbers)
print(next(it))
'''

'''


import os
#print(dir)
dir = r'A:\Ash Learning\Python Udemy courseera\Ash_Exercises'
files=os.popen('dir *.py')
fileit=iter(files)
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
'''

'''
square=((10,8),(10,23),(25,23),(25,8))
for points in square:
    print(points)
   '''
    
import os
#print(dir)
dir12 = r'A:\Ash Learning\Python Udemy courseera\Ash_Exercises'
files=os.popen('dir12 *.py')
fileit=iter(files)
print(next(fileit))
print(next(fileit))
