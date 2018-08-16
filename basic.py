'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class node:
    def __init__ (self):
        self.N = None;
        self.NE = None;
        self.E = None;
        self.SE = None;
        self.S = None;
        self.SW = None;
        self.W = None;
        self.NW = None;
    
    def getN (self):
        return(self.N);
    
    def setN (self, newN):
        self.N = newN;
    
    def getNE (self):
        return(self.NE);
        
    def setNE (self, newNE):
        self.NE = newNE;
    
    def getE (self):
        return (self.E);

    def setE (self, newE):
        self.E = newE;
    
    def getSE (self):
        return (self.SE);
    
    def setSE (self, newSE):
        self.SE = newSE;

    def getS (self):
        return (self.S);
    
    def setS (self, newS):
        self.S = newS;
    
    def getSW (self):
        return (self.SW);

    def setSW (self, newSW):
        self.SW = newSW;
    
    def getW (self):
        return (self.W);
    
    def setW (self, newW):
        self.W = newW;    

    def getNW (self):
        return (self.NW);
    
    def setNW (self, newNW):
        self.NW = newNW;
    
class cell (node):
    def __init__ (self):
        value = None;
        candidates = [];
    
    def setValue (self, newValue):
        self.value = newValue;

    def getValue (self):
        return self.value;
    
    def addCandidate (self, newCandidate):
        self.candidates.append(newCandidate);
    
    def removeCandidate (self, delCandidate):
        self.candidates.remove(delCandidate);
        

class grid:
    def __init__(self, width, length):
        self.anchor = cell();
        buff = self.anchor;
        for x in range(1, ((width+length)-1)):
            buff.setE(cell());
            buff = buff.getE();
            
    def getTotalNodes(self):
        total = 0;
        buff = self.anchor;
        while buff.getE() != None:
            total = total+1;
            buff =  buff.getE();
        return total;

        
        
        
        
        
        
        
x = cell();
x.setN(1);
x.setNE(2);
x.setE(3);
x.setSE(4);
x.setS(5);
x.setSW(6);
x.setW(7);
x.setNW(8);

g=grid(1,1);
print (g.getTotalNodes());




print (x.getNE());
print("Hello World")
