class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getData(self):
        self.name=input("enter your name: ")
        self.mark=input("enter your mark: ")
    def putData(self):
        print(self.name,"\n",self.mark)

obj=student("","")
obj.getData()
obj.putData()
