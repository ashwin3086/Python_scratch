

#print list of files from a directory
'''
import os
dir = r'A:\Ash Learning\Python Udemy courseera\Ash_Exercises'
files = os.popen("dir *.py")
for file in files:
    print(file,end='')

'''



#NOT WORKING
'''
#version 2 of above print files from directory
import subprocess

proc= subprocess.Popen('ls', stdout=subprocess.PIPE)
output= proc.stdout.read()
print (output)
'''
