class computer:
   def __init__(self,RAM,storage,weight):
     self.RAM=RAM
     self.storage=storage
     self.weight=weight
   def getspecs(self):
     self.RAM=input("enter the RAM size")
     self.storage=input("enter the storage size")
     self.weight =input("enter the weight")
   def displayspecs(self):
     print("The RAM size of the computer is",self.RAM)
     print("the storage of the computer is",self.storage)
     print("the weight is",self.weight)

class laptop(computer):
   def lapspecs(self):
     self.lapweight=input("enter the weight of laptop")
   def getweight(self):
      print("weight of laptop is",self.lapweight)

class desktop(computer):
   def deskspecs(self):
     self.deskdisplay=input("enter the display size of desktop")
   def getdisplay(self):
      print("display size of desktop is",self.deskdisplay)


obj1=desktop('','','')
obj2=laptop('','','')
obj2.getspecs()
obj2.displayspecs()
obj2.lapspecs()
obj2.getweight()
obj1.deskspecs()
obj1.getdisplay()