# what is class 
# a class is a blueprint for creating objects. 
# syntax
# class my_car():
#     pass

class Car:
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model

car1 = Car("BMW" , "XS")
print(car1.brand) #BMW
print(car2.model) #XS
