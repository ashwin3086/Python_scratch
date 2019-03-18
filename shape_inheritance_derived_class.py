'''

Inheritance is a relationship

car is a vehicle
manager is a employee

rectangle is a shape
    Shapes have attributes


'''


class shape:
    def __init__(self,xcor,ycor):
        self.x=xcor
        self.y=ycor

    def __str__(self):
        return 'x : ' + str(self.x) + ' y :' + str(self.y)

    def move (self,x1,y1):
        self.x=self.x + x1
        self.y = self.y + y1

class rectangle(shape):
    def __init__(self,xcor,ycor,length,height):
        shape.__init__(self,xcor,ycor)
        self.length=length
        self.height=height

    def __str__(self):
        retstr = shape.__str__(self)
        retstr += ' length : ' + str(self.length) + \
                  ' height : ' + str (self.height)
        return retstr


rec=rectangle(5,10,15,20)
print(rec)
rec.move(10,10)
print(rec)