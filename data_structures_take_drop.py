
## DEMO with LIST
'''
def take(num,lyst):
    rlist=[]
    if num>0:
        for i in range(0,num):
            rlist.append(lyst[i])
        return rlist
    else:
        for i in range (len(lyst)+num, len(lyst)):
            #print("val of i:" + str(i))
            rlist.append (lyst[i])
        return rlist

def drop(num,lyst):
    rlist=[]
    for i in range(num,len(lyst)):
        rlist.append(lyst[i])
    return rlist

names=['ash','nan','ish','hmm']
print("length of list is :" + str(len(names)))
somenames=take(3,names)
print(somenames)
somenames=drop(3,names)
print(somenames)
somenames=take(-3,names)
print(somenames)
'''



## DEMO with TUPLES

'''
class point:
    def __init__ (self,x,y):
        self.point=(x,y)

    def __str__ (self):
        return "x:" + str(self.point[0]) + " y:" + str(self.point[1])

    def setlocation (self,x,y):
        self.point = (x,y)

class line:
    def __init__ (self,p1,p2):
        self.point1=p1
        self.point2=p2

    def __str__ (self):
        return "Point 1: " + str (self.point1) +'\n' \
               "Point 2: " + str (self.point2) + '\n'

## Tuple is best used for points
## Compositions -> HAS - A relationship
## A line has a point


p1 = point(1,2)
print(p1)
p1.setlocation(10,20)
print(p1)
p2=point(8,9)
line1=line(p1,p2)
print(line1)
'''

