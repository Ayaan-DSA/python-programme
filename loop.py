# for loop
# for i in range(10, 1, -1):
  #  print(i)
    # while loop
#i = 10
#while i > 0:
   # print(i)
   # i -= 1
# for i in range(10):
#     if i == 4:
#         continue
    
#     if i == 9:
#         break

#     if i == 7:
#         pass
#     print(i)

# --print table till user say stop--

# while True:
#     num = int(input("Enter a number = "))
#     for i in range(1, 11):
#         print( num * i)
#     inp = input("do you want to exit ?? (yes / no  ")
#     if inp == "yes":
# #        break  
# 
# --- Function --- 
# def print_hello():
#     print("Hello world")

# print_hello()

# def sum():
#     a = int(input("first number = "))
#     b = int(input("second number = "))
#     return a+b

# result = sum()
# print(result)

# def add(a , b):
#  result = a + b
#  print(result)

# n1 = int(input("first number = "))
# n2 = int(input("second number = ")) 
# add(n1 , n2)

def area(side):
    return side * side
side = int(input("Enter side of square = "))
result = area(side)
print(result) 

