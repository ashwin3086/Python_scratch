class person:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=int(age)

    def __str__(self):
        return self.name +' ' + self.sex + ' ' + str(self.age)

    def changename(self,name):
        self.name=name

    def changeage(self):
        self.age = self.age + 1


person1 = person('Ashwani','M','32')
person2 = person('Nandu','F','32')

print('Person 1 : ' + str(person1))
print('Person 2 : ' + str(person2))
person1.changeage()
print('Person 1 : ' + str(person1))