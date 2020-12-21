class employeesA:
#class objects and constructors
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("my name is ",self.name)

    def setaddress(self,address):
        self.address=address

    def getaddress(self):
        return self.address

    def fun(self):
        print("basic class in python")

    def marks(self):
        pass


class myinto:
    class_variable=0
    def no(self,no_inc):
        self.class_variable+=no_inc
        print(self.class_variable)
obj2=myinto()
obj2.no(34)
obj2.no(45)
obj2.no(67)
print(obj2.class_variable)


obj=employeesA("waqas")
obj.fun()
obj.hello()
obj.setaddress("razabad chowk suraj miani roal multan")
print(obj.getaddress())

