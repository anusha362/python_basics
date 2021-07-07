class student:
    def __init__(self,name,hodname):
        self.name=name
        self.hodname=hodname
    def getData(self):
        self.name=input("enter your name: ")

class hod(student):
    def putData(self):
        self.hodname=input("enter hod name: ")
    def display(self):
        print("Student name is",self.name)
        print("hod name is",self.hodname)
class princi(hod):
    def fun3(self):
        print("This is principal of hod")
class management(princi):
    def fun4(self):
        print("This is the management")
obj=management("","")
obj.getData()
obj.putData()
obj.display()
obj.fun3()
obj.fun4()