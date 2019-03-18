#creating your own object/datatype
# Class  - Definition of a abstract data type in a program
# Object - Particular instance of class definition
# aName = name('john','Doe')
# HEre name is class and aName is object


class Name:
    #constuctor  methods-- declaration/instantiation
    #This first part talks about attributes of class
    def __init__(self,first,middle,last):
        self.first=first
        self.middle=middle
        self.last=last
   #this talks about behavior /current state of object
    def __str__(self):
        return self.first+ " " + self.middle + " " + self.last

    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]
# Here we are instantiating it
# Now in teh above class the self.first is basically assigned with Ashwani
var_name=Name('Ashwani' ,'Kumar','Kammara')
print(var_name)
print(var_name.initials())


