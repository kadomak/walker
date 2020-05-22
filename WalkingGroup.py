#CSci 1133-20
#Kowe Kadoma
#HW 12 Problem A
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

    def __eq__(self,walker2):
        if self.xInit == walker2.xInit and self.yInit == walker2.yInit:
            return True
        else:
            return False

    def __lt__(self,walker2):
        walkerDistance = math.sqrt(self.xInit**2 + self.yInit**2)
        walker2Distance = math.sqrt(walker2.xInit**2 + walker2.yInit**2)
        if walkerDistance < walker2Distance:
            return True
        else:
            return False     
        
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

class WalkerGroup():
    def __init__(self, fieldObj, walkers, stepCount =0):
        self.steps = stepCount
        self.field = fieldObj
        self.walkers = walkers

    def getStepCount(self):
        return self.steps
    
    def allTakeOneStep(self):
        List = self.walkers
        List[0].randomStep()
        List[1].randomStep()
        List[2].randomStep()
        List[3].randomStep()    
        self.steps = self.getStepCount() + 1

    def countMeetings(self): 
        List = self.walkers
        count = 0
        for i in range(len(List)):
             for j in range(i+1,len(List)):
                if List[j] == List[i]:
                    count += 1
        return count         

    def numberOut(self):
        List = self.walkers
        Outsiders = 0
        for i in range(List):
            if sielf.field.isInField(List[i].getX(),List[i].getY()) == False:
                Outsiders +=1        
        return Outsiders

    def __str__(self):
        self.walkers.sort()
        result =  "\nField: \n" + str(self.field) + "\n"
        for element in self.walkers:
            result = result + str(element) + "\n"
        return result + "\nNumber of Steps: "+ str(self.steps) 


#main program
field = Field(-5,-5,5,5)
walkerList =[RandomWalker("Tom",0,0),RandomWalker("Dick",0,0),BiasedRandomWalker([[1, 0, .24], [0, 1, .24], [-1, 0, .24], [0, -1, .24], [1, 1, .04]],"Harry",0,0), BiasedRandomWalker([[1, 0, .23], [0, 1, .23], [-1, 0, .23], [0, -1, .31]],"Jane",0,0)]
walkers = WalkerGroup(field,walkerList,0)
count = walkers.countMeetings()

while field.isInField(walkerList[0].getX(),walkerList[0].getY()) == True and field.isInField(walkerList[1].getX(),walkerList[1].getY()) == True and field.isInField(walkerList[2].getX(),walkerList[2].getY()) ==True and field.isInField(walkerList[3].getX(),walkerList[3].getY()) == True:
    walkers.allTakeOneStep()
    walkers.countMeetings()

print(walkers)
print("Number of meetings:",count)

  



    


