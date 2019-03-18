#List comprehensions are shortcut for for loop

'''
grades=[10,20,30,40]
print(grades)
grades=[grade+5 for grade in grades]
print(grades)
'''

'''
file= open('grades.txt')
grades=file.readlines()
print grades
for i in range(len(grades)):
    grades[i]=grades[i].rstrip() #remove new line character 
'''

'''
grades=[grade.rstrip() for grade in open('grades.txt')]
print (grades)
'''

'''
N=range(1,101)
even = [x for x in N if x % 2==0]
print (even)

'''

sent="hey what the hell are you doing"
sent += "come on tell me are you ok"
words=sent.split(' ')
wlen=[(word, len(word)) for word in words]
print(wlen)