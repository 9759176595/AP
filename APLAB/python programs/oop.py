##class Rectangle:
##    def Area(self,length,breadth):
##        print("Length=",length)
##        print("Breadth=",breadth)
##        return length*breadth
##ob1=Rectangle()
##print("Area of rectangle=",ob1.Area(3,4))


##class Prac:
##   x=5
##   def disp(self,x):
##        x=30
##        print("THe value of local variable x is",x)
##       print("the value of instance variable x is",x)
##ob=Prac()
##ob.disp(50)
##
##class Prac:
##   x=5
##   def disp(self,x):
##        x=30
##        print("THe value of local variable x is",x)
##       print("the value of instance variable x is",self.x)
##ob=Prac()
##ob.disp(50)

#SElf parameter with method
##class Self_Demo:
##    def Method_A(self):
##        print("In method A")
##        print("WOw got a called from A!!!")
##    def Method_B(self):
##        print("In method B Calling method A")
##        self.Method_A()
##Q=Self_Demo()
##Q.Method_B()

#Display class attribute and methods
##class DisplayDemo:
##    Name=' ';
##    Age=' ';
##    def read(self):
##        Name=input('Enter name of Student')
##        print("Name",Name)
##        Age=input('Enter age of student')
##        print("Age",Age)
##D1=DisplayDemo()
##D1.read()

#Aceessibility
##class Person:
##    def __init__(self):
##        self.Name='Bill Gates'
##        self.__BankAccNo=10101
##
##    def Display(self):
##        print("Name=",self.Name)
##        print("Bank Acount no=",self.__BankAccNo)
##
##P=Person()
###Access public attributte outside class
##print("Name=" ,P.Name)
##P.Display()
###TRy to acese private variable outside class butfails
##print("Salary",P.__BankAccNo)
##P.Display()


##init method
class Circle:
    def __init__(self,pi):
        self.pi=pi
    def calc_area(self,radius):
        return self.pi*radius**2
C1=Circle(3.14)
print("area of circle is=",C1.calc_area(5))

















              

















