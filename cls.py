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

class college :
    colleges = " abc college"

    def __init__(self, name):
        self.name = name
s1 = college("abhi")
s2 = college ("adi")

print(s1.name) #abhi
print(s2.name) #adi
print(college.colleges) #abc college
        