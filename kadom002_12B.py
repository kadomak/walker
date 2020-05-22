#CSCi 1133-20
#Kowe Kadoma
#HW 12 Problem B
import random
import math
class RandomWalker():
    def __init__(self, name = "", xInit = 0, yInit = 0):
        self.name = name
        self.xInit = xInit
        self.yInit = yInit

    def getX(self): 
        return self.xInit
       
    def getY(self):
        return self.yInit
       
    def randomStep(self):
         xPos = [-1,0,1]
         yPos = [-1,1]
         xpos = [-1,1]

         if random.choice(xPos) == 0:
             self.xInit = self.getX()
             self.yInit = self.getY() + random.choice(yPos)
         else:
             self.xInit = self.getX() + random.choice(xpos)
             self.YInit = self.getY()
             
    def reset(self):
        self.xInit = 0
        self.yInit = 0
        
    def __str__(self):
        return str(self.name) + "  " + "(" + str(self.xInit) +","+ str(self.yInit)+ ")"

class BiasedRandomWalker(RandomWalker):
    def __init__(self,stepProbabilites, name="", xInit=0, yInit=0):
        self.Probabilities = stepProbabilites
        RandomWalker.__init__(self,name,xInit,yInit)

    def getProbabilities(self):
        return self.Probabilities

    def randomStep(self):
        Int = random.uniform(0,1.0)
        List = self.getProbabilities()
        if Int <= List[0][2]:
            self.xInit = List[0][0] + self.getX()
            self.yInit = List[0][1]  + self.getY()
        elif Int > List[0][2] and Int <= (List[0][2] + List[1][2]):
            self.xInit = List[1][0] + self.getX()
            self.yInit = List[1][1] + self.getY()
        elif Int > (List[0][2] + List[1][2]) and Int <= (List[0][2] + List[1][2] + List[2][2]):
            self.xInit = List[2][0] + self.getX()
            self.yInit = List[2][1] + self.getY()
        elif Int > (List[0][2] + List[1][2]+List[2][2]) and Int <= (List[0][2] + List[1][2]+List[2][2]+List[3][2]):
            self.xInit = List[3][0] + self.getX()
            self.yInit = List[3][1] + self.getY()
        elif Int > (List[0][2] + List[1][2]+List[2][2]+List[3][2]) and Int <= (List[0][2] + List[1][2]+List[2][2]+List[3][2]+List[4][2]):
            self.xInit = List[4][0] + self.getX()
            self.yInit = List[4][1] + self.getY()


class Field():
    def __init__(self, xMinInit, yMinInit, xMaxInit, yMaxInit):
        self.xMin = xMinInit
        self.yMin = yMinInit
        self.xMax = xMaxInit
        self.yMax = yMaxInit

    def isInField(self, x, y):
        if x > self.xMax or x < self.xMin:
            Result = False
        elif y > self.yMax or y < self.yMin:
            Result = False
        else:
            Result = True
        return Result
               
    def __str__(self): 
        return "x min: " + str(self.xMin) +" " + "x max: " + str(self.xMax)  + \
               "\ny min: " + str(self.yMin) + " y max: " + str(self.yMax)

class OriginWalker(BiasedRandomWalker):
    def __init__(self, stepProbabilities, name = "", xInit=0, yInit=0,OriginRevisits=0):
         BiasedRandomWalker.__init__(self,stepProbabilities,name,xInit,yInit)
         self._OriginRevisits = OriginRevisits

    def getOriginRevisits(self):
        return self._OriginRevisits

    def reset(self):
        self.xInit = 0
        self.yInit = 0
        self._OriginRevisits = 0

    def randomStep(self):
        super(OriginWalker,self).randomStep()
        if self.xInit == 0 and self.yInit ==0:
            self._OriginRevisits = self.getOriginRevisits() + 1
        
    def __str__(self):
        return str(self.name)+ " " + "Origin Revisits: " + str(self._OriginRevisits)




#main program
field = Field(-4,-4,4,4)
walker = OriginWalker([[ 1, 0,.25], [ 0, 1,.25], [-1, 0,.25], [ 0, -1,.25]], "Tom", 0,0)
walker2 = OriginWalker([[ 1, 0, .3], [ 0, 1, .2], [-1, 0, .3], [ 0, -1, .2]],"Dick",0,0)
walker3 = OriginWalker([[ 1, 0, .4], [ 0, 1, .4], [-1, 0, .1], [ 0, -1, .1]],"Harry",0,0)

countingList=[]
for i in range(100):
    while field.isInField(walker.getX(),walker.getY()) == True:
        walker.randomStep()
    countingList.append(walker.getOriginRevisits())
    walker.reset()
    countingList.sort()
Max = countingList[99]
Min = countingList[0]
Average = sum(countingList)/100
print("Tom","\nMinimum Origin Revisits:", Min, "\nMaximum Origin Revisits: ", Max, "\nAverage Origin Revisits: ", Average)



countingList=[]
for i in range(100):
    while field.isInField(walker2.getX(),walker2.getY()) == True:
        walker2.randomStep()
    countingList.append(walker2.getOriginRevisits())
    walker2.reset()
    countingList.sort()
Max = countingList[99]
Min = countingList[0]
Average = sum(countingList)/100
print("Dick","\nMinimum Origin Revisits:", Min, "\nMaximum Origin Revisits: ", Max, "\nAverage Origin Revisits: ", Average)


countingList=[]
for i in range(100):
    while field.isInField(walker3.getX(),walker3.getY()) == True:
        walker3.randomStep()
    countingList.append(walker3.getOriginRevisits())
    walker3.reset()
    countingList.sort()
Max = countingList[99]
Min = countingList[0]
Average = sum(countingList)/100
print("Harry","\nMinimum Origin Revisits:", Min, "\nMaximum Origin Revisits: ", Max, "\nAverage Origin Revisits: ", Average)

        

