# what is class 
# a class is a blueprint for creating objects. 
# syntax
# class my_car():
#     pass

# class Car:
#     def __init__(self , brand , model):
#         self.brand = brand 
#         self.model = model

# car1 = Car("BMW" , "XS")
# print(car1.brand) #BMW
# print(car2.model) #XS

# class with methods

# class college :
#     colleges = " abc college"

#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print(f"The name of student is {self.name} and college is {college.colleges}")

# info1 = college("abhi")
# info1.info()
# info2 = college("adi")
# info2.info()
# s1 = college("abhi")
# s2 = college ("adi")

# print(s1.name, college.colleges) #abhi
# print(s2.name , college.colleges) #adi
# print(college.colleges) #abc college


# class fruits:
#         def __init__ (self, name):
#           self.name = name 
#         def __str__(self):
#              print(f"The fruit name is {self.name}")
# fruit1 = fruits ("mango")
# fruit1.__str__()

# Encapsulation (Protecting Data)

class bankacc:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amt):
        self.balance+= amt
    def show(self):
        print(f"Your new balance after deposit is {self.balance}")
    def withdraw(self, amt):
        if amt > self.balance:
            print("Not enough balance")
            print(f"your balance is {self.balance}")
        else:
            self.balance -= amt
            print(f"Your new balance after withdrawal is {self.balance}")    
acc1 = bankacc(1000)
print (f"initial bal = {acc1.balance}")
acc1.deposit(500)
acc1.show()
acc1.withdraw(400)

      