class Student:
    grades=[]
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def addGrade (self,grade):
        self.grades.append(grade)

    def showGrades (self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        print ("His grades are : ")
        return grds

    def __str__(self):
        return "Student name is " + self.name

s1= Student('Ashwani','1')
s1.addGrade(100)
s1.addGrade(98)
print (s1)
print(s1.showGrades())