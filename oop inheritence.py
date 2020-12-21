class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name

    def isemployee(self):
        return False
        print("sorryyy you are not a employee at that time")

class employee(person):

    def isemployee(self):
        return True
        print("welcome in your company you are the employee at that company")

emp=person("geek1")
print(emp.getname(),emp.isemployee())
emp=employee("geeks")
print(emp.getname(),emp.isemployee())


class base1(object):
    def __init__(self):
        self.str1="geek"
        print(base1)

class base2(object):
    def __init__(self):
        self.str2="geekyshows"
        print(base2)

class derived(base1,base2):
    def __init__(self):

        base1.__init__(self)
        base2.__init__(self)
        print("derived class")
    def printstr(self):
        print(self.str1,self.str2)

obj3=derived()
obj3.printstr()
obj3.str2
obj3.str1


contact={"waqas":+923016636957648,"rizwan":+922343247344,"usman":+9223435554445,"mudasir":+923454544345,"awais":+9234454657676
         ,"ayesha":+9234454544343,"memona":+92345445457744,"farzeen":+923443745457453}

for name,number in contact.items():
    print("{} has a phone number {}".format(name,number))

contactus={"waqas":+923016957654566648,"rizwan":+922343247344,"usman":+9223435554445,"mudasir":+923454544345,"awais":+9234454657676
         ,"ayesha":+9234454544343,"memona":+92345445457744,"farzeen":+923443745457453}


for key,value in contactus.items():
    print("%s is name and number is :%s"%(key.upper(),value))





